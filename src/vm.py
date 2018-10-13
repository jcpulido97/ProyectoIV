import time
import json
import ipaddress
import re
import os

class VM:
    def __init__(self, nombre="", vcpu=-1, ram=0, uuid=0, ip="", vmdsk="",  mac_address="", alive=None, date_created = time.time()):

        if int(uuid) > 0:
            self.__uuid = int(uuid)
        else:
            self.__uuid = None

        if nombre:
            self.__nombre = str(nombre)
        else:
            self.__nombre = None

        if int(vcpu) > 0:
            self.__vcpu =  int(vcpu)
        else:
            self.__vcpu = -1

        # Memoria RAM en KB y es múltiplo de 2
        memoria = int(ram)
        if ((memoria & (memoria - 1)) == 0) and memoria > 0:
            self.__ram = int(ram)
        else:
            self.__ram = None

        try:
            ip = ipaddress.ip_address(ip)
            self.__ip = str(ip)
        except:
            self.__ip = None

        #vmdsk no puede estar vacío
        if os.path.exists(vmdsk):
            self.__vmdsk = vmdsk
        else:
            self.__vmdsk = None

        if re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", mac_address.lower()):
            self.__mac_address = mac_address
        else:
            self.__mac_address = None

        if isinstance(alive, bool):
            self.__alive = alive
        else:
            self.__alive = None

        if date_created > 0:
            self.__date_created = date_created
        else:
            self.__date_created = time.time()

    def getDateCreated(self):
        return self.__date_created

    def setDateCreated(self,date):
        if isinstance(date,float) or isinstance(date,int):
            if date > 0:
                self.__date_created = date
                return True
            else:
                return False
        else:
            return False

    def getNombre(self):
        return self.__nombre

    def setNombre(self,nombre):
        if nombre:
            self.__nombre = str(nombre)
            return True
        else:
            return False

    def getIP(self):
        return self.__ip

    def setIP(self,ip):
        try:
            ip = ipaddress.ip_address(ip)
            self.__ip = str(ip)
            return True
        except:
            return False

    def getMAC(self):
        return self.__mac_address

    def setMAC(self,mac_address):
        # MAC-address regex check
        if re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", mac_address.lower()):
            self.__mac_address = mac_address
            return True
        else:
            return False

    def isAlive(self):
        return self.__alive

    def setAlive(self,alive):
        if isinstance(alive, bool):
            self.__alive = alive
            return True
        else:
            return False

    def getVCPU(self):
        return self.__vcpu

    def setVCPU(self,num_cpu):
        if int(num_cpu) > 0:
            self.__vcpu = num_cpu
            return True
        else:
            return False

    def getRAM(self):
        return self.__ram

    def setRAM(self,ram):
        memoria = int(ram)
        # Comprobamos si la cantidad de memoria es potencia de 2
        if ((memoria & (memoria - 1)) == 0) and memoria > 0:
            self.__ram = ram
            return True
        else:
            return False

    def getUuid(self):
        return self.__uuid

    def setUuid(self,uuid):
        if int(uuid) > 0:
            self.__uuid = uuid
            return True
        else:
            return False

    def getVmdsk(self):
        return self.__vmdsk

    def setVmdsk(self,vmdsk):
        if os.path.exists(vmdsk):
            self.__vmdsk = vmdsk
            return True
        else:
            return False

    @staticmethod
    def fromJson(string):
        vm = VM()
        vm.__dict__ = json.loads(string)
        return vm

    def toJson(self):
        return __str__(self)

    def __str__(self):
        return json.dumps(self.__dict__)
        # return "{Nombre: "+str(self.nombre)+", Vcpu: "+str(self.vcpu)+", RAM: "+str(self.ram)+", UUID: "+str(self.uuid)+", IP: "+str(self.ip)+", VMDISK: "+str(self.vmdsk)+", MAC: "+str(self.mac_address)+", date_created: "+str(self.date_created)+"}"
