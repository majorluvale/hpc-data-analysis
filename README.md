#HPC Plan Data Extraction
Overview

This project provides a simple way to extract Humanitarian Programme Cycle (HPC) plan data using a Python function. It allows users to retrieve structured plan-level information for a given year and global cluster.

The core functionality is implemented in hpc_data.py, while a Jupyter notebook is provided for testing and exploration.

Project Structure

hpc_data.py
Contains the main function getPlanData used to fetch and structure HPC data.

hpc_analysis_notebook.ipynb
A Jupyter notebook used to test the function and explore the returned data.

Requirements

Install dependencies using:

pip install -r requirements.txt

Or manually:

pip install requests numpy pandas openpyxl matplotlib seaborn plotly nbformat>=4.2.0
Usage
from hpc_data import getPlanData

PLAN_YEAR = 2025
GLOBAL_CLUSTER_ID = 13  # Example: GBV

df = getPlanData(PLAN_YEAR, GLOBAL_CLUSTER_ID)
df.head()
Parameters

PLAN_YEAR: Year of the HPC plan (e.g., 2025)

GLOBAL_CLUSTER_ID: Global cluster identifier (see table below)

Global Cluster IDs
Global Cluster Id	Name	Code	Type
1	Camp Coordination / Management	CCM	global
2	Early Recovery	ERY	global
3	Education	EDU	global
4	Emergency Shelter and NFI	SHL	global
5	Emergency Telecommunications	TEL	global
6	Food Security	FSC	global
7	Health	HEA	global
8	Logistics	LOG	global
9	Nutrition	NUT	global
10	Protection	PRO	global
11	Water Sanitation Hygiene	WSH	global
12	Protection - Child Protection	PRO-CPN	aor
13	Protection - Gender-Based Violence	PRO-GBV	aor
14	Protection - Housing, Land and Property	PRO-HLP	aor
15	Protection - Mine Action	PRO-MIN	aor
16	Multipurpose Cash	MPC	global
26479	Multi-sector	MS	custom
26480	Coordination and support services	CSS	custom
26481	Other	OTH	custom
26512	Agriculture	AGR	custom
26513	COVID-19	COV19	custom
26546	Protection - Human Trafficking & Smuggling	PRO-HTS	aor
Function Description
getPlanData(year, globalClusterId)

Fetches plan-level HPC data for a given year and global cluster.

Inputs

year (int): Plan year

globalClusterId (int): Global cluster ID

Output

Returns a pandas DataFrame containing plan-level information

Example columns

planId

planYear

countryName

countryISO3

planName

planType

isReleased

peopleInNeed

peopleTargeted

cumulativeReach

requirements

funding

Notebook Usage

The notebook hpc_analysis_notebook.ipynb can be used to:

Test the getPlanData function

Explore and visualize the data

Perform quick analysis

Notes

Data is retrieved from the HPC public API

Availability depends on the selected year and cluster

Output is structured for direct use in analysis workflows
