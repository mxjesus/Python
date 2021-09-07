#!/usr/bin/python

import time
import RPi.GPIO as GPIO
from time import sleep
from signal import pause


# Assignment of GPIO pins
LCD_RS = 2
LCD_E  = 3
LCD_DATA4 = 10
LCD_DATA5 = 9
LCD_DATA6 = 11
LCD_DATA7 = 8

LCD_WIDTH = 16      # Characters per line
LCD_LINE_1 = 0x80   # Address of the first line of the display
LCD_LINE_2 = 0xC0   # Address of the second line of the display
LCD_CHR = GPIO.HIGH
LCD_CMD = GPIO.LOW
E_PULSE = 0.0005
E_DELAY = 0.0005

def lcd_send_byte(bits, mode):
    # Set pins to LOW
    GPIO.output(LCD_RS, mode)
    GPIO.output(LCD_DATA4, GPIO.LOW)
    GPIO.output(LCD_DATA5, GPIO.LOW)
    GPIO.output(LCD_DATA6, GPIO.LOW)
    GPIO.output(LCD_DATA7, GPIO.LOW)
    if bits & 0x10 == 0x10:
      GPIO.output(LCD_DATA4, GPIO.HIGH)
    if bits & 0x20 == 0x20:
      GPIO.output(LCD_DATA5, GPIO.HIGH)
    if bits & 0x40 == 0x40:
      GPIO.output(LCD_DATA6, GPIO.HIGH)
    if bits & 0x80 == 0x80:
      GPIO.output(LCD_DATA7, GPIO.HIGH)
    time.sleep(E_DELAY)    
    GPIO.output(LCD_E, GPIO.HIGH)  
    time.sleep(E_PULSE)
    GPIO.output(LCD_E, GPIO.LOW)  
    time.sleep(E_DELAY)      
    GPIO.output(LCD_DATA4, GPIO.LOW)
    GPIO.output(LCD_DATA5, GPIO.LOW)
    GPIO.output(LCD_DATA6, GPIO.LOW)
    GPIO.output(LCD_DATA7, GPIO.LOW)
    if bits&0x01==0x01:
      GPIO.output(LCD_DATA4, GPIO.HIGH)
    if bits&0x02==0x02:
      GPIO.output(LCD_DATA5, GPIO.HIGH)
    if bits&0x04==0x04:
      GPIO.output(LCD_DATA6, GPIO.HIGH)
    if bits&0x08==0x08:
      GPIO.output(LCD_DATA7, GPIO.HIGH)
    time.sleep(E_DELAY)    
    GPIO.output(LCD_E, GPIO.HIGH)  
    time.sleep(E_PULSE)
    GPIO.output(LCD_E, GPIO.LOW)  
    time.sleep(E_DELAY)  

def display_init():
    lcd_send_byte(0x33, LCD_CMD)
    lcd_send_byte(0x32, LCD_CMD)
    lcd_send_byte(0x28, LCD_CMD)
    lcd_send_byte(0x0C, LCD_CMD)  
    lcd_send_byte(0x06, LCD_CMD)
    lcd_send_byte(0x01, LCD_CMD)  

def lcd_message(message):
    message = message.ljust(LCD_WIDTH," ")  
    for i in range(LCD_WIDTH):
      lcd_send_byte(ord(message[i]),LCD_CHR)

            
if __name__ == '__main__':
    # initialize
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(LCD_E, GPIO.OUT)
    GPIO.setup(LCD_RS, GPIO.OUT)
    GPIO.setup(LCD_DATA4, GPIO.OUT)
    GPIO.setup(LCD_DATA5, GPIO.OUT)
    GPIO.setup(LCD_DATA6, GPIO.OUT)
    GPIO.setup(LCD_DATA7, GPIO.OUT)

    display_init()
    
#xd
    while True: 
        lcd_send_byte(LCD_LINE_1, LCD_CMD)
        lcd_message("Sistemas")
        lcd_send_byte(LCD_LINE_2, LCD_CMD)
        lcd_message("Embebidos")
        sleep(4)
        lcd_send_byte(LCD_LINE_1, LCD_CMD)
        lcd_message("Jesus Jimenez")
        lcd_send_byte(LCD_LINE_2, LCD_CMD)
        lcd_message("Juarez")
        sleep(4)
        lcd_send_byte(LCD_LINE_1, LCD_CMD)
        lcd_message("Gabriel Daniel")
        lcd_send_byte(LCD_LINE_2, LCD_CMD)
        lcd_message("Aguilar Luna")
        sleep(4)
        lcd_send_byte(LCD_LINE_1, LCD_CMD)
        lcd_message("Proyecto Final")
        lcd_send_byte(LCD_LINE_2, LCD_CMD)
        lcd_message("*GIMNASIO*")
        sleep(4)
    GPIO.cleanup()
