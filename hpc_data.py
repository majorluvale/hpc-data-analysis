import requests
import numpy as np
import pandas as pd

def getPlanData(year, globalClusterId):
    """This function return planData by year. PlanData include planId,Country,iso,name,	planType,isReleased,planCostingType,inNeed,target,cumulativeReach,requirements,funding,cashTransferFunding for HLP only"""
    
    #Get Cluster info by Code
    try:
        code, clustername = getGlobalClusterInfoByCode(globalClusterId)
        if code is not None and clustername is not None:
            print(f'Cluster code: {code}, Cluster name: {clustername}')
        else:
            return
    except TypeError as e:
        print("The Global cluster code is incorrect!", e)
        return
    
    try:
        year = int(year)
        assert year >= 2019  and year <= 2026, "The year must be an integer between 2019 and 2026"
    except AssertionError as e:
        print("An error occured! ", e)
        return
        

    
    url = "https://api.hpc.tools/v2/public/planSummary"
    params = {
        "year": year,
        "includeIndicators": True,
        "includeCaseloads": True,
        "includeFinancials": True,
        "includeDisaggregatedData": True,
    }

    try:
        r = requests.get(url, params=params)
        data = r.json()["data"]["planData"]
    
    except requests.exceptions.ConnectionError as conErr:
        print("The connection was not succefull! ", conErr)
        return

    plans = pd.json_normalize(data, max_level=1)[
        [
            "planId",
            "planYear",
            "name",
            "planType",
            "isReleased",
            "planCostingType",
            "planFocusCountry.name",
            "planFocusCountry.iso3",
        ]
    ]
    plans.rename(
        columns={"planFocusCountry.name": "Country", "planFocusCountry.iso3": "iso3"},
        inplace=True,
    )
    print("Working on caseloads")
    caseloads = pd.json_normalize(data, record_path=["caseloads"], meta=["planId"])

    # Exploser la liste
    print("Extracting reached People")
    cumilativeReach = caseloads.explode("measurements")
    cumilativeReach["measurements"] = cumilativeReach["measurements"].apply(
        lambda x: {} if pd.isna(x) else x
    )
    cumilativeReach = pd.json_normalize(cumilativeReach["measurements"])[
        "cumulativeReach"
    ]
    df = caseloads.join(cumilativeReach)

    # Filter by GlobalCluster code
    df = df[df["availableGlobalClusterCode"] == code]
    todelete = [
        "caseloadId",
        "caseloadCustomRef",
        "caseloadType",
        "caseloadDescription",
        "availableGlobalClusterCode",
        "entityId",
        "totalPopulation",
        "affected",
        "measurements",
    ]
    df.drop(todelete, axis=1, inplace=True)
    # df = df[['planId', 'planYear', 'planType', 'shortName','planType', 'inNeed', 'target', 'cumulativeReach', 'isReleased']]
    # df.rename(columns={'shortName': 'country'}, inplace=True)
    df.inNeed = pd.to_numeric(df["inNeed"], errors="coerce")
    df.target = pd.to_numeric(df["target"], errors="coerce")
    df.cumulativeReach = pd.to_numeric(df["cumulativeReach"], errors="coerce")

    # Ajout des détails de financement
    print("Working on requirements funding")
    requirements = [
        p
        for p in data
        if p.get("financialData", {}).get("requirements", {}).get("breakdown")
    ]
    Req = pd.json_normalize(
        requirements,
        meta=["planId"],
        max_level=3,
        record_path=["financialData", "requirements", "breakdown", "byGlobalCluster"],
    )
    Req = Req[Req.globalClusterId == globalClusterId]
    print("Working on funding data")
    funded = pd.json_normalize(
        data,
        meta=["planId"],
        max_level=3,
        record_path=["financialData", "funding", "breakdown", "byGlobalCluster"],
    )
    funded = funded[funded["globalClusterId"] == globalClusterId]
    fundedData = Req.merge(funded, how="outer", on="planId")

    df = df.merge(fundedData, how="outer", on="planId")
    df.fillna(0, inplace=True)

    df = df.merge(plans, on="planId", how="left")
    df = df[
        [
            "planId",
            "planYear",
            "Country",
            "iso3",
            "name",
            "planType",
            "isReleased",
            "planCostingType",
            "inNeed",
            "target",
            "cumulativeReach",
            "requirements",
            "funding",
            "cashTransferFunding",
        ]
    ]
    print("All done!")
    return df



def getGlobalClusterInfoByCode(globalClusterCode):
    url = "https://api.hpc.tools/v1/public/global-cluster"
    try:
        resp = requests.get(url).json()['data']
    
    except requests.exceptions.ConnectionError as errt:
        print("The connection was not successfull", errt)
        return
    
    
    try:
        code = next((item['code'] for item in resp if item['id'] == globalClusterCode), None)
        nomcluster = next((item['name'] for item in resp if item['id'] == globalClusterCode), None)

        assert code is not None and nomcluster is not None, "The enterred Global cluster code is inccorrect"

    except AssertionError as e:
        print("An error occured! ", e)
        return
    

    return code, nomcluster