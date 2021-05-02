import sys
import numpy as np

import csv

def OutputToCsvFile(numpyArray, OutputFileName):
    np.savetxt(OutputFileName + ".csv" ,numpyArray,fmt="%.0f", delimiter=",")


#-- Read in Training set  -- 
raw_data = np.genfromtxt(sys.argv[1],delimiter=',')  ## train.csv
#print (type(raw_data))
#OutputToCsvFile(raw_data,"raw_data")

data = raw_data[1:,3:]
#print (type(data))
#OutputToCsvFile(data,"data")

where_are_NaNs = np.isnan(data)
data[where_are_NaNs] = 0
#print where_are_NaNs
#OutputToCsvFile(data,"data_NaNs")

#-- Data Format pre-Handle for training data --
month_to_data = {} ## Dictionary ( Key:month , Value:Data)

for month in range(12):
    sample=np.empty(shape = (18 , 480))
    for day in range(20):
        for hour in range(24):
            sample[:,day * 24 + hour] = data [18 * (month * 20 + day): 18 * (month * 20 + day + 1),hour]
    month_to_data[month]=sample
    OutputToCsvFile(sample,"sample_month"+ str(month + 1))