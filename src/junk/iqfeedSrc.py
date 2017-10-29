import datetime
import socket
import os.path
import pandas as pd


def download_symbol(self, symbol):
    
        # Construct the message needed by IQFeed to retrieve data
        #[bars in seconds],[beginning date: CCYYMMDD HHmmSS],[ending date: CCYYMMDD HHmmSS],[empty],[beginning time filter: HHmmSS],[ending time filter: HHmmSS],[old or new: 0 or 1],[empty],[queue data points per second]
        #message = "HIT,%s,%i,%s,%s,,093000,160000,1\n" % symbol, self.timeFrame, self.startDate, self.endDate
        #message = message = "HIT,%s,%s,20150101 075000,,,093000,160000,1\n" % symbol, self.timeFrame
    
        fileName = "{0}{1}-{2}-{3}-{4}.csv".format(
                self.downloadDir, symbol, self.timeFrame, 
                self.startDate, self.endDate)
        exists = os.path.isfile(fileName)
        
        if exists == False:       
            
            #          HIT,NASDAQ,'30',
            message = "HIT,{0},'{1}',{2},{3},,093000,160000,1\n".format(
                    symbol, self.timeFrame, self.startDate, self.endDate)
        
            # Open a streaming socket to the IQFeed server locally
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((self.host, self.port))
            
            sock.sendall(message)
            data = self.read_historical_data_socket(sock)
            sock.close
            
            # Remove all the endlines and line-ending
            # comma delimiter from each record
            data = "".join(data.split("\r"))
            data = data.replace(",\n","\n")[:-1]
    
            # Write the data stream to disk
            
            f = open(fileName, "w")
            f.write(data)
            f.close()
            
        return pd.io.parsers.read_csv(
                fileName, header=0, index_col=0, 
                names=['datetime','open','low','high','close','volume','oi'], 
                parse_dates=True)-*- coding: utf-8 -*-

