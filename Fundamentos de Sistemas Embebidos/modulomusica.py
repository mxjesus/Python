#!/usr/bin/python

import os, sys

def moduloled():
    print("button 1 pressed")
    os.system("sudo python3 /home/pi/lightshowpi/py/synchronized_lights.py --file=/home/pi/lightshowpi/music/sample/VivaLaVida.mp3")
    
moduloled()