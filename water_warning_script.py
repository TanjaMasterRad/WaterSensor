from time import sleep
from gpiozero import InputDevice
import RPi.GPIO as GPIO
import urllib.request

 
greenLED = 27
no_rain = InputDevice(18)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(greenLED, GPIO.OUT)
GPIO.output(greenLED ,GPIO.LOW)

TOKEN = '7220140173:AAHIItPKAifaWr936eWPq9g1kfiYb1SXNR4'
CHAT_ID = '5125310957'

def send_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
    req = urllib.request.Request(url, method='PUT')
    response = urllib.request.urlopen(req)

 
while True:

    while not no_rain.is_active:
        GPIO.output(greenLED ,GPIO.HIGH)
        print("led on")
        send_message("Voda je detektovana")
        while True:
            if no_rain.is_active:
                GPIO.output(greenLED ,GPIO.LOW)
                print("led off")
                break

    sleep(1)
