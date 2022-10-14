import Adafruit_DHT
import datetime
import csv
import threading
import time
#Average over 5 min for temp readings to file
# Edit the text string for which text file to 
# Using DHT11
cur_time = datetime.datetime.now()
str_cur_time = str(cur_time)
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


final = [("Temperature", "Humidity", "Time and Date"),(temp_avg, hum_avg, str_cur_time)]

#prints out to csv file
c = open('Jar' + n  + '.csv', 'a')
o = csv.writer(c)


# make functions that return values



def sense_forever():
    while True:
        date = datetime.datetime.now()
        print('reading sensor ' , date) 
        time.sleep(5)

sensor = threading.Thread(target=sense_forever)
sensor.daemon = True
sensor.start()

while True:
    date = datetime.datetime.now()
    print('This part of the program is not blocked by the sensor ' , date)
    time.sleep(1)
