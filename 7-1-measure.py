import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt


dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
comp = 4
troyka = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)   # светодиоды
GPIO.setup(dac, GPIO.OUT)    # ЦАП
GPIO.setup(troyka, GPIO.OUT) # тройка - модуль
GPIO.setup(comp, GPIO.IN)    # компоратор

def dec2bin(value):
    return [int(bit) for bit in bin(int(value))[2:].zfill(8)]

def bin2dec(list):

    weight = 2 ** 8 # разрядность DEC
    val = 0

    for i in range(0, 8):
        val += weight * list[i]
        weight /= 2
    
    return val
    
def adc():

    ls = [0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(0, 8):

        ls[i] = 1

        GPIO.output(dac, ls)

        time.sleep(0.001)

        if(GPIO.input(comp) == 0):
            ls[i] = 0

    return bin2dec(ls)

data = []

try:
    StartTime = time.time() # момент начала измерений

    GPIO.output(17, 1)       # подали на спаянную плату напряжение
    
    val = 0

    while(val <= 255 * 0.97): # пока конденсатор не заряжен почти до конца
        
        val = adc()
        data.append(val)

        print("V = {:.2f}".format(val * 3.3 / 256))

        GPIO.output(leds, dec2bin(val))

    endChargeTime = time.time() # момент полной зарядки конденсатора
    charge_time = endChargeTime - StartTime # время потраченное на зарядку
    
    GPIO.output(17, 0)       # убрали на спаянной плату напряжение

    val = 255

    while(val >= 255 * 0.02): # пока конденсатор не разряжен почти до конца

        val = adc()
        data.append(val)

        print("V: {:.2f}".format(val * 3.3 / 256))
        
        GPIO.output(leds, dec2bin(val))
    
    EndDischargeTime = time.time() # момент полной разрядки конденсатора
    Finish_Time = EndDischargeTime - StartTime # время эксперимента
        
finally:
    GPIO.output(dac, 0)
    GPIO.output(leds, 0)
    GPIO.cleanup()

plt.plot(data) # построить график
plt.show()     # показать график

data_str = [str(item) for item in data] # список всех значение в data

with open("7-1-data.txt", "w") as outfile:
    outfile.write("\n".join(data_str))

with open("7-1-settings.txt", "w") as outfile:
    outfile.write("Частота дискретизации:", len(data) / Finish_Time, "Hz") 
    outfile.write("Шаг квантования АЦП: {:.4f}", format(3.3 / 256), "V")

print("Общая продолжительность эксперимента:", Finish_Time, "c")
print("Период одного измерения:", Finish_Time / len(data), "c")  # ?????????????
print("Частота дискретизации:", len(data) / Finish_Time, "Hz")   # ?????????????
print("Шаг квантования АЦП: {:.4f}", format(3.3 / 256), "V")