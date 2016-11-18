#!/usr/bin/env python

##############################################################################
#
# Written by Alex Gomez for the Raspberry Pi - 2016
#
# Website:
# Contact: alejandrogomezpublic@gmail.com
#
# Feel free to use and modify this code for you own use in any way.
#
# This program is designed to turn ON / OFF GPIO ports and relays on and off
# at set times stored in a MySql database.
#
##############################################################################


import RPi.GPIO as GPIO #import library to read port GPIO
import time             # that allow to sleep timers

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN) #Read output from crontroller detector
GPIO.setup(7, GPIO.OUT) #Water pump or selenoid Off


while  True:
    if GPIO.input(17)  == 1:                        #check the status of the signal water level sensor
        print ("Botella Patron vacia o dispnible")  #if the sensor is ON Down will activate the pump in 5 sec
        GPIO.output(7, 0)                           #Water pump or selenoid Off
        time.sleep(5)
    elif GPIO.input(17)  == 0:                      #when output from sensor water level is Off
        print ("Riego detectado, bomba activada")
        GPIO.output(7, 1)                           #Water pump or selenoid On
        time.sleep(5)

GPIO.clean()













