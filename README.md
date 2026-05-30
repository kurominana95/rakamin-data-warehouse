# Banking Transaction Data Warehouse using Python ETL and SQL Server

## Project Overview

This project aims to design and implement a **Banking Transaction Data Warehouse** using an **ETL (Extract, Transform, Load) process** with **Python** and **Microsoft SQL Server**. The system integrates banking-related data from multiple sources, including SQL databases, CSV files, and Excel files into a centralized data warehouse for transaction analysis and reporting.

The project applies data transformation, data cleaning, duplicate handling, and stored procedures to support analytical queries on customer accounts and transaction activities.

---

## Objectives

The objectives of this project are:

* Build a centralized **banking transaction data warehouse**
* Implement an **ETL pipeline** using Python
* Integrate data from multiple data sources
* Perform data cleaning and transformation
* Remove duplicate transaction records
* Support business analysis using **Stored Procedures**

---

## Tech Stack

### Programming Language

* Python

### Libraries

* pandas
* pyodbc

### Database

* Microsoft SQL Server
* SQL Server Management Studio (SSMS)

### Development Environment

* Visual Studio Code (VS Code)

---

## Data Sources

This project integrates data from multiple sources:

| Source                    | Format              |
| ------------------------- | ------------------- |
| Customer, Account, Branch | SQL Server Database |
| Transactions              | SQL Server Table    |
| Transactions              | CSV File            |
| Transactions              | Excel File          |

---

## Data Warehouse Schema

The data warehouse adopts a **star-schema design** with one fact table and several dimension tables.

### Dimension Tables

#### 1. DimCustomer

Contains customer-related information.

Columns:

* CustomerID
* CustomerName
* Address
* CityName
* StateName
* Age
* Gender
* Email

#### 2. DimAccount

Contains account information.

Columns:

* AccountID
* CustomerID
* AccountType
* Balance
* DateOpened
* Status

#### 3. DimBranch

Contains branch information.

Columns:

* BranchID
* BranchName
* BranchLocation

### Fact Table

#### FactTransaction

Contains customer transaction records.

Columns:

* TransactionID
* AccountID
* TransactionDate
* Amount
* TransactionType
* BranchID

---

## Table Relationships

The database follows the following relationships:

<img width="622" height="287" alt="ERD baru (1)" src="https://github.com/user-attachments/assets/993d5271-0ff5-4bee-9c31-7af01d29de15" />

---

## ETL Process

### Extract

Data is extracted from:

* SQL Server database
* CSV files
* Excel files

### Transform

Several transformations are applied:

* Standardizing column names
* Converting transaction date to datetime format
* Data type conversion
* Duplicate transaction removal
* Customer information standardization

### Load

The transformed data is loaded into:

* DimCustomer
* DimAccount
* DimBranch
* FactTransaction

inside the **DWH database**.

---

## Duplicate Handling

Transaction data from multiple sources may contain duplicate records. Duplicate transactions are removed using Python before loading into the fact table.

Example implementation:

```python
df_fact_clean = df_fact.drop_duplicates(
    subset=["TransactionID"]
)
```

---

## Stored Procedures

Several stored procedures are implemented to support business reporting and analysis.

### Daily Transaction Summary

Displays daily transaction statistics based on a selected date range.

Output:

* Transaction Date
* Total Transactions
* Total Amount

### Customer Current Balance

Displays customer account information and calculated current balance.

Current balance is calculated as:

* **Deposit → Added to balance**
* **Other transaction types → Deducted from balance**

Only **active accounts** are included.

---

## Project Structure

```text
project-folder/
│── etl_dimcustomer.py
│── etl_dimaccount.py
│── etl_dimbranch.py
│── etl_facttransaction.py
│── transaction_csv.csv
│── transaction_excel.xlsx
│── README.md
```

---

## How to Run

### 1. Install dependencies

```bash
pip install pandas pyodbc
```

### 2. Configure SQL Server

Ensure SQL Server is running and the following databases exist:

* `sample`
* `DWH`

### 3. Run ETL scripts

```bash
python etl_dimcustomer1.py
python etl_dimbranch.py
python etl_dimaccount.py
python etl_facttransaction.py
```

### 4. Execute Stored Procedures

Run stored procedures in **SQL Server Management Studio (SSMS)**.

---

## Key Features

* Multi-source ETL pipeline
* SQL Server integration
* Data warehouse implementation
* Duplicate transaction handling
* Automated data transformation
* Business reporting with stored procedures

---

## Author

**Najwa Khoir Aldawiyah**
Statistics Graduate | Data Analytics | Data Engineering 
