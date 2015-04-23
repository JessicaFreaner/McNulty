"""test to connect to TestStress"""
import pymysql
import pandas.io.sql as psql

user = 'root'
passwd = 'my0c3@n'
host = '104.236.209.73'


def connect():
    """Function to connect to the database"""

    db = pymysql.connect(host=host,
                         user=user,
                         passwd=passwd,
                         db='stress_test')
    return db


def import_df(sql_table):
    """Import dataframe from MySql, returns a pandas dataframe"""

    db = connect()
    sql = "SELECT * FROM %s" % sql_table
    df = psql.read_sql(sql, db)
    db.close()

    return df


if __name__ == '__main__':

    df = import_df('all_hospitals')
    print 'Type of the dataframe', type(df)
    print 'Length of the dataframe:', len(df)

