
"""
Bitcoin Signals
"""
import numpy as np
import pandas as pd
#Data Source
import yfinance as yf
import os
#Data viz
import plotly.graph_objs as go

# For Notifications
import datetime
import time
from plyer import notification 

import smtplib, ssl

#Email Server Set-UP
smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "XXX"
password = "XXX" 
#input("Type your password and press enter: ")

# Create a secure SSL context
context = ssl.create_default_context()





# Get Bitcoin data
BTCData = yf.download(tickers='BTC-GBP', period = '5d', interval = '1m')
BTCnow = BTCData.iloc[-1,-3]
BTCthen = BTCData.iloc[-1440,3]
BTCNow= round(BTCnow,0)
BTCThen= round(BTCthen,0)
BTCchange = ((BTCNow-BTCThen)/BTCThen)*100
BTCChange= round(BTCchange,2)

# Get Ether data
ETHData = yf.download(tickers='ETH-GBP', period = '5d', interval = '1m')
ETHnow = ETHData.iloc[-1,-3]
ETHthen = ETHData.iloc[-1440,3]
ETHNow= round(ETHnow,0)
ETHThen= round(ETHthen,0)
ETHchange = ((ETHNow-ETHThen)/ETHThen)*100
ETHChange= round(ETHchange,2)

#Notification
#if we fetched data
if not (BTCData.empty):
    #converting data into JSON format
    #data = Data.json()['Success']
    
    #repeating the loop for multiple times
    while(True):
        # Get Bitcoin data
        BTCData = yf.download(tickers='BTC-GBP', period = '5d', interval = '1m')
        BTCnow = BTCData.iloc[-1,-3]
        BTCthen = BTCData.iloc[-1440,3]
        BTCNow= round(BTCnow,0)
        BTCThen= round(BTCthen,0)
        BTCchange = ((BTCNow-BTCThen)/BTCThen)*100
        BTCChange= round(BTCchange,2)

        # Get Ether data
        ETHData = yf.download(tickers='ETH-GBP', period = '5d', interval = '1m')
        ETHnow = ETHData.iloc[-1,-3]
        ETHthen = ETHData.iloc[-1440,3]
        ETHNow= round(ETHnow,0)
        ETHThen= round(ETHthen,0)
        ETHchange = ((ETHNow-ETHThen)/ETHThen)*100
        ETHChange= round(ETHchange,2)
         
        daynum= datetime.datetime.today().weekday()
        #Thursday is #3
        if daynum == 3:
                
                Cmessage = "Current BTC Price : {BTCNowp}\nChange BTC : {BTCChangep}%\nCurrent ETH Price : {ETHNowp}\nChange ETH : {ETHChangep}%".format(
                               BTCNowp = BTCNow,
                               BTCChangep = BTCChange,
                               ETHNowp = ETHNow,
                               ETHChangep = ETHChange)
                
                if os.name == "posix":
                    Title = "Bitcoin Stats"
                    Message = "Current BTC Price : " + str(BTCNow) + "\nChange BTC : " + str(BTCChange) + "%\nCurrent ETH Price : " + str(ETHNow) + "\nChange ETH : " + str(ETHChange) + "%"
        
         
                    def notify(title, text):
                        os.system("""
                                  osascript -e 'display dialog "{}" with title "{}"'
                                  """.format(text, title))
                    notify(Title,Message)
                
                else:   
                    notification.notify(
                        #title of the notification,
                        title = "Crypto Stats on {}".format(datetime.datetime.today()),
                        #the body of the notification
                        message = "Current BTC Price : {BTCNowp}\nChange BTC : {BTCChangep}%\nCurrent ETH Price : {ETHNowp}\nChange ETH : {ETHChangep}%".format(
                                BTCNowp = BTCNow,
                                BTCChangep = BTCChange,
                                ETHNowp = ETHNow,
                                ETHChangep = ETHChange),
                        #": {Now}\n24hr Price : {Then}\nChange :{Change}%" ,
                        #creating icon for the notification
                        #we need to download a icon of ico file format
                        app_icon = r'C:\Users\danhe\Pictures\Paomedia-Small-N-Flat-Bell.ico',
                        # the notification stays for 50sec
                        timeout  = 50  
                        )
                    #Email Details
                sender_email = "xxx"
                receiver_email = "xxx"
                emessage = """Subject: Crypto Stats
                    
                \nCurrent BTC Price - {BTCNowp}\nChange BTC - {BTCChangep}%\nCurrent ETH Price - {ETHNowp}\nChange ETH - {ETHChangep}%""".format(
                             BTCNowp = BTCNow,
                             BTCChangep = BTCChange,
                             ETHNowp = ETHNow,
                             ETHChangep = ETHChange)
                            # Try to log in to server and send email
                try:
                    server = smtplib.SMTP(smtp_server,port)
                    server.ehlo() # Can be omitted
                    server.starttls(context=context) # Secure the connection
                    server.ehlo() # Can be omitted
                    server.login(sender_email, password)
                    #Send Email
                    server.sendmail(sender_email, receiver_email, emessage)
                except Exception as e:
                    # Print any error messages to stdout
                    print(e)
                finally:
                    server.quit() 
                #sleep for 4 hrs => 60*60*4 sec
                #notification repeats after every 4hrs
                time.sleep(60*60*3)
        else:
            if os.name == "posix":
                    Title = "Bitcoin Stats"
                    Message = "Current BTC Price : " + str(BTCNow) + "\nChange BTC : " + str(BTCChange) + "%\nCurrent ETH Price : " + str(ETHNow) + "\nChange ETH : " + str(ETHChange) + "%"
        
         
                    def notify(title, text):
                        os.system("""
                                  osascript -e 'display dialog "{}" with title "{}"'
                                  """.format(text, title))
                    notify(Title,Message)
                        
            else:
                notification.notify(
                    #title of the notification,
                    title = "Crypto Stats on {}".format(datetime.datetime.today()),
                    #the body of the notification
                    message = "Current BTC Price : {BTCNowp}\nChange BTC : {BTCChangep}%\nCurrent ETH Price : {ETHNowp}\nChange ETH : {ETHChangep}%".format(
                                BTCNowp = BTCNow,
                                BTCChangep = BTCChange,
                                ETHNowp = ETHNow,
                                ETHChangep = ETHChange),
                    #": {Now}\n24hr Price : {Then}\nChange :{Change}%" ,
                    #creating icon for the notification
                    #we need to download a icon of ico file format
                    app_icon = r'C:\Users\danhe\Pictures\Paomedia-Small-N-Flat-Bell.ico',
                    # the notification stays for 50sec
                    timeout  = 50  
                    )
                
                #sleep for 4 hrs => 60*60*4 sec
                #notification repeats after every 4hrs
                time.sleep(60*60*1)        
                
    
  
#declare figure
fig = go.Figure()

#Candlestick
fig.add_trace(go.Candlestick(x=BTCData.index,
                open=BTCData['Open'],
                high=BTCData['High'],
                low=BTCData['Low'],
                close=BTCData['Close'], name = 'market data'))

# Add titles
fig.update_layout(
    title='Bitcoin live share price evolution',
    yaxis_title='Bitcoin Price (GBP)')

# X-Axes
fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=15, label="15m", step="minute", stepmode="backward"),
            dict(count=45, label="45m", step="minute", stepmode="backward"),
            dict(count=1, label="HTD", step="hour", stepmode="todate"),
            dict(count=6, label="6h", step="hour", stepmode="backward"),
            dict(step="all")
        ])
    )
)

#Show
#fig.show()