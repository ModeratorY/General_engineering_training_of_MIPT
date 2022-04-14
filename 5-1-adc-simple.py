import RPi.GPIO as GPIO
import time

def dec2bin (value):
    return [int(elem) for elem in bin(value)[2:].zfill(8)]

def from_10_to_2_dac (val):
    signal = dec2bin(val)
    GPIO.output (dac, signal)
    return signal 

def adc (): 
    compValue = GPIO.input (comp)
    return compValue

maxVoltage = 3.3

dac = [26, 19, 13, 6, 5, 11, 9, 10]

comp = 4
troyka = 17
maxVoltage = 3.3
levels = 256

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)

GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)

GPIO.setup(comp, GPIO.IN)

try:
    while True:

        for value in range (256): 
            signal = from_10_to_2_dac(value)
            compVal = adc ()
            V = value / levels * maxVoltage 
    

            if (compVal == 0):
                print("Значение:", value, "Бинарный код значения:", signal,"Напряжение:", V)
                break

            time.sleep (0.005)

finally:
    GPIO.output(dac,GPIO.LOW)
    GPIO.cleanup()