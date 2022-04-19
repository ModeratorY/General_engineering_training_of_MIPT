import RPi.GPIO as GPIO
import time

def dec2bin (value):
    return [int(elem) for elem in bin(value)[2:].zfill(8)]

def from_10_to_2_dac (val):
    signal = dec2bin(val)
    GPIO.output (dac, signal)
    return signal 

def adc (): 

    compvalue = 0

    for Value in range(256):

        GPIO.output(dac, dec2bin(value))
        
        time.sleep(0.005)

        compsignal = GPIO.input(comp)

        if compsignal == 0:

            compvalue = value
            break
    
    return compvalue


dac = [26, 19, 13, 6, 5, 11, 9, 10]


comp = 4
troyka = 17
maxV = 3.3
levels = 256

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)

GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)

GPIO.setup(comp, GPIO.IN)

try:
    while True:

        compValue = adc()
        binV = dec2bin(compValue)

        V = compValue / levels * maxV

        print("Значени:", compValue, "Бинарный код:", binV, "Напряжение:", V)

finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup()