import serial
import time
from urllib.request import urlopen
arduino = serial.Serial('COM7', 9600, timeout = .1)
while True:
    ch = arduino.readline()[:-1]
    if ch:
        temp = float(ch)
        f = urlopen("https://api.thingspeak.com/update?api_key=5DIKLNWHEL0DHTPG&field6=%s", float(temp))
        print(temp)
        time.sleep(3)

