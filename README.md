# Snowflake Access Data Query and Export Tool

This tool connects to a Snowflake instance, executes a set of predefined queries, and exports the results to an Excel file, with each query's output in a separate worksheet. I developed this at USAA in support of Information Governance and IAM objectives while designing and managing the IAM architecture. The output of this tool allows you to greatly enrich data from your IdP and other sources to gain actionable insights.  

## Features

- Connects to Snowflake using configurable parameters.
- Executes multiple queries on Snowflake databases.
    - Grants to roles data from the ACCOUNT_USAGE schema in the SNOWFLAKE database.
    - Grants to users data from the ACCOUNT_USAGE schema in the SNOWFLAKE database.
    - Warehouse events history from the ACCOUNT_USAGE schema in the SNOWFLAKE database.
    - Object privileges data from the INFORMATION_SCHEMA of the database you define.
- Exports results to an Excel file with each result set in a separate worksheet.

## Setup

### Prerequisites

- Python 3.x 
- Snowflake account with the necessary permissions
- Python libraries: `snowflake-connector-python`, `pandas`, `openpyxl`
- An assigned role with permissions to query the `SNOWFLAKE` DB and any other DB which you want to query for object privileges

### Known issues

At this time `snowflake-connector-python` is v3.6.0 and only compatible with Python up to version 3.10, with 3.12 support TBD pending [release of v3.7.0](https://github.com/snowflakedb/snowflake-connector-python/blob/main/DESCRIPTION.md). If you attempt to install the connector with Python 3.12 you will encounter errors. 

### Installation

1. Install the required Python libraries:

    ```bash
    pip install snowflake-connector-python pandas openpyxl
    ```
2. Download the repo files and extract to a directory or git clone

3. Modify the `config.json` file in the project directory to replace the values with your actual Snowflake details. For authentication options refer to [python connector API docs](https://docs.snowflake.com/en/developer-guide/python-connector/python-connector-api#functions)

4. In the `object_privileges` query, Replace `DB_one` with the name of the DB you want to query

## Usage

Run the script using Python:

```bash
python snfaccess.py