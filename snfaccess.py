from snowflake.connector import connect
from snowflake.core import Root
import pandas as pd
import json

## Read from stored connection parameters in config file
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

## Store snowflake connection parameters from JSON configuration
snowflake_config = config['snowflake']

## Establish connection. The **snowflake_config syntax in the connect function call uses dictionary unpacking to unpack the connection parameters directly, matching them to the corresponding argument names in the function.
conn = connect(**snowflake_config)

## Function to execute a query and return a pandas DataFrame
def execute_query(query):
    cur = conn.cursor()
    try:
        cur.execute(query)
        df = pd.DataFrame(cur.fetchall(), columns=[col[0] for col in cur.description])
        return df
    finally:
        cur.close()

queries = {
    "grants_to_roles": "SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.GRANTS_TO_ROLES",
    "grants_to_users": "SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.GRANTS_TO_USERS",
    "warehouse_events_history": "SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.WAREHOUSE_EVENTS_HISTORY",
    "object_privileges": "SELECT * FROM DB_ONE.INFORMATION_SCHEMA.OBJECT_PRIVILEGES"
}

## Execute queries and write each to separate worksheets in Excel
with pd.ExcelWriter('snowflake_data.xlsx', engine='openpyxl') as writer:
    for sheet_name, query in queries.items():
        df = execute_query(query)
        df.to_excel(writer, sheet_name=sheet_name, index=False)

conn.close()

