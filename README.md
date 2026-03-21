# HPC Plan Data Extraction
## Overview

This project provides a simple way to extract Humanitarian Programme Cycle (HPC) plan data using a Python function. It allows users to retrieve structured plan-level information for a given year and global cluster.

The core functionality is implemented in hpc_data.py, while a Jupyter notebook is provided for testing and exploration.

## Project Structure

* `hpc_data.py`
Contains the main function getPlanData used to fetch and structure HPC data.

* `hpc_analysis_notebook.ipynb`
A Jupyter notebook used to test the function and explore the returned data.

## Requirements

Install dependencies using:

```
pip install -r requirements.txt
```

Or manually:

```
pip install requests numpy pandas openpyxl matplotlib seaborn plotly nbformat>=4.2.0
```

## Usage
```
from hpc_data import getPlanData

PLAN_YEAR = 2025
GLOBAL_CLUSTER_ID = 13  # Example: GBV

df = getPlanData(PLAN_YEAR, GLOBAL_CLUSTER_ID)
df.head()
```
![df.head() screenshot](df_head.png "d.head() screenshot")

It is also possible to fetch data for multiple years and loop through them.
e.g.:

```
YEARS = [2019, 2020, 2021, 2022, 2023, 2024, 2025]
GLOBAL_CLUSTER_ID = 14  # Example: HLP

dataframes = []
for year in YEARS:
    print("Working on", year)
    dataframes.append(getPlanData(year))

df = pd.concat(dataframes)

print("It's done, thank you")
df.head()
```

You can also save the DataFrame in Excel format:

`df.to_excel("planDataHLP2019-2025.xlsx")` will save the dataframe to excel

### Parameters

* ``PLAN_YEAR``: Year of the HPC plan (e.g., 2025)
* ``GLOBAL_CLUSTER_ID``: Global cluster identifier (see table below)

| *Global Cluster Id* | *Name*                                      | *Code* | *Type* |
|:------:|-----------------------------------------------|:--------:|:--------:|
| `1`      | Camp Coordination / Management               | `CCM`    | global   |
| `2`      | Early Recovery                               | `ERY`    | global   |
| `3`      | Education                                    | `EDU`    | global   |
| `4`      | Emergency Shelter and NFI                    | `SHL`    | global   |
| `5`      | Emergency Telecommunications                 | `TEL`    | global   |
| `6`      | Food Security                                | `FSC`    | global   |
| `7`      | Health                                       | `HEA`    | global   |
| `8`      | Logistics                                    | `LOG`    | global   |
| `9`      | Nutrition                                    | `NUT`    | global   |
| `10`     | Protection                                   | `PRO`    | global   |
| `11`    | Water Sanitation Hygiene                     | `WSH`    | global   |
| `12`     | Protection - Child Protection                | `PRO-CPN`| aor      |
| `13`     | Protection - Gender-Based Violence           | `PRO-GBV`| aor      |
| `14`     | Protection - Housing, Land and Property      | `PRO-HLP`| aor      |
| `15`     | Protection - Mine Action                     | `PRO-MIN`| aor      |
| `16`     | Multipurpose Cash                            | `MPC`    | global   |
| `26479`  | Multi-sector                                 | `MS`     | custom   |
| `26480`  | Coordination and support services            | `CSS`    | custom   |
| `26481`  | Other                                        | `OTH`    | custom   |
| `26512`  | Agriculture                                  | `AGR`    | custom   |
| `26513`  | COVID-19                                     | `COV19`  | custom   |
| `26546`  | Protection - Human Trafficking & Smuggling   | `PRO-HTS`| aor      |

## Function Description
`getPlanData(year, globalClusterId)`

Fetches plan-level HPC data for a given year and global cluster.

### Inputs

* `year` * *(int)* *: Plan year

* `globalClusterId` * *(int)* *: Global cluster ID

### Output

* Returns a **pandas DataFrame** containing plan-level information

### Returned columns

* `planId`: * *Plan ID* * 
* `planYear`: * *Plan year, eg.2021* * 
* `countryName`: * *Name of the country, eg. Democratic Republic of Congo* *
* `countryISO3`: * *Country's ISO3 code, eg. COD* * 
* `planName`: * *The name of the plan. eg. Mozambique humanitarian response plan* *
* `planType`: * *Type of plan* *
* `isReleased`: * *Is the plan released? show False is the plan is not released* *
* `peopleInNeed`: * *People in Need, see the IASC definition* *
* `peopleTargeted`: * *People targeted, see the IASC definition* *
* `peopleReached`: * *People reached, see the IASC definition* *
* `requiredFunds`: * *Required funds* *
* `fundedAmount`: * *Funded amount (in USD)* * 
* `cashTransferFunding`: * *Funded amount for cash transfer only* *

### Notebook Usage

The notebook `hpc_analysis_notebook.ipynb` can be used to:
* Test the `getPlanData` function
* Explore and visualize the data
* Perform quick analysis

### Notes

* Data is retrieved from the HPC public API
* Availability depends on the selected year and cluster
* Output is structured for direct use in analysis workflows

### Contact
For questions or further information, reach out via email:

Trésor Major Luvale – majorluvale2012@gmail.com
