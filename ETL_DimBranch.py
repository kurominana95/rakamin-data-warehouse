import pyodbc
import pandas as pd

source = pyodbc.connect(
        "DRIVER={SQL Server};"
        "SERVER=LAPTOP-NJJ3I0H1\\SQL2025;"
        "DATABASE=sample;"
        "Trusted_Connection=yes;"
    )

queries = """SELECT branch_id as BranchID, 
branch_name as BranchName, 
branch_location as BranchLocation FROM branch 
"""

df = pd.read_sql(queries,source)
print(df.head)

destination = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=LAPTOP-NJJ3I0H1\\SQL2025;"
    "DATABASE=DWH;"
    "Trusted_Connection=yes;"
)

cursor = destination.cursor()

for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO DimBranch
        (BranchID, BranchName, BranchLocation)
        VALUES (?, ?, ?)
    """,
    row["BranchID"],
    row["BranchName"],
    row["BranchLocation"]
    )

destination.commit()

print("DimBranch loaded successfully!")

