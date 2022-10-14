import Adafruit_DHT
import datetime
import csv
#Average over 5 min for temp readings to file
# Edit the text string for which text file to 
# Using DHT11
x = datetime.datetime.now()
date = str(x)
rec  = []
sen = Adafruit_DHT.DHT11
pin_Num = 4




n = input("Which Jar would you like to measure : ")


# Gets readings from DHT. Should retry up 15 times
while True:
    h, t = Adafruit_DHT.read_retry(sen, pin_Num)
    h = float()
    t = float()









#Gets averages from Temp(t) and Hum(h)
temp_rec = []
temp_avg = sum(temp_rec)/len(temp_rec)

hum_rec = []
hum_avg = sum(hum_rec)/len(hum_rec)


final = [("Temperature", "Humidity", "Time and Date"),(temp_avg, hum_avg, x)]




Testing here
Trying again
