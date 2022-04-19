import RPi.GPIO as GPIO
import time 

def dec2bin (value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    print ("Введите период сигнала: ")
    period = int(input())

    while True:
        for i in range (0, 255, 1):
            GPIO.output(dac, dec2bin(i))
            time.sleep(period / 512)
        
        for i in range (255, 0, -1):
            GPIO.output(dac, dec2bin(i))
            time.sleep(period / 512)

finally: 
    GPIO.output(dac, 0)
    GPIO.cleanup()