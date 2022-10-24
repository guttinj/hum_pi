
import Adafruit_DHT
import datetime, csv, time, os, sys, pathlib
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
# from PyQt5.QtGui import QIcon
# from PyQt5 import QtGui, QtCore
# import threading

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

        if len(hum_list) < 600: 

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


















































#sensor = threading.Thread(target=sense_forever(humidity, temp))
#sensor.daemon = True
#sensor.start()
        
# hum_list, temp_list = sense_forever(humidity, temp)

# def get_avg(hum_list, temp_list):
#     hum_avg = sum(hum_list) / len(hum_list)
#     temp_avg = sum(temp_list) / len(temp_list)
#     date = str(datetime.datetime.now())
#     return(hum_avg, temp_avg, date)

# hum_avg, temp_avg, cur_time = get_avg(hum_list, temp_list)

# def export_csv(n, hum_avg, temp_avg, cur_time):

#     final_data = [hum_avg, temp_avg, cur_time]
#     file_name = "Jar" + n + ".csv"

#     if os.path.exists(file_name):

#         chosen_file = open(file_name, 'a')
#         open_file = csv.writer(chosen_file)
#         open_file.writerow(final_data)
#         print("File write complete")

#     else:
#         def exit_program():
#             print("No file has been created. Closing the program.")

#         #def create_csv():
           
#             #with open(file_name, 'w') as csvfile:
#                 #new_file = csv.writer(csvfile)
#                 #new_file.writerow(['Humidity ', ' Temp ', ' Date and Time'])
#                 #new_file.writerow(final_data)
#                 #print(file_name + " has been created and is ready for use.")
      
#         app = QApplication(sys.argv)
#         widget = QWidget()

#         button1 = QPushButton(widget)
#         button1.setText('Yes')
#         button1.move(64, 32)
#         button1.clicked.connect(create_csv)
#         button1.clicked.connect(QtCore.QCoreApplication.instance().quit)

#         button2 = QPushButton(widget)
#         button2.setText('No')
#         button2.move(192, 32)
#         button2.clicked.connect(exit_program)
#         button2.clicked.connect(QtCore.QCoreApplication.instance().quit)

#         widget.setGeometry(50,50,320,200)
#         widget.setWindowTitle("Selected file does not currently exist. Would you like to create new file Jar" + n + ".csv?")
#         widget.show()
#         sys.exit(app.exec_())

#         #create_file = input("Selected file does not currently exist. Would you like to create new file Jar" + n + ".csv?: Y or N ")

# export_csv(n, hum_avg, temp_avg, cur_time)


