import Adafruit_DHT
import datetime, csv, time, os, sys, pathlib
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
# from PyQt5.QtGui import QIcon
# from PyQt5 import QtGui, QtCore
import threading

sen = Adafruit_DHT.DHT11
pin_Num = 4
humidity = 0
temp = 0

n = input("Which Jar would you like to measure : ")

def get_jar_file(): 
    """
    Get jar file name
    """

    file_name = "Jar" + n + ".csv"

    if os.path.exists(file_name) == False:
           
        with open(file_name, 'w') as csvfile:
            new_file = csv.writer(csvfile)
            new_file.writerow(['Humidity ', ' Temp ', ' Date and Time'])
            #new_file.writerow(final_data)
            print(file_name + " has been created and is ready for use.")

    return(file_name)    

jar_file = get_jar_file()

def sense_forever(humidity, temp, jar_file): #get humidity and temperature values

    iteration = 0
    hum_list = []
    temp_list = []

    while True:

        if len(hum_list) < 3600: 

            humidity, temp = Adafruit_DHT.read_retry(sen, pin_Num)

            time.sleep(1)
            
            hum_list.append(humidity)
            temp_list.append(temp)
        else:
            hum_avg = sum(hum_list) / len(hum_list)
            temp_avg = sum(temp_list) / len(temp_list)
            date = str(datetime.datetime.now())
            final_data = [hum_avg, temp, date]

            chosen_file = open(jar_file, 'a')
            open_file = csv.writer(chosen_file)
            open_file.writerow(final_data)
            print("File write complete")
          
            break

    return(hum_avg, temp_avg, date)

while True:
    sense_forever(humidity, temp, jar_file)