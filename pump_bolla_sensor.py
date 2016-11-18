__author__ = 'alexg'
import RPi.GPIO as GPIO #importamos la libreria para leer los puertos
import time             #

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN) #Read output from moisture detector
GPIO.setup(22, GPIO.OUT) #Bomba de agua output pin

counter = 0
while  True:
       #GPIO.input(17)
    if GPIO.input(17)  == 0:
        print ("riegos detectados")
        GPIO.output(22, 0) #Moisture en off
        time.sleep(5)
    elif GPIO.input(17)  == 1:            #when output from moisture is HIGH
        print ("Riego detectado, bomba activada")
        GPIO.output(22, 1)  #se activa la bomba
        time.sleep(5)
     #   counter = counter+1
     #   print (counter)

GPIO.clean()







