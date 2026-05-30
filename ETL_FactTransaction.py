import pyodbc
import pandas as pd

source = pyodbc.connect(
        "DRIVER={SQL Server};"
        "SERVER=LAPTOP-NJJ3I0H1\\SQL2025;"
        "DATABASE=sample;"
        "Trusted_Connection=yes;"
    )

queries = """SELECT transaction_id as TransactionID,
account_id as AccountID,transaction_date as TransactionDate,amount as Amount,transaction_type as TransactionType,
branch_id as BranchID
FROM transaction_db
"""
df_db = pd.read_sql(queries, source)
print(df_db.head)

df_csv = pd.read_csv("transaction_csv.csv")
df_csv.columns = [
    "TransactionID",
    "AccountID",
    "TransactionDate",
    "Amount",
    "TransactionType",
    "BranchID"
]
print(df_csv.head)
df_csv["TransactionDate"] = pd.to_datetime(
    df_csv["TransactionDate"],
    errors="coerce"
)

df_xlsx = pd.read_excel("transaction_excel.xlsx")
df_xlsx.columns = [
    "TransactionID",
    "AccountID",
    "TransactionDate",
    "Amount",
    "TransactionType",
    "BranchID"
]
print(df_xlsx.head)
df_xlsx["TransactionDate"] = pd.to_datetime(
    df_xlsx["TransactionDate"],
    errors="coerce"
)

df_fact = pd.concat(
    [df_db, df_csv, df_xlsx],
    ignore_index=True
)

df_fact_clean = df_fact.drop_duplicates(
    subset=["TransactionID"]
)
print(f"{len(df_fact)-len(df_fact_clean)} row(s) of duplicate removed")

print(df_fact_clean)

destination = pyodbc.connect(
    "DRIVER={SQL Server};" 
    "SERVER=LAPTOP-NJJ3I0H1\\SQL2025;" 
    "DATABASE=DWH;" 
    "Trusted_Connection=yes;" ) 

cursor = destination.cursor() 

for _, row in df_fact_clean.iterrows(): 
    cursor.execute(""" INSERT INTO FactTransaction 
                   (TransactionID, 
                   AccountID, 
                   TransactionDate, 
                   Amount, TransactionType, BranchID) 
                   VALUES (?, ?, ?, ?, ?, ?) """, 
                   
                   row["TransactionID"], 
                   row["AccountID"], 
                   row["TransactionDate"], 
                   row["Amount"], 
                   row["TransactionType"], 
                   row["BranchID"] ) 
    
destination.commit() 
print("FactTransaction loaded successfully!")