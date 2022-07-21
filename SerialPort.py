#Use module serial
import serial

#Use module pyais sub IterMessages
from pyais import IterMessages

#Undecoded data discription
ser = serial.Serial('COM3', 9600)
data = ser.readline()

#Loop decode data
for data in ser:

    for msg in IterMessages(data):
        print(msg.decode())



