#import Adafruit_DHT
import datetime
import csv
# import threading
import time
import os


# sen = Adafruit_DHT.DHT11
# pin_Num = 4
humidity = 0
temp = 0


n = input("Which Jar would you like to measure : ")

def sense_forever(humidity, temp):#get humidity and temperature values
    count = 0
    hum_list = []
    temp_list = []
    while True:
        if count <= 4:


            humidity, temp = Adafruit_DHT.read_retry(sen, pin_Num)
            
            humidity += 5
            temp += 12

            ##print('reading sensor ' , date) 
            time.sleep(1)
            
            hum_list.append(humidity)
            temp_list.append(temp)
            count = count + 1
        else:
            break
    return(hum_list, temp_list)
        

hum_list, temp_list = sense_forever(humidity, temp)

def get_avg(hum_list, temp_list):
    hum_avg = sum(hum_list) / len(hum_list)
    temp_avg = sum(temp_list) / len(temp_list)
    date = str(datetime.datetime.now())
    return(hum_avg, temp_avg, date)

hum_avg, temp_avg, cur_time = get_avg(hum_list, temp_list)

def export_csv(n, hum_avg, temp_avg, cur_time):
    final_data = [hum_avg, temp_avg, cur_time]
    file_name = "Jar" + n + ".csv"
    #chosen_file = open(file_name, 'a')

    if os.path.exists(file_name):
        chosen_file = open(file_name, 'a')
        open_file = csv.writer(chosen_file)
        open_file.writerow(final_data)
        print("File write complete")
    else:
        create_file = input("Selected file does not currently exist. Would you like to create new file Jar" + n + ".csv?: Y or N ")
        
        if create_file == "Y" or create_file == "y":
            with open(file_name, 'w') as csvfile:
                new_file = csv.writer(csvfile)
                new_file.writerow(['Humidity ', ' Temp ', ' Date and Time'])
                new_file.writerow(final_data)
            print(file_name + " has been created and is ready for use.")
        else:
            print("No file was created. Closing the program.")


export_csv(n, hum_avg, temp_avg, cur_time)

