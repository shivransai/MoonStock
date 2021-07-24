# MoonStock
##Goal
Gather and display top 15 stocks listed in NYSE (2400) and NASDAQ (3300) that have the highest percent-change for the current day. 

##Development Plan
###Overall 
Host all data on AWS and use Github for version controlling. 

###Backend 
Build csv file of all stocks listed in NYSE and NASDAQ 
Feed csv file to Yfinance API 
Derive open and close for each ticker everyday at 11am and 3:30pm
Calculate % change on all stocks based on Open and Close 
Aggregate 15 top performing stocks 

###Frontend
Display 15 stocks on a HTML page
Use Twitter Bootstrap and CSS formatting to improve aesthetics 


Run "python main.py"

Must have python >3.0
