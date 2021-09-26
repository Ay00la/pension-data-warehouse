# Pension Data Modeling
### Project Overview
This purpose of this project is to model data on SQL Server Management Studio(SSMS) and build an ELT pipeline using Python's pandas and pyodbc package. The ELT pipeline transfers data from a set of files within a directory, load data into Database tables and transform it.

### Dataset
Nil

### Environment
* Python 3.6 or above
* SQL Server Management Studio(SSMS)
* Jupyter notebook
* pyodbc - Python package for SQL Server

### Details of the project
In this project the "Tables and Columns - SQL Server" sheet in the Data Master Google Sheet was copied and saved as a CSV file.
The CSV file was then iterated through to Create, Drop tables and also Alter tables in the pension database.

More details of the Data Modeling are in **elt.ipynb** notebook.

### How to run
The ```create_tables.py``` and ```elt.py``` file should be run independently as shown below:
```
python create_tables.py
```
then:
```
python elt.py
```

### Note:
The project is incomplete and still in progress.

### TO DO:
* Downlaod all pension data into a folder.
* Build an ELT pipeline which uses the **COPY** command to bulk insert data into database table.
* Team work/Collaborate with Kacie for documentation of the project.
* Team work/Collaborate with Nillia to probably fetch data using API because I am new to API and how it works.
