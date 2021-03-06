import RPi.GPIO as GPIO
import time

def dec2bin (value):
    return [int(elem) for elem in bin(value)[2:].zfill(8)]

def  from_10_to_2_dac (val):
    signal = dec2bin(val)
    GPIO.output (dac, signal)
    return signal 

def bin2dec(value):
    dec = 0
    deg = 0

    for i in range(7, -1, -1):       
        dec += (2 * value[i]) ** deg
        deg += 1

    return dec

def adc (): 

    bin = dec2bin(0)

    for i in range(7):

        bin[i] = 1
        GPIO.output(dac, bin)
        time.sleep(0.001)

        if GPIO.input(comp) == 0:
            bin[i] = 0

    dec = bin2dec(bin)

    return dec

dac = [26, 19, 13, 6, 5, 11, 9, 10]

comp = 4
troyka = 17
maxV = 3.3

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

leds = [21, 20, 16, 12, 7, 8, 25, 24]

GPIO.setup(leds, GPIO.OUT)

def ledsFunc(V):

    GPIO.output(leds, 0)

    i = int(((V + 0.1) / 3.3) * 8)

    for j in range(i):
        GPIO.output(leds[j], 1)

try:
    while True:
        dec = adc()
        
        V = (3.3 * dec) / 256
       
        print("Напряжение: ", V)

        ledsFunc(V)

finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup()