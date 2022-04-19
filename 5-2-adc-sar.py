import RPi.GPIO as GPIO
import time

def dec2bin (value):
    return [int(elem) for elem in bin(value)[2:].zfill(8)]

def  from_10_to_2_dac (val):
    signal = dec2bin(val)
    GPIO.output (dac, signal)
    return signal 

def adc (): 
    compValue = GPIO.input (comp)
    return compValue

dac = [26, 19, 13, 6, 5, 11, 9, 10]

comp = 4
troyka = 17
maxV = 3.3

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

start_signal = [1, 0, 0, 0, 0, 0, 0, 0]

try:
    while True:
        
        value = 0
        
        for n in range (8): 
            value += int(2 ** (7 - n))

            signal = dec2bin(value)

            GPIO.output (dac, signal)

            time.sleep(0.001)
            
            V = value /256 * maxV

            compVal = adc ()

            if (compVal == 0):
                value -= 2 ** (7 - n)

        print("Значение:", value, "Бинарный код:", signal,"Напряжение:", V)

finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup()