import csv
import pandas as pd


# Read the Tables and Columns - SQL Server spreadsheet
with open('Tables and Columns - SQL Server.csv', 'r') as f:
    csvreader = csv.reader(f, delimiter=',')
    next(csvreader) #Skip first row

    # create a dictionary whose keys are the table names and values are tuples of column, datatype and alter sql
    dict = {}

    # Iterate through csv file and append keys and values into the dictionar
    for line in csvreader:
        key = line[1]
        value1 = line[2]
        value2 = line[5]
        value3 = line[6]

        if key in dict:
            dict[key].append((value1, value2, value3))
        else:
            dict[key]= [(value1, value2, value3)]


# Creates a list of Create table queries for all tables
create_table_queries = []

# Iterate through the dictionary
for key, value in dict.items():
    query = """Create table if not exists [{}](""".format(key.replace(".", "].["))
    for column_name, data_type, alter_sql in value:
        query2 ="""{}  {}, """.format(column_name, data_type)
        query += query2
    query += ")"
    query = query.replace(", )", ");")
    #print(query)
    create_table_queries.append(query)


# Creates a list of Alter table queries for all tables
alter_table_queries = []

# Iterate through the dictionary
for key, value in dict.items():
    for column_name, data_type, alter_sql in value:
        query ="""{}""".format(alter_sql)
        alter_table_queries.append(query)


# SQL queries to create tables for pension database
DCPlanData_table = """CREATE TABLE IF NOT EXISTS [pension].[DCPlanData](
actives                 nvarchar,
assets                  nvarchar,
cashbalance             nvarchar,
conts_ee                nvarchar,
conts_er                nvarchar,
coveredpayroll          nvarchar,
dcplanid                nvarchar,
ee_contrate_mandatory   nvarchar,
ee_contrate_max         nvarchar,
ee_contrate_verbatim    nvarchar,
eligible_eegroups       nvarchar,
eq_avg                  nvarchar,
er_contrate_fixedrate   nvarchar,
er_contrate_matchrate   nvarchar,
er_contrate_verbatim    nvarchar,
fy                      nvarchar,
hybrid                  nvarchar,
inactives               nvarchar,
investmentoptions       nvarchar,
mandatory_default       nvarchar,
members                 nvarchar,
planname                nvarchar,
planname_db             nvarchar,
ppd_id                  nvarchar,
primary                 nvarchar,
state                   nvarchar,
year_est                nvarchar
)"""

ActuarialCosts_table = """CREATE TABLE IF NOT EXISTS [pension].[ActuarialCosts](
ActValDate_ActuarialCosts  nvarchar,
ContributionFY             nvarchar,
EEGroupID                  nvarchar,
fy                         nvarchar,
NormCostAmount_EE          nvarchar,
NormCostAmount_ER          nvarchar,
NormCostAmount_tot         nvarchar,
NormCostRate_EE            nvarchar,
NormCostRate_EE_est        nvarchar,
NormCostRate_ER            nvarchar,
NormCostRate_ER_est        nvarchar,
NormCostRate_tot           nvarchar,
NormCostRate_tot_est       nvarchar,
notes_ActCosts             nvarchar,
PlanName                   nvarchar,
ppd_id                     nvarchar,
ProjectedPayroll           nvarchar,
ReqContAmount_ER           nvarchar,
ReqContAmount_tot          nvarchar,
ReqContRate_ER             nvarchar,
ReqContRate_ER_est         nvarchar,
ReqContRate_tot            nvarchar,
source_ActCosts            nvarchar,
TierID                     nvarchar,
UAALRate                   nvarchar
)"""

# SQL queries to drop tables for pension database
DCPlanData_table_drop = """DROP TABLE IF EXISTS [pension].[DCPlanData]"""
ActuarialCosts_table_drop = """DROP TABLE IF EXISTS [pension].[ActuarialCosts]"""
RetirementSystemBasics_table_drop = """DROP TABLE IF EXISTS [pension].[RetirementSystemBasics]"""
PensionTopStocksTopBonds_table_drop = """DROP TABLE IF EXISTS [pension].[PensionTopStocksTopBonds]"""
PensionInvestmentFees_table_drop = """DROP TABLE IF EXISTS [pension].[PensionInvestmentFees]"""
PensionInterestRateRisk_table_drop = """DROP TABLE IF EXISTS [pension].[PensionInterestRateRisk]"""
PensionCreditRating_table_drop = """DROP TABLE IF EXISTS [pension].[PensionCreditRating]"""
PPDDataLatest_table_drop = """DROP TABLE IF EXISTS [pension].[PPDDataLatest]"""
PFPlan_PPDSupplement_table_drop = """DROP TABLE IF EXISTS [pension].[PFPlan_PPDSupplement]"""
RetirementSystemData_table_drop = """DROP TABLE IF EXISTS [pension].[RetirementSystemData]"""
PensionInvestmentPerformanceDetailed_table_drop = """DROP TABLE IF EXISTS [pension].[PensionInvestmentPerformanceDetailed]"""
StateLocalDisability_PPD_table_drop = """DROP TABLE IF EXISTS [pension].[StateLocalDisability_PPD]"""

# List of create table queries
create_table_queries2 = [DCPlanData_table, ActuarialCosts_table]

# Append queries in create_table_queries2 list to create_table_queries list
for query in create_table_queries2:
    create_table_queries.append(query)

# List of drop table queries
drop_table_queries = [DCPlanData_table_drop, ActuarialCosts_table_drop, RetirementSystemBasics_table_drop, \
                      PensionTopStocksTopBonds_table_drop, PensionInvestmentFees_table_drop, PensionInterestRateRisk_table_drop, \
                      PensionCreditRating_table_drop, PPDDataLatest_table_drop, PFPlan_PPDSupplement_table_drop, \
                      RetirementSystemData, PensionInvestmentPerformanceDetailed, StateLocalDisability_PPD]
