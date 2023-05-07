#Author - Raghav Atris
#Project Name - Lucifer
#Language Used - Python

import datetime
import random
import psutil
import pywhatkit
import webbrowser
import sys
import cv2
import speedtest
from playsound import playsound
from plyer import notification
import os
import winshell
import pyautogui
from Brain.Brain import ReplyBrain
from Body.Listen import MicExecution
from Body.Speak import Speak
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from LuciferUi import Ui_MainWindow
from pynput.keyboard import Key,Controller
keyboard = Controller()
print(">> Starting The Lucifer : Wait for few Seconds")

def YouTube(term):
    result = "https://www.youtube.com/results?search_query=" + term
    webbrowser.open(result)
    Speak("This is what I found for your query")
    pywhatkit.playonyt(term)

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
    
    def run(self):
        MainExecution(self)

def MainExecution(self): 
    Speak("Hello There, I'm Lucifer. Your Own Virtual Consciousness. How can I be of Your Service?")

    while True:
        self.Data = MicExecution(self)
        self.Data = str(self.Data)
        if len(self.Data)<3:
            pass
        
        elif "time" in self.Data:
            time = datetime.datetime.now().strftime('%I:%M %p')
            Speak(f"It's {time}.")

        elif "date" in self.Data:
            date = datetime.datetime.now().strftime("%b %d %Y")
            Speak(f"It's {date}.")

        elif "news" in self.Data or 'headlines' in self.Data or "buzzing" in self.Data:
            Speak("please wait, fetching the latest news")
            main_url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=506bf612a20742b881438715a5a5173f'
            main_page = requests.get(main_url).json()
            articles = main_page["articles"]
            head = []
            day = ["first", "second", "third", "fourth", "fifth"]
            for ar in articles:
                head.append(ar["title"])
            for i in range(len(day)):
                Speak(f"{head[i]}")

        elif 'weather' in self.Data or "temperature" in self.Data:
                self.Data = self.Data.replace("weather", "")
                self.Data = self.Data.replace("of", "")
                self.Data = self.Data.replace("at", "")
                self.Data = self.Data.replace("of", "")
                self.Data = self.Data.replace("the", "")
                self.Data = self.Data.replace("in", "")
                self.Data = self.Data.replace("city", "")
                self.Data = self.Data.replace("tell", "")
                self.Data = self.Data.replace("me", "")
                self.Data = self.Data.replace("can", "")
                self.Data = self.Data.replace("you", "")
                self.Data = self.Data.replace("today's", "")
                self.Data = self.Data.replace("lucifer", "")

                api_key = "241364c869bf698199af0bb545c3ca03"
                base_url = "http://api.openweathermap.org/data/2.5/weather?"
                city_name = self.Data
                complete_url = base_url + "appid=" + api_key + "&q=" + city_name
                response = requests.get(complete_url)
                x = response.json()
                if x["cod"] != "404":
                    y = x["main"]
                    current_temperature = y["temp"]
                    current_pressure = y["pressure"]
                    current_humidiy = y["humidity"]
                    z = x["weather"]
                    weather_description = z[0]["description"]
                    r = ("In" + city_name + " Temperature is " +
                        str(int(current_temperature - 273.15)) + " degree celsius " +
                        ", atmospheric pressure " + str(current_pressure) + " hpa unit" +
                        ", humidity is " + str(current_humidiy) + " percent"
                                                                " and " + str(weather_description))
                    Speak(r)

        elif "location" in self.Data or "where am I" in self.Data:
                Speak("please wait, let me check")
                try:
                    ipAdd = requests.get('https://api.ipify.org').text
                    url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    city = geo_data['city']
                    country = geo_data['country']
                    Speak(
                        f"I am not sure, but i think you are currently in {city} city of {country} country")
                except Exception as e:
                    Speak(
                        "sorry, due to network issue, i am not able to find where we are. Please try again")
                    pass    

        elif "battery" in self.Data:
                battery = psutil.sensors_battery()
                percentage = battery.percent
                Speak(f"our system have {percentage} percent battery")
                if percentage >= 50:
                    Speak("we have enough power to continue our work")
                elif percentage >= 30 and percentage <= 50:
                    Speak(
                        "we should connect our system to charging point to continue our work")
                elif percentage >= 15 and percentage <= 30:
                    Speak(
                        "we don't have enough power to continue our work, we should connect our system to charging point to continue our work ")
                elif percentage <= 15:
                    Speak(
                        "we are draining, please connect our system to charging point or our system will shutdown soon")

        elif "Camera" in self.Data or "camera" in self.Data:
                Speak(random.choice(
                    ["Sure!, opening camera", "Alright!, opening camera"]))
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(50)
                    if k == 27:
                        break
                cap.release()
                cv2.destroyAllWindows()

        elif "internet speed" in self.Data:
                    Speak("please wait, fetching your internet speed")
                    wifi  = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576       
                    download_net = wifi.download()/1048576
                    Speak(f"Wifi download speed is {download_net} mbp/s")
                    Speak(f"Wifi Upload speed is {upload_net} mbp/s")        
        
        elif 'play' in self.Data or "Play" in self.Data:
            song = self.Data.replace('play', '')
            Speak('playing ' + song)
            pywhatkit.playonyt(song)
        
        elif "note" in self.Data:
            pyautogui.press('win')
            pyautogui.write('notepad')
            pyautogui.sleep(1)
            pyautogui.press('enter')
            Speak("Sure! what should i note?")
            self.Data = MicExecution(self)
            self.Data = str(self.Data)
            try:
                self.Data = self.Data.replace("type", "")
                self.Data = self.Data.replace("write", "")
                self.Data = self.Data.replace("lucifer", "")
                pyautogui.write(self.Data)
            except:
                Speak("Please try again!")

        elif "cpu" in self.Data:
             usage = str(psutil.cpu_percent())
             Speak('CPU usage is at ' + usage)      

        elif "pause" in self.Data or "stop" in self.Data:
            pyautogui.press("k")

        elif "resume" in self.Data:
            pyautogui.press("k")   

        elif "photo" in self.Data or "selfie" in self.Data:
                    pyautogui.press("win")
                    pyautogui.write("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(1)
                    Speak("Say Cheese!")
                    pyautogui.press("enter")
    
        elif "open" in self.Data:
            try:
                self.Data = self.Data.replace("open", "")
                self.Data = self.Data.replace("lucifer", "")
                Speak(random.choice(
                    ["opening..."+self.Data, "Launching..."+self.Data]))
                pyautogui.press('win')
                pyautogui.write(self.Data)
                pyautogui.sleep(1)
                pyautogui.press('enter')
            except:
                Speak("It doesn't look like you have an app like that")        
        
        elif "schedule my day" in self.Data:
                tasks = []
                file = open("DataBase\\tasks.txt","w")
                file.write(f"")
                file.close()
                Speak("Enter the number of tasks, you want to schedule")
                print("")
                no_tasks = int(input("Enter the number of tasks : "))
                print("")
                Speak("Enter the tasks, you want to schedule")
                i = 0
                for i in range(no_tasks):
                    print("")
                    tasks.append(input("Enter the task : "))
                    print("")
                    file = open("DataBase\\tasks.txt","a")
                    file.write(f"{i}. {tasks[i]}\n")
                    file.close()
        
        elif "alarm" in self.Data:
                Speak("Sure!, Please Enter the time!")   
                print("")
                time = input("Enter the time : ")
                while True:
                    Time_Ac = datetime.datetime.now()
                    now = Time_Ac.strftime("%H:%M:%S")
                    
                    if now == time:
                        playsound('Alarm.mp3')
                        hour = int(datetime.datetime.now().hour)
                        if hour >= 0 and hour < 18:
                            Speak("Good Morning")
                            time = datetime.datetime.now().strftime('%I:%M %p')
                            Speak(f"It's {time}.")
                            import requests
                            geo_url = "http://ip-api.com/json"
                            response = requests.get(geo_url)
                            data = response.json()
                            lat = data['lat']
                            lon = data['lon']
                            api_key = "241364c869bf698199af0bb545c3ca03"
                            weather_url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
                            response = requests.get(weather_url)
                            data = response.json()
                            print(f"Location: {data['name']}, {data['sys']['country']}")
                            Speak(f"It's Currently: {data['main']['temp']}°C, And the Weather condition is: {data['weather'][0]['description']}")
                            break   
                        
                        elif hour >= 18 and hour < 24:
                            Speak("Good Evening")
                            time = datetime.datetime.now().strftime('%I:%M %p')
                            Speak(f"It's {time}.")
                            import requests
                            geo_url = "http://ip-api.com/json"
                            response = requests.get(geo_url)
                            data = response.json()
                            lat = data['lat']
                            lon = data['lon']
                            api_key = "241364c869bf698199af0bb545c3ca03"
                            weather_url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
                            response = requests.get(weather_url)
                            data = response.json()
                            print(f"Location: {data['name']}, {data['sys']['country']}")
                            Speak(f"It's Currently: {data['main']['temp']}°C, And the Weather condition is: {data['weather'][0]['description']}")
                            break   
                    
        elif "type" in self.Data or "write" in self.Data:
            try:
                self.Data = self.Data.replace("type", "")
                self.Data = self.Data.replace("lucifer", "")
                self.Data = self.Data.replace("write", "")
                pyautogui.write(self.Data)
            except:
                Speak("Please try again!") 

        elif "show my schedule" in self.Data or "what do i have for today" in self.Data:
            file = open("DataBase\\tasks.txt","r")
            content = file.read()
            file.close()
            notification.notify(
                title = "My schedule",
                message = content,
                app_icon = "Assets\My-Schedule.ico",
                timeout = 15
            )
            
        elif "increase" in self.Data or "turn up" in self.Data:
             Speak("I've turned it up.")
             for i in range(5):
                    keyboard.press(Key.media_volume_up)
                    keyboard.release(Key.media_volume_up)
                    pass

        elif "decrease" in self.Data or "turn down" in self.Data:
            Speak("I've turned it down")
            for i in range(5):
                keyboard.press(Key.media_volume_down)
                keyboard.release(Key.media_volume_down)
                pass

        elif "mute" in self.Data:
              pyautogui.press("volumemute")      
              Speak("I've Muted it")  

        elif "start" in self.Data or "volume" in self.Data or "media control" in self.Data or "gesture based media control" in self.Data:
            Speak("Sure!, Starting media based volume control!")
            os.startfile("Main.py")        

        elif 'switch' in self.Data or 'change' in self.Data:
                Speak(random.choice(["Sure!", "Alright"]))
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                pyautogui.keyUp("alt")

        elif 'minimize' in self.Data:
                Speak(random.choice(["Sure!", "Alright"]))
                pyautogui.keyDown("win")
                pyautogui.press("down")
                pyautogui.keyUp("win")

        elif "maximize" in self.Data:
                Speak(random.choice(["Sure!", "Alright"]))
                pyautogui.keyDown("win")
                pyautogui.press("up")
                pyautogui.keyUp("win") 

        elif 'close' in self.Data:
                Speak(random.choice(
                    ["closing...", "terminating..."]))
                pyautogui.keyDown("alt")
                pyautogui.press("f4")
                pyautogui.keyUp("alt")

        elif 'lock' in self.Data:
                import ctypes
                try:
                    Speak("locking your device")
                    ctypes.windll.user32.LockWorkStation()
                except Exception as e:
                    Speak("window is already locked")

        elif 'empty recycle bin' in self.Data or "clean recycle bin" in self.Data:
                try:
                    winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
                    Speak("Alright, cleaning recycle bin")
                    import time
                    time.sleep(3)
                    Speak("Recycle Bin is cleaned")
                except Exception as e:
                    Speak("Recycle bin is already cleaned") 

        elif "youtube" in self.Data:
            self.Data = self.Data.replace("lucifer","")
            self.Data = self.Data.replace("youtube","")
            self.Data = self.Data.replace("search","")
            YouTube(self.Data)

        elif "where" in self.Data:
            self.Data = self.Data.replace("where", "")
            self.Data = self.Data.replace("is", "")
            self.Data = self.Data.replace("city", "")
            self.Data = self.Data.replace("state", "")
            self.Data = self.Data.replace("country", "")
            self.Data = self.Data.replace("located", "")
            self.Data = self.Data.replace("location", "")
            self.Data = self.Data.replace("tell me","")
            url = 'https://google.nl/maps/place/' + self.Data + '/&amp;'

            webbrowser.open(url)
            Speak(f'location of {self.Data} is on your screen')

        elif "shutdown" in self.Data:
                Speak("okay, please wait, Initializing shutdown protocol")
                os.system("shutdown /s /t 5")

        elif "restart" in self.Data:
                Speak("okay, please wait, restarting your computer")
                os.system("shutdown /r /t 5")

        elif "hibernate" in self.Data:
                Speak("okay, please wait, hibernating your computer")
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        
        elif "goodbye" in self.Data or "bye" in self.Data or "good bye" in self.Data or "offline" in self.Data or "break" in self.Data or "sleep" in self.Data:
                Speak("nice talking to you!")
                hour = int(datetime.datetime.now().hour)
                if hour >= 0 and hour < 18:
                    Speak("Have a Nice day!")
                    sys.exit()
                elif hour >= 18 and hour < 24:
                    Speak("Goodnight, Sweet dreams!")
                    sys.exit()  
        else:
                Reply = ReplyBrain(self.Data)
                Speak(Reply)
                                          
startExecution = MainThread()  

class Main(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("Assets\lucifer.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        startExecution.start()

app = QApplication(sys.argv)
Ui_MainWindow = Main()
Ui_MainWindow.show()
exit(app.exec_())
