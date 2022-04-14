import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

try: 
    p = GPIO.PWM(21, 1000) # (номер пина, частота мерцания диода)
    p.start(0) # коэффициент заполнения импульса = 0

    while True:
        print("Введи коэффициент duty cycle:")
        dutycycle = int(input())
        p.start(dutycycle)

finally:
    GPIO.output(21, 0)
    GPIO.cleanup()

    