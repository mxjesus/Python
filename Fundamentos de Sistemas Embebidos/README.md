# Vídeo de demostración del funcionamiento del sistema

https://www.youtube.com/watch?v=MdtUl0X5Wl0

# Información

En general, este proyecto se trata de realizar un gimnasio dentro de una casa inteligente, el cual cuenta con sensores de movimiento, proximidad, temperatura, humedad, micrófonos, entre otros sensores que permiten una gran realización de tareas. Se realizó por medio de una Raspberry Pi Modelo 4B en el lenguaje de programación Python, así como algunos materiales extra. 

Se anexa el vídeo donde se ven las pruebas. (También se realizó una simulación en C++ pero no se encontró el código) 

# Descripción de los códigos

## AlarmaPV.py

Realiza el funcionamiento de la alarma en una ventana, en caso de detectar algo cercano, se encenderá y avisará al usuario a través de un bot de telegram.

## Bot1.py

Este programa lo que va a hacer es que, dependiendo del comando que el usuario ingrese en Telegram, entonces va a encender, apagar un LED en específico o todas al mismo tiempo.

## Bot2.py

Realiza la atenuación de las luces. 

## LCD.py

Este programa imprime en la LCD varios mensajes. 

## Ledsmusicales.py

Este programa se utilizará para la función de los leds musicales, con el uso de BlueDot.

## masterbot.py

Son hilos que realizan los programas tanto de la atenuación (bot2.py) como el encendido (bot1.py) y el apagado 

## modulomusica.py

Realizando el comando os.system en donde se va a reproducir música y se va a realizar el juego de luces.

## proyectofinal.py

Unión de script

## settings.py

Se da la información de la intensidad de los leds. 

## temperatura_humedad.py

Muestra cuál es la temperatura y humedad que el sensor detectó en ese instante, nos estará dando estos datos entre 5 y 15 segundos y en caso de que llegue a detectar que la temperatura que registró supera al que el usuario no quiere que sobrepase, lo mejor será que mande una señal de alerta.
