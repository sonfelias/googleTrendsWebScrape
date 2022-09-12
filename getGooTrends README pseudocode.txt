1st approach

I was able to create a program like this for this requirement before in
c#.net winforms by using webbrowser control.
The idea is to to access the url in a webbrowser control
url 'https://trends.google.com/trends/explore?date=2015-01-01%202022-09-12&geo=US&q=bitcoin'
then load page in a webbrowser control.
Once page is loaded then you can manipulate html DOM elements objects
inside webbrowser control.

but i'm not going to do it like that since requirement is a script and
not an executable

===================================================================

2nd approach
use python web scraping

pseudocode
1) access url 'https://trends.google.com/trends/explore?date=2015-01-01%202022-09-12&geo=US&q=bitcoin'
you can edit the date querystring upon your requirements

2) get all html contents
3) get <table> element, and get all <tr>'s under the <table> element
4) loop thru the <tr> collection and strip Month and BitCoin data
5) add Month and BitCoin in a temp array
6) if looping is done, then dump the temp array data to a csv file

this is working, but the html document i'm getting
does not have the data from the ajax calls, 
so when I get the response html document from server, the data from ajax calls is not loaded
so I was not able to get the <table> element and get the <tr><td> data

filename for this approach is in getData.py

this took me some time like 3 hrs, as I am trying
all possible means to wait for the ajax calls to load their data
before manipulating the html elements but they are not loading.

i tried also using phantomjs to wait for the ajax calls
and get the complete html documents element page but
was not getting the complete html documents
so I abandon this approach

this approach is feasible for static pages
means if you have the html elements saved in the page itself
and does not require any javascript ajax calls to load data

===================================================================

3nd approach
use Phyton and PyTrends

this approach is much simpler
Google has scraper like api by using PyTrends

filename for this approach is, getGooTrends.py

to execute this 
1) if pytrends is not installed, pls install pytrends in your vscode terminal
	pip install pytrends
2) open getGooTrends.py
3) execute the file by 
	python getGooTrends.py
4) get the result file named getGooTrends_output.csv


this took me only 1 hour to do
this is the approach that I choose

===================================================================



