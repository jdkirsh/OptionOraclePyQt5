import pandas as pd
from sqlalchemy import create_engine

# engine=create_engine

# from pandasql import *
import sqlite3
DATABASE = (r'C:\FINANCE\Python\pyCharm\Projects\OptionOraclePyQt5\database\MyDB.db3')

# ALCH_DATABASE = (r"sqlite:///C:\\FINANCE\\Python\\Projects\\OptionOraclePyQt5\\database\\MyDB.db3")

import pandas as pd

def dictToDot(DictVar):
    if isinstance(DictVar, dict):
        from types import SimpleNamespace
        NS = SimpleNamespace(**DictVar)
        return NS
    else:
        print("Error on dictToDot!!!")

# funtion for SQL on DataFrame
# def pysqldf(q):
#     return sqldf(q, globals())

# from pandasql import sqldf, load_meat, load_births
# pysqldf = lambda q: sqldf(q, globals())
# meat = load_meat()
#
# print (pysqldf("SELECT * FROM meat ;"))
#
# data = pd.read_csv("SPYtoDF1.csv")

# def dataSelect(dataIn, callSw, putSw):
def get_TableSql(SqlName):
    db = sqlite3.connect(DATABASE)
    TableFrame = pd.read_sql(SqlName, db)
    db.close()
    return TableFrame

def loadUnderlying():
    # db = sqlite3.connect(DATABASE)
    loadTableExp = "SELECT * FROM underlying"
    retFrame = get_TableSql(loadTableExp)
    # retFrame= pd.read_sql_table()
    # db.close()
    return retFrame


def dataSelect(*,callSw, putSw):
    # engine = sqlite3.connect(r'C:\FINANCE\Python\pyCharm\Projects\PyQt5 Tutorials\database\MyDB.db3')
    qFrame = pd.DataFrame     # return frame from query
    rFrame = pd.DataFrame     # frame returned from function
    # tableFrame = dataIn
    # tableFrame = pd.read_csv("SPYtoDF1.csv")
    # engine.execute("SELECT * FROM options").fetchall()
    if callSw and not putSw:
        # getCallExp = '''SELECT * FROM tableFrame WHERE Type ='Call';'''
        getCallExp = "SELECT * FROM options WHERE Type = 'Call'"
        # rFrame = engine.execute(getCallExp).fetchall()
        qFrame = get_TableSql(getCallExp)
        # rFrame = rFrame.append(qFrame)
    elif putSw and not callSw:
            # getPutExp = '''SELECT * FROM tableFrame WHERE Type ='Put' ;'''
            getPutExp = "SELECT * FROM options WHERE Type = 'Put'"
            # rFrame = engine.execute(getPutExp).fetchall()
            qFrame = get_TableSql(getPutExp)
            # rFrame = rFrame.append(qFrame)
    else:
        getAllExp = "SELECT * FROM options"
        # rFrame = engine.execute(getPutExp).fetchall()
        qFrame = get_TableSql(getAllExp)
        # rFrame = rFrame.append(qFrame)
    return qFrame


def main():
    # try:
    #     dataIn = pd.read_csv("SPYtoDF1.csv")
    # except IOError as err:
    #     print("read csv I/O error: {0}".format(err))
    import os
    print ("cwd =", os.getcwd() )
    # retFrame = dataSelect(dataIn, True, True)
    # tableFrame = pd.read_csv("SPYtoDF1.csv")
    # engine = sqlite3.connect('MyDB.db3')
    # tableFrame.to_sql(name='tableFrame', con=engine, if_exists='replace')
    # print (engine.execute("SELECT * FROM options").fetchall() )
    # retFrame = dataSelect(True, True)
    # retFrame = pd.DataFrame
    # engine = sqlite3.connect('MyDB.db3')
    # retFrame = pd.read_sql_table('twBottom', engine)
    # retFrame = dataSelect(callSw=True,putSw=True)
    retFrame = loadUnderlying()
    print (retFrame)
    jkDict = retFrame.set_index('attribute').T.to_dict('list')
    jkns = dictToDot(jkDict)
    print(retFrame)
    # df.loc[df['column_name'] == some_value]
    # filtered_df = df.query('X>1')
    # df.set_index('ID').T.to_dict('list')
    # print (retFrame)

    # >> > from types import SimpleNamespace
    # >> > d = {'key1': 'value1', 'key2': 'value2'}
    # >> > n = SimpleNamespace(**d)
    # >> > print(n)
    # namespace(key1='value1', key2='value2')
    # >> > n.key2
    # 'value2'


if __name__ == "__main__":
    main()
