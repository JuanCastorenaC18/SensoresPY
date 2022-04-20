import imp
from listaSensor import datalistaSensor
import ApiAdonis
import operSensores
import sensores

class Principal():
    def __init__(self):
        self.cont = 1
        self.Sensorlista= datalistaSensor()
        self.Sensorlista.toObjects()
        #self.metodSens=sensores.Sensores()
        self.valores = operSensores.medicionSensores()
        #self.valores.MetodoMedicion()
          
        while True:
            print('<<CONTADOR>>:  ',self.cont)
            self.cont = self.cont + 1
            for x in self.Sensorlista:
                self.Sensorlista.toObjects()
                self.valores.saveList()
                self.valores.controlMotor()
                #Lista a app
                
                self.valores.metodomedir(x, self.cont)
                #Medir motores
                #self.metodSens.medicion(x, self.cont)
                
            if(self.cont == 8):
                self.cont = 1

        
if __name__ == '__main__':
    main = Principal()