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



