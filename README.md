# Use of Python to pull data from OCHA HPC API
In this project I will be pulling data from the OCHA HPC API and analyze it using pandas, and graphs using seaborn.

HPC Plan Data Extraction
Overview

This project provides a simple way to extract Humanitarian Programme Cycle (HPC) plan data using a Python function. It allows users to retrieve structured plan-level information for a given year and global cluster.

The core functionality is implemented in hpc_data.py, while a Jupyter notebook is provided for testing and exploration.

Project Structure

hpc_data.py
Contains the main function getPlanData used to fetch and structure HPC data.

hpc_analysis_notebook.ipynb
A Jupyter notebook used to test the function and explore the returned data.

Requirements

Make sure you have the following installed:

Python 3.x

pandas

requests (if used inside your function)

You can install dependencies with:

pip install pandas requests
Usage

Import the function and call it with the desired parameters:

from hpc_data import getPlanData

PLAN_YEAR = 2025
GLOBAL_CLUSTER_ID = 13  # Example: GBV

df = getPlanData(PLAN_YEAR, GLOBAL_CLUSTER_ID)
df.head()
Parameters

PLAN_YEAR
The year of the HPC plan (e.g., 2025)

GLOBAL_CLUSTER_ID
The global cluster identifier
Example:

13 → GBV

14 → Housing, Land and Property (HLP)

Cluster IDs can be retrieved from:
https://api.hpc.tools/v1/public/global-cluster

Function Description
getPlanData(year, globalClusterId)

Fetches plan-level HPC data for a given year and global cluster.

Inputs

year (int): Plan year

globalClusterId (int): Global cluster ID

Output

Returns a pandas DataFrame containing plan-level information

Example columns include:

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

Example Output

The returned dataframe contains structured data per country/plan, including:

General plan metadata (name, type, year)

Geographic information (country name and ISO3)

Key indicators:

People in need

People targeted

Funding requirements and contributions

Notebook Usage

The notebook hpc_analysis_notebook.ipynb can be used to:

Test the getPlanData function

Explore the dataset interactively

Perform quick analysis and validation

Notes

The function relies on the HPC public API

Data availability depends on the selected year and cluster

Results are returned as a pandas DataFrame for easy analysis