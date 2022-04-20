from requests import request
from Data import dataSensor
import RPi.GPIO as GPIO
import Adafruit_DHT
import time
from Data import dataSensor
from listaSensor import datalistaSensor
import datetime
#from operSensores import medicionSensores
from ApiAdonis import APIRestProyecto
import os
from gpiozero import MotionSensor
#from hx711 import HX711  # importa la clase HX711

class Sensores:
    def __init__(self):
        self.apiAdonis = APIRestProyecto("","")
        print(self.apiAdonis.getToken())
        self.lista = dataSensor()
        self.jsonlista = datalistaSensor()
        #self.valores=medicionSensores()
        
    def MetodoMedicion(self,medicion):
        self.apiAdonis.metodoGet()
        print(self.apiAdonis.MandarValores(medicion))
        
    def onoff(self, status):
        if(status == 1):
            self.motores()
            self.apiAdonis.metodoPutmotor()
        elif(status == 0):
            print('EL STATUS SIGUE EN 0')
        else:
            print('ALGO RARO PASA')
        
    def medicion(self,sensor, contador):
        if(sensor.tipo=='US'):
            self.sensorULTRASONICO(sensor)
        elif(sensor.tipo=='TEMP'):
            self.sensorTemp(sensor)
        elif(sensor.tipo=='HUM'):
            self.sensorHUM(sensor)
        elif(sensor.tipo=='PIR'):
            self.sensorPIR(sensor)
        elif(sensor.tipo=='GAS'):
            self.sensorgasMQ5(sensor)
        else:
            print('No esta en la lista')
    
    def sensorULTRASONICO(self,sensor):
        GPIO.setwarnings(False)
        date = datetime.datetime.now()
        self.objvalores=dataSensor()
        self.objvalores.id=sensor.id
        self.objvalores.clave=sensor.clave
        fecha = (date.strftime('%Y/%m/%d'))
        hora = date.strftime('%H:%M')
        self.objvalores.fecha=fecha
        self.objvalores.hora=hora
        pines=sensor.pin[0]
        trigger=pines['trigger']
        echo=pines['echo']
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(trigger, GPIO.OUT)
        GPIO.setup(echo, GPIO.IN)
        GPIO.output(trigger, True)
        time.sleep(1)
        GPIO.output(trigger, False)
        while GPIO.input(echo) == False:
            start = time.time()
        while GPIO.input(echo) == True:
            end = time.time()
        sig_time = end-start
        #Centimetros:
        distance = [sig_time / 0.000058]
        print('Distance: {} centimetros'.format(distance))
        self.objvalores.valor=distance
        diccionario=self.lista.getDictorys(self.objvalores)
        self.MetodoMedicion(diccionario)

    '''def sensorDHT11(self,sensor):
        GPIO.setwarnings(False)
        date = datetime.datetime.now()
        self.objvalores=dataSensor()
        self.objvalores.id=sensor.id
        self.objvalores.clave=sensor.clave
        fecha = (date.strftime('%Y/%m/%d'))
        hora = date.strftime('%H:%M')
        self.objvalores.fecha=fecha
        self.objvalores.hora=hora
        pines=sensor.pin[0]
        trigger=pines['trigger']
        sensor = Adafruit_DHT.DHT11 #Cambia por DHT22 y si usas dicho sensor
        #pin = sensores.pin[0] #Pin en la raspberry donde conectamos el sensor
        #pin = 4 #Pin en la raspberry donde conectamos el sensor
        print('Leyendo')
        humedad, temperatura = Adafruit_DHT.read_retry(sensor, trigger)
        print ('Humedad: ' , humedad)
        print ('Temperatura: ' , temperatura)
        ambiente = [humedad, temperatura]
        
        self.objvalores.valor=ambiente
        diccionario=self.lista.getDictorys(self.objvalores)
        self.valores.MetodoMedicion(diccionario)
        time.sleep(1000000) #Cada segundo se evalúa el sensor'''
    
    def sensorTemp(self,sensor):
        date = datetime.datetime.now()
        self.objvalores=dataSensor()
        self.objvalores.id=sensor.id
        self.objvalores.clave=sensor.clave
        fecha = (date.strftime('%Y/%m/%d'))
        hora = date.strftime('%H:%M')
        self.objvalores.fecha=fecha
        self.objvalores.hora=hora
        pines=sensor.pin[0]
        trigger=pines['trigger']
        sensor = Adafruit_DHT.DHT11 #Cambia por DHT22 y si usas dicho sensor
        #pin = sensores.pin[0] #Pin en la raspberry donde conectamos el sensor
        #pin = 4 #Pin en la raspberry donde conectamos el sensor
        temperatura = Adafruit_DHT.read_retry(sensor, trigger)
        print('el tipo')
        print(type(temperatura))
        print ('Temperatura: ' , temperatura)
        
        self.objvalores.valor=temperatura[0]
        diccionario=self.lista.getDictorys(self.objvalores)
        self.MetodoMedicion(diccionario)
        time.sleep(1) #Cada segundo se evalúa el sensor
        
    def sensorHUM(self,sensor):
        date = datetime.datetime.now()
        self.objvalores=dataSensor()
        self.objvalores.id=sensor.id
        self.objvalores.clave=sensor.clave
        fecha = (date.strftime('%Y/%m/%d'))
        hora = date.strftime('%H:%M')
        self.objvalores.fecha=fecha
        self.objvalores.hora=hora
        pines=sensor.pin[0]
        trigger=pines['trigger']
        sensor = Adafruit_DHT.DHT11 #Cambia por DHT22 y si usas dicho sensor
        #pin = sensores.pin[0] #Pin en la raspberry donde conectamos el sensor
        #pin = 4 #Pin en la raspberry donde conectamos el sensor
        print('Leyendo')
        humedad = Adafruit_DHT.read_retry(sensor, trigger)
        print ('Humedad: ' , humedad)
        
        self.objvalores.valor=humedad[1]
        diccionario=self.lista.getDictorys(self.objvalores)
        self.MetodoMedicion(diccionario)
        time.sleep(1) #Cada segundo se evalúa el sensor
        
    def sensorPIR(self, sensor):
        date = datetime.datetime.now()
        self.objvalores=dataSensor()
        self.objvalores.id=sensor.id
        self.objvalores.clave=sensor.clave
        fecha = (date.strftime('%Y/%m/%d'))
        hora = date.strftime('%H:%M')
        self.objvalores.fecha=fecha
        self.objvalores.hora=hora
        pines=sensor.pin[0]
        trigger=pines['trigger']
        status=2
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(trigger, GPIO.IN)
        if GPIO.input(trigger):
            status = 1
            self.objvalores.valor=status
            print('\nSe detecto una presencia')
        else:
            status = 0
            self.objvalores.valor=status
            print('\nNo hay presencia')
        time.sleep(1)
        diccionario=self.lista.getDictorys(self.objvalores)
        self.MetodoMedicion(diccionario)
        time.sleep(1)
        
        '''d.valor = status
        self.lista.add(d)'''
        '''pin = 5
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(23, GPIO.OUT)
        #LED

        pir = MotionSensor(pin)
        pir.wait_for_motion()
        
        print("Movimiento detectado")
        GPIO.output(23, True)
        pir.wait_for_no_motion()
        GPIO.output(23, False)'''
        
    def sensorgasMQ5(self, sensor):
        date = datetime.datetime.now()
        self.objvalores=dataSensor()
        self.objvalores.id=sensor.id
        self.objvalores.clave=sensor.clave
        fecha = (date.strftime('%Y/%m/%d'))
        hora = date.strftime('%H:%M')
        self.objvalores.fecha=fecha
        self.objvalores.hora=hora
        pines=sensor.pin[0]
        trigger=pines['trigger']
        #GPIO.setmode(GPIO.BCM)
        '''ledOutPin=23
        gasInPin=5
        readValue=1''' # default is 1 as Gas sensor deactivated
        
        #GPIO.setup(ledOutPin, GPIO.OUT)
        GPIO.setup(trigger, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        print("Detect changed of Gas sensor to " + str(GPIO.input(trigger)))
        readValue = GPIO.input(trigger)

        GPIO.add_event_detect(trigger, GPIO.BOTH)
        print("Detectando....")
        if readValue:
            status = 1
            self.objvalores.valor=status
            print('\nSe detecto Gas o Humo')
        else:
            status = 0
            self.objvalores.valor=status
            print('\nNo se detecto nada')
        time.sleep(1)
        diccionario=self.lista.getDictorys(self.objvalores)
        self.MetodoMedicion(diccionario)
        time.sleep(1)
        GPIO.cleanup()
        
    def motores(self):
        # Set GPIO numbering mode
        GPIO.setmode(GPIO.BCM)
        pina = 11
        pinb = 12
        # Set pin 11 as an output, and set servo1 as pin 11 as PWM
        GPIO.setup(pina,GPIO.OUT)
        GPIO.setup(pinb,GPIO.OUT)
        servo1 = GPIO.PWM(pina,50) # Note 11 is pin, 50 = 50Hz pulse
        servo2 = GPIO.PWM(pinb,50)
        #start PWM running, but with value of 0 (pulse off)
        servo1.start(0)
        servo2.start(0)
        print ("Waiting for 2 seconds")
        #time.sleep(0)
        # Turn back to 90 degrees
        print ("Turning back to 90 degrees for 2 seconds")
        servo1.ChangeDutyCycle(7)
        servo2.ChangeDutyCycle(7)
        time.sleep(5)
        #turn back to 0 degrees
        print ("Turning back to 0 degrees")
        servo1.ChangeDutyCycle(2)
        servo2.ChangeDutyCycle(2)
        time.sleep(0.5)
        servo1.ChangeDutyCycle(0)
        servo2.ChangeDutyCycle(0)
        #Clean things up at the end
        servo1.stop()
        GPIO.cleanup()
        print ("Goodbye")
        
            
    