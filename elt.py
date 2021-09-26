import configparser
import pyodbc
from sql_queries import alter_table_queries


def alter_tables(cnxn, cursor):
    """Alters tables in pension database by running all alter table queries
    defined in sql_queries.py
    :param cursor: cursor to the database
    :param cnxn: database connection reference
    """
    for query in alter_table_queries:
        cursor.execute(query)
        cnxn.commit()


def main():
    """
    Driver main function.
    """
    # Read 'db.cfg' files
    config = configparser.ConfigParser()
    config.read('db.cfg')

    server = config.get("PARAM", "server")
    database = config.get("PARAM", "database")
    username = config.get("PARAM", "username")
    password = config.get("PARAM", "password")

    try:
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        cursor = cnxn.cursor()
        cnxn.set_session(autocommit=True)
    except Exception as e:
        print(e)

    try:
        alter_tables(cnxn, cursor)
        print("Table altered successfully!")
    except Exception as e:
        print(e)

    # close connection and cursor
    cursor.close()
    cnxn.close()


if __name__ == "__main__":
    main()
