#!/usr/bin/env python 

import subprocess


# Iterable con las rutas de los scripts
scripts_paths = ("/home/pi/Documents/Fundamentos de Sistemas Embebidos./Proyecto/masterbot.py",
                 "/home/pi/Documents/Fundamentos de Sistemas Embebidos./Proyecto/temperatura_humedad.py",
                 "/home/pi/Documents/Fundamentos de Sistemas Embebidos./Proyecto/Ledsmusicales.py",
                 "/home/pi/Documents/Fundamentos de Sistemas Embebidos./Proyecto/LCD.py",
                 "/home/pi/Documents/Fundamentos de Sistemas Embebidos./Proyecto/AlarmaPV.py")

# Creamos cada proceso    
procesos = [subprocess.Popen(["python", script]) for script in scripts_paths]

# Esperamos a que todos los subprocesos terminen.
for proceso in procesos:
    proceso.wait()

# Resto de código a ejecutar cuando terminen todos los subprocesos.