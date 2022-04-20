from Data import dataSensor
from ApiAdonis import APIRestProyecto
from sensores import Sensores
import time

class medicionSensores():
    def __init__(self):
         self.apiAdonis = APIRestProyecto("","")
         self.metodSens = Sensores()
         print(self.apiAdonis.getToken())
         self.dataMedicion = dataSensor()
         #self.sensor = self.dataMedicion.getDictorys()
         
         '''while True:
             print(self.apiAdonis.metodoGet())'''
         
        
    '''def MetodoMedicion(self,medicion):
        self.apiAdonis.metodoGet()
        print(self.apiAdonis.MandarValores(medicion))'''
        
    def saveList(self):
        #Guardar en archivo
        self.apiAdonis.guardar()
    
    def controlMotor(self):
        #Status motor
        status = self.apiAdonis.metodoGetmotor()
        print('EL STATUS', status)
        self.metodSens.onoff(status)
        
    def metodomedir(self, x, cont):
        #Medir motores
        self.metodSens.medicion(x, cont)