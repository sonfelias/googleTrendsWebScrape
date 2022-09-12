from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv


url = 'http://trends.google.com/trends/'
url_date = 'explore?date=2015-01-01%202022-09-12'
url_end = '&geo=US&q=bitcoin'
url = url + url_date + url_end

headers = {'User-agent': 'your bot 0.1'}
r=requests.get(url, headers=headers)
htmlContent = BeautifulSoup(r.content, 'html.parser') 

tableDataToCollect=[]

meRow = {'Month','bitcoin: (United States)'} 

#loop thru <tr> and collect data for csv output
for myRow in htmlContent.findAll('tr'):
    rowData = myRow.find('td')
    mnth = rowData.get_text().strip()
    bitc = rowData.get_text().strip()    

    meRow['month']=mnth
    meRow['bitcoin']=bitc    
    tableDataToCollect.append(meRow)

#output to csv
fileToCSV=pd.DataFrame(tableDataToCollect)
fileToCSV.to_csv('output.csv', encoding='utf-8', index=False)