import pyodbc
import pandas as pd

source = pyodbc.connect(
        "DRIVER={SQL Server};"
        "SERVER={SERVER-NAME};"
        "DATABASE=sample;"
        "Trusted_Connection=yes;"
)

queries = """SELECT account_id as AccountID, 
customer_id as CustomerID, 
account_type as AccountType, 
balance as Balance,
date_opened as DateOpened,
status as Status FROM account
"""

df = pd.read_sql(queries, source)
print(df.head)

destination = pyodbc.connect(
        "DRIVER={SQL Server};"
        "SERVER={SERVER-NAME};"
        "DATABASE=DWH;"
        "Trusted_Connection=yes;" 
)

cursor = destination.cursor()

for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO DimAccount
        (AccountID, CustomerID, AccountType, Balance, DateOpened, Status)
        VALUES (?, ?, ?, ?, ?, ?)
    """,
    row["AccountID"],
    row["CustomerID"],
    row["AccountType"],
    row["Balance"],
    row["DateOpened"],
    row["Status"],
    )

destination.commit()

print("DimAccount loaded successfully!")


