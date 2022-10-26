import sys, os, csv, datetime
import time
from PyQt5.QtWidgets import QPushButton, QMainWindow, QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QObject, QThread, pyqtSignal

""" Initialize Variables"""
pin_Num = 4
humidity = 0
temp = 0

n = input("Which Jar would you like to measure : ")

def get_jar_file(): 
    
        file_name = "Jar" + n + ".csv"

        if os.path.exists(file_name) == False:
           
            with open(file_name, 'w') as csvfile:
                new_file = csv.writer(csvfile)
                new_file.writerow(['Humidity ', ' Temp ', ' Date and Time'])
                print(file_name + " has been created and is ready for use.")

        return(file_name)    

jar_file = get_jar_file()

class Worker(QObject):

    finished = pyqtSignal()  # our signal out to the main thread to alert it we've completed our work

    def __init__(self):
        super(Worker, self).__init__()
        self.working = True  # this is our flag to control our loop

    def work(self, jar_file):
        while self.working:

            hum_list = []
            temp_list = []

            if len(hum_list) < 5: 

                #humidity, temp = Adafruit_DHT.read_retry(sen, pin_Num)
                humidity, temp = 1, 3
                time.sleep(1) #remember to take this out when using the Adafruit
                
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

        self.finished.emit() # alert our gui that the loop stopped
        return(hum_avg, temp_avg, date)
            #print("I'm running")
            #time.sleep(1)
        
class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 800, 600)
        self.setWindowTitle("Program")
        self.setWindowIcon(QIcon('icon.png'))

        self.startbtn = QPushButton("Start", self)
        self.startbtn.resize(self.startbtn.minimumSizeHint())
        self.startbtn.move(100, 100)
        self.stopbtn = QPushButton("Stop", self)
        self.stopbtn.move(100, 200)
        self.stopbtn.resize(self.stopbtn.minimumSizeHint())

        self.thread = None 
        self.worker = None

        self.startbtn.clicked.connect(self.start_loop)  

    def start_loop(self):
        self.thread = QThread()  # a new thread to run our background tasks in
        self.worker = Worker()  # a new worker to perform those tasks
        self.worker.moveToThread(self.thread)  # move the worker into the thread, do this first before connecting the signals
        
        self.thread.started.connect(self.worker.work)  # begin our worker object's loop when the thread starts running
        self.stopbtn.clicked.connect(self.stop_loop)  # stop the loop on the stop button click
        self.worker.finished.connect(self.loop_finished)  # do something in the gui when the worker loop ends
        self.worker.finished.connect(self.thread.quit)  # tell the thread it's time to stop running
        self.worker.finished.connect(self.worker.deleteLater)  # have worker mark itself for deletion
        self.thread.finished.connect(self.thread.deleteLater)  # have thread mark itself for deletion
        # make sure those last two are connected to themselves or you will get random crashes

        self.thread.start()

    def stop_loop(self):
        self.worker.working = False
        # since thread's share the same memory, we read/write to variables of objects running in other threads
        # so when we are ready to stop the loop, just set the working flag to false

    def loop_finished(self):
        # received a callback from the thread that it completed
        print('Looped Finished')

def run():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

# this is good practice as well, it allows your code to be imported without executing
if __name__ == '__main__': # then this script is being run directly, 
    run() 
else: # this script is being imported
    ... # usually you can leave off the else
