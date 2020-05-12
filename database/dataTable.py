import pandas as pd

# from pandasql import *
import sqlite3
DATABASE = (r'C:\FINANCE\MyExamples\PyCharm\Projects\OptionOraclePyQt5\database\MyDB.db3')

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
    retFrame = pd.DataFrame
    retFrame = dataSelect(callSw=True,putSw=True)
    print (retFrame)
    # print (retFrame)


if __name__ == "__main__":
    main()
