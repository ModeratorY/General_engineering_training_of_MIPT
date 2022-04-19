import RPi.GPIO as GPIO

def decimal2binary (value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try: 

    while True:
        print("\nВведите число от 0 до 255 для подачи напряжения(exit = выход): ")

        number = input()

        if number == exit: exit()

        if number.isdigit() != 1:
            print("Это не целое число или оно отрицательное!")
            exit()
            
        number = int(number)

        if (number > 255) or (number < 0):
            print ("Это не число в нужно диапазоне (от 0 до 255)")
            exit()

        GPIO.output(dac, decimal2binary(number))
        print("Напряжение:  {:.4f}".format((3.3 * number) / 256), "\n")

finally: 
    GPIO.output(dac, 0)
    GPIO.cleanup()