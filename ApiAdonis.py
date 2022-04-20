from email import header
import time
import json
from unicodedata import name
from wsgiref import headers
import requests 
from requests.structures import CaseInsensitiveDict
from Data import dataSensor

class APIRestProyecto:
    def __init__(self,domain,prefix,lista=list()):
        self.domain=domain
        self.prefix=prefix
        self.lista=lista
        self.domain="http://3.140.250.50:3333"
        self.prefix = "/"
        self.endpoint = self.domain+self.prefix
        self.token = ""
        self.listaMedicion = dataSensor()
        
        
    def getToken(self,path="login/:request"):
        path="http://3.140.250.50:3333/login/:request"
        headers = CaseInsensitiveDict()
        headers["Accept"] = "application/json"
        resp = requests.post(path,data=datalogin, headers=headers)
        tok=resp.json()
        self.token=tok['token']
        return resp.json()
    
    def toObjects(self):
        lista=list()
        data=self.getDataJson()
        for x in data:
            lista.append(id=x['id'],tipo=x['tipo'],pin=x["pin"],clave=x["clave"])
        self.lista=lista
        
    def metodoPost(self,path,sensor):
        path=self.endpoint+path
        headers=CaseInsensitiveDict()
        headers["Accept"] = "application/json"
        headers["Authorization"] = "Bearer %s" % self.token
        reque=requests.post(path,data=sensor,headers=headers)
        return reque.json()
    
    def metodoPostM(self, path='guardarMedicion/:request'):
        path="http://3.140.250.50:3333/guardarMedicion/:request"
        headers=CaseInsensitiveDict()
        headers["Accept"] = "application/json"
        headers["Authorization"] = "Bearer %s" % self.token
        reque=requests.post(path,datamedicion=sensor,headers=headers)
        return reque.json()
    
    def MandarValores(self,sensor):
        path="http://3.140.250.50:3333/guardarMedicion/:request"
        headers=CaseInsensitiveDict()
        headers["Accept"] = "application/json"
        headers["Authorization"] = "Bearer %s" % self.token
        reque=requests.post(path,data=sensor,headers=headers)
        return reque.json()
    
    
    
    def metodoGet(self):
        try:
            self.lista=[]
            path="http://3.140.250.50:3333/verSensores"
            headers = CaseInsensitiveDict()
            headers["Accept"] = "application/json"
            headers["Authorization"] = "Bearer %s" % self.token
            resp = requests.get(path, headers=headers)
            lis=resp.json()
            self.lista=lis
            self.toJson(self.lista)
            return resp.json()
        except:
            print('ERROR NO VA JSON VACIO')
    
    def metodoGetmotor(self):
        path="http://3.140.250.50:3333/obtenerStatus"
        headers = CaseInsensitiveDict()
        headers["Accept"] = "application/json"
        headers["Authorization"] = "Bearer %s" % self.token
        resp = requests.get(path, headers=headers)
        #print(resp.json())
        return resp.json()
    
    def metodoPutmotor(self):
        path="http://3.140.250.50:3333/cambiarStatus"
        headers = CaseInsensitiveDict()
        headers["Accept"] = "application/json"
        headers["Authorization"] = "Bearer %s" % self.token
        resp = requests.put(path, headers=headers)
        #print(resp.json())
        return resp.json()
    
    def toJson(self,listaSensores):		
        file = open("sensores.json", "w")
        file = json.dump([ob for ob in listaSensores], file,indent=4)     
         
    def guardar(self):
        res = self.metodoGet() 
        self.toJson(res)
        return res
            
    def __next__(self):
        if self.__idx__<len(self.lista):
            x =self.lista[self.__idx__]
            self.__idx__+=1 
            return x
        else:
            raise StopIteration 
    def __iter__(self):
        self.__idx__ = 0
        return self
    
datalogin = 	{
		"email":"angel@gmail.com",
        "password":"1234"
	}



#print(communication.metodoPost("guardarSensor/:request",data)) 
'''print(communication.getToken(datalogin))'''
'''while True:
        communication.guardar()
        communication.metodoPostM()'''


