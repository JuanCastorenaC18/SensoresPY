import json
import os.path


class dataSensor():
    def __init__(self,  id='', fecha='', hora='', clave='', valor='', lista=list()):
        self.id = id
        self.clave = clave
        self.fecha = fecha
        self.hora = hora
        self.valor = valor
        self.lista = lista
    
    # CRUD
    def add(self, sensor):
        self.lista.append(sensor)
        
    def eliminar(self, sensor):
        self.lista.remove(sensor)
        
    def getSensormedida(self, index):
        return self.lista[index]
    
    def modificar(self, index, sensor):
        self.lista[index] = sensor
        self.lista.pop(index)
        self.lista.insert(index, sensor)
        
    def tamano(self):
        return len(self.lista)
    
    def getlist(self):
        return self.lista
    
    def __str__(self):
        return self.id + ' \t\t' + self.fecha + '\t\t' + self.hora + ' \t\t' + self.clave + ' \t\t' + self.valor
    
    def searchS(self, buscar):
        for a in self.lista:
            if a.sensor == buscar:
                print(a.id, " ", a.clave, " ", a.fecha, " ", a.hora, " ", a.valor)
                
    def getDictorys(self,objmedir):
        return {
            "id": objmedir.id,
            "clave": objmedir.clave,
            "fecha": objmedir.fecha,
            "hora": objmedir.hora,
            "valor": objmedir.valor
        }
    def getDictoryPrueba(self):
        return {
            "id": 1,
            "clave": "US",
            "fecha": "2022-04-18",
            "hora": "15:01",
            "valor": 11.2334
        }
        
    def convertirdic(self):
        for x in self.lista:
            dicc = x.getDictorys()
        return dicc
    
    def listDicts(self):
        listDiccionario = list()
        for x in self.lista:
            listDiccionario.append(x.getDictoryp())
            print(x.getDictoryp())
        return listDiccionario
    
    def getDataJson(self):
        data = []
        print(type(data))
        if os.path.isfile("Json/productos.json"):
            file = open("Json/productos.json", "r")
            data = json.loads(file.read())
            print(type(data))
        return data
    
    def toJsonM(self, listajson):
        file = open("medidas.json", "w")
        json.dump(listajson, file, indent=4, sort_keys=True)
