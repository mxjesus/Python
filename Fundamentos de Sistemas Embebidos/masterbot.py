#!/usr/bin/python
# main.py

from gpiozero import PWMLED
import settings
import threading

settings.init()

def funcBot1():
    import bot1
def funcBot2():
    import bot2
#def funcBot3():
#    import temperatura_humedad

b1 = threading.Thread(target=funcBot1, name='bot1', daemon = True)
b2 = threading.Thread(target=funcBot2, name='bot2', daemon = True)
#b3 = threading.Thread(target=funcBot3, name='temperatura_humedad', daemon = True)
b1.start()
b2.start()
#b3.start()


mapeo_leds_gpio = {1:PWMLED(26),2:PWMLED(19),3:PWMLED(13),4:PWMLED(6),5:PWMLED(5),6:PWMLED(0),7:PWMLED(1),8:PWMLED(12)}

while True:
    #print(settings.ledList)
    #print(settings.intensidadLeds)
    for x, y in mapeo_leds_gpio.items():
        if settings.ledList[x] == 1:
            y.value = settings.intensidadLeds
        else:
            y.value = 0