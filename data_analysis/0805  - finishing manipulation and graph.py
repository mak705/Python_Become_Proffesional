import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from matplotlib.finance import candlestick_ohlc
import matplotlib.dates as mdates
from matplotlib import style

style.use('fivethirtyeight')


def build_ohlc(t,o,h,l,c):
    t = mdates.date2num(t)
    return [t,o,h,l,c]
    

def populate_DB():
    chunks = pd.read_csv('btceUSD.csv', chunksize=400000)
    for chunk in chunks:
        chunk.columns = ['Unix', 'Price', 'Volume']
        with sqlite3.connect('tutorial.db') as conn:
            chunk.to_sql('Bitcoin', conn, if_exists= 'append')

#populate_DB()

def pull_from_DB():
    with sqlite3.connect('tutorial.db') as conn:
        df = pd.read_sql('SELECT * FROM Bitcoin LIMIT 100000', con=conn, index_col="index")

    return df
df = pull_from_DB()
#print(df.head())

df['Date'] = pd.to_datetime(df['Unix'], unit='s')
df.set_index('Date', inplace=True)
del(df['Unix'])
print(df.tail())

ohlc = df['Price'].resample('5D', how='ohlc')

print(ohlc.head())

#ohlc['']

fig = plt.figure()
ax1 = plt.subplot2grid((1,1), (0,0))

ohlc['candlestick_plot'] = list(map(build_ohlc, ohlc.index, ohlc['open'],ohlc['high'],ohlc['low'],ohlc['close']))
ohlc['20MA'] = pd.rolling_mean(ohlc['close'], 20)
ohlc['100MA'] = pd.rolling_mean(ohlc['close'], 100)

print(ohlc.head())

candlestick_ohlc(ax1, ohlc['candlestick_plot'])
ohlc['20MA'].plot(ax=ax1, label = '20MA')
ohlc['100MA'].plot(ax=ax1, label = '100MA')
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
for label in ax1.xaxis.get_ticklabels():
    label.set_rotation(45)

plt.legend(loc=4)

plt.show()


            
            

