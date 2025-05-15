import pywhatkit as kit
import datetime
import time
import pyautogui

def send_measage(contact,text):
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute + 1 # send  after 1 minute
    countryCode = "+92"
    contact = countryCode + contact


    # kit.sendwhatmsg("+923134549651", "Hello! This is a text from Hala's Code", hour, minute)
    # contact = "+923134549651"
    kit.sendwhatmsg_instantly(contact, text, wait_time=30, tab_close=True)

    # send  
    time.sleep(20)
    pyautogui.press("enter")
    print("msg sent")