#!/usr/bin/python

from bluedot import BlueDot
from signal import pause
import os, sys
import threading

var = 0
var2 = 0
once = 0
once2 = 0
salir = 0
bd = BlueDot(cols=2, rows=1)
bd[0,0].color = "red"

def funcMusic():
    import modulomusica

def pressed_1(pos):
    global var,var2
    var = 1
    var2 = 0
    
def pressed_2(pos):
    global var,var2
    var = 0
    var2 = 1

b1 = threading.Thread(target=funcMusic, name='modulomusica', daemon = True)

while salir == 0:
    
    bd[0,0].when_pressed = pressed_1
    bd[1,0].when_pressed = pressed_2
    
    if var:
        if var2 == 0:
            if once == 0:
                b1.start()
                print("button 1 pressed")
                once = 1
                once2 = 0

    else:
        if var2 == 1:
            if once2 == 0:
                print("button 2 pressed")
                kill = os.popen("sudo pgrep python").read()
                print(type(kill),kill[-6:-1])
                inst = ''
                for i in kill[-6:-1]:
                    print(i)
                    if ord(i) >= 48 and ord(i) <= 57:
                        print(i,type(i),ord(i))
                        inst = inst + i
                evento = "sudo kill" + " " + inst
                print(evento)
                os.system(evento)
                salir = 1
print("Luces musicales apagadas")
        
