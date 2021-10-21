from data_loader import *
import time
import os
import random
from google_speech import Speech
from playsound import playsound
import threading
from recorder import *
import pyttsx3


# say "Hello World"
topic80 = load_data()
lang = "en"
prep = "Please prepare your answer after the beep."
start_speaking = "Please speaking after the beap."
Speech_prep = Speech(prep, lang)
Speech_start = Speech(start_speaking, lang)

while True:
    current_topic = random.choice(topic80)
    print(current_topic)
    engine = pyttsx3.init()
    engine.setProperty("rate", 200)
    engine.say(current_topic)
    engine.say(prep)
    engine.runAndWait()
    playsound("beep.m4a")
    countdown(15)
    engine.say(start_speaking)
    engine.runAndWait()
    playsound("beep.m4a")
    t = threading.Thread(target=recorder, args=[45, current_topic])
    t.start()
    countdown(45)
    # 等待 t 這個子執行緒結束
    t.join()
    os.system("clear")
