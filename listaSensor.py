import json
import os


class datalistaSensor():
    def __init__(self,  id='', pin=[], tipo='', clave='', listaS=list()):
        self.id = id
        self.pin = pin
        self.tipo = tipo
        self.clave = clave
        self.listaS = listaS

    def tamano(self):
        return len(self.listaS)
        
    def getlist(self):
        return self.listaS
    
    def __str__(self):
        return str(self.id) + ' \t\t' + str(self.pin) + '\t\t' + str(self.tipo) + ' \t\t' + str(self.clave)
    
    def searchS(self, buscar):
        for a in self.listaS:
            if a.sensor == buscar:
                print(a.id, " ", a.pin, " ", a.tipo, " ", a.clave, "", a.clave)
                
    def getDictoryls(self):
        return {
            "id": self.id,
            "pin": self.pin,
            "tipo": self.tipo,
            "clave": self.clave
        }
        
    def convertirdic(self):
        for x in self.listaS:
            dicc = x.getDictoryls()
        return dicc
    
    def listDictls(self):
        listDiccionario = list()
        for x in self.listaS:
            listDiccionario.append(x.getDictoryls())
            print(x.getDictoryls())
        return listDiccionario
    
    def getDataJson(self):
        data = []
        if os.path.isfile("sensores.json"):
            file = open("sensores.json", "r")
            data = json.loads(file.read())
        return data
    
    def toObjects(self):
        listaOS=list()
        data=self.getDataJson()
        for x in data:
            listaOS.append(datalistaSensor (id=x['id'],tipo=x['tipo'],pin=x["pin"],clave=x["clave"]))
        self.listaS=listaOS
        
    def __next__(self):
        if self.__idx__<len(self.listaS):
            x =self.listaS[self.__idx__]
            self.__idx__+=1 
            return x
        else:
            raise StopIteration 
    def __iter__(self):
        self.__idx__ = 0
        return self
            
    '''def verificar(self):
        for x in self.listaS:
            print(x.id)'''