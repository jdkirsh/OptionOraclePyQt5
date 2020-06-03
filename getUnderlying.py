# from yahoo_fin.options import *
import pandas as pd
import sqlite3

DATABASE = (r'C:\FINANCE\Python\pyCharm\Projects\OptionOraclePyQt5\database\MyDB.db3')

from types import SimpleNamespace

from yahoo_fin.stock_info import get_quote_table

ticker = 'AAPL'

tickerDF = get_quote_table(ticker , dict_result = False)

engine = sqlite3.connect(DATABASE)
tickerDF.to_sql(name='quote_table', con=engine, if_exists='replace')

tickerDF_trasposed = tickerDF.transpose()
tickerDF_trasposed.to_sql(name='transposed', con=engine, if_exists='replace')

# print ("pasue")
#
# ns = SimpleNamespace(**tickerDict)
# print ("Volume=",ns.Volume)

'''
  [Symbol] TEXT,
  [LastUpdate] TEXT,
  [LastPrice] TEXT,
  [Change] TEXT,
  [Bid] TEXT,
  [Ask] TEXT,
  [DividendPct] TEXT,
  [ImpPct] TEXT,
  [HistPct] TEXT);
'''