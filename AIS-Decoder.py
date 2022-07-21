########################################################################## Version 1.0
#Use module serial
import serial

#Use module pyais sub IterMessages
from pyais import IterMessages

#Undecoded data discription (Open your device manager and check the serial port COM1,COM2 or COM3)
ser = serial.Serial('COM3', 9600)
data = ser.readline()

#Loop decode data
for data in ser:

    for msg in IterMessages(data):
        print(msg.decode())
        
########################################################################## Version 1.1

import serial
import pandas

#Use module pyais sub IterMessages
from pyais import IterMessages

#Undecoded data discription
ser = serial.Serial('COM3', 9600)
data = ser.readline()

#Loop decode data
for data in ser:

    for msg in IterMessages(data):
        print(msg.decode())
        df = pd.DataFrame(print(msg.decode()))

########################################################################## Version 1.2 

#Use module serial
#Use module datetime
import serial
import datetime
from pymongo import MongoClient

#Use module pyais sub IterMessages
from pyais import IterMessages

#Undecoded data discription
ser = serial.Serial('COM3', 9600)
data = ser.readline()

#Loop decode data
for data in ser:

    for msg in IterMessages(data):
        print(msg.decode())

        x = datetime.datetime.now()
        print(x.strftime("%c"))

        ship_file = open('DecodeData.txt', "a")
        ship_file.writelines("\n") 
        
########################################################################## Version 1.3 
import serial
import datetime
import sys

from pyais import IterMessages

ser = serial.Serial('COM3', 9600)
data = ser.readline()

for data in ser:

    for msg in IterMessages(data):
        x = datetime.datetime.now()
        print(x.strftime("%c"))

        data1 = (msg.decode())
        data2 = (x.strftime("%c"), msg.decode())
        print(data2)
        print(type(data2))

        with open('AIS.txt', 'a', newline='') as f:
            print(data2, file=f)
            f.close()
            
########################################################################## Version 1.4

#Library for serial port reader
import serial

#Library to recode the date
import datetime

#Library for decode messages
from pyais import IterMessages

#Serial port variable
ser = serial.Serial('COM3', 9600)
data = ser.readline()


for data in ser:
    for msg in IterMessages(data):

        x = datetime.datetime.now() 
        print(x.strftime("%c")) 

        data1 = (msg.decode()) 
        data2 = (x.strftime("%c"), msg.decode()) 

        print(data2) 

        with open('AISDataStorage.txt', 'a', newline='') as f: 
            print(data2, file=f) 
            f.close()

