from pytrends.request import TrendReq
import pandas as pd
import time

strDateToday = time.strftime("%Y-%m-%d")
strTimeFrame = '2015-01-01 ' + strDateToday

pyt = TrendReq(hl='en-GB', tz=360)

dataset = []

pyt.build_payload(
    kw_list=['bitcoin'],
    cat=0,
    timeframe=strTimeFrame,
    geo='')

data = pyt.interest_over_time()

if not data.empty:
    data = data.drop(labels=['isPartial'],axis='columns')
    dataset.append(data)

res = pd.concat(dataset, axis=1)
res.to_csv('getGooTrends_output.csv')

print('Done please see getGooTrends_output.csv')