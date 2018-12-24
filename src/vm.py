from src.db import db

import time
import json
import ipaddress
import re
import os

class VM(db.Model):
    uuid = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), default='')
    vcpu = db.Column(db.Integer, default=0)
    ram = db.Column(db.Integer, default=0)
    ip = db.Column(db.String(15), default='')
    mac_address = db.Column(db.String(17), default='')
    vmdsk = db.Column(db.String(1000), default='')
    alive = db.Column(db.Boolean, default=False)
    date_created = db.Column(db.Float, default=time.time())

    def __repr__(self):
        return str(self)

    def __init__(self, nombre="", vcpu=0, ram=0, uuid=0, ip="", vmdsk="",  mac_address="", alive=False, date_created = time.time()):
        if int(uuid) > 0:
            self.uuid = int(uuid)
        else:
            self.uuid = 0

        if nombre:
            self.nombre = str(nombre)
        else:
            self.nombre = ''

        if int(vcpu) > 0:
            self.vcpu =  int(vcpu)
        else:
            self.vcpu = 0

        # Memoria RAM en KB y es múltiplo de 2
        memoria = int(ram)
        if memoria > 0:
            self.ram = int(ram)
        else:
            self.ram = 0

        try:
            ip = ipaddress.ip_address(ip)
            self.ip = str(ip)
        except:
            self.ip = ''

        #vmdsk no puede estar vacío
        self.vmdsk = vmdsk

        if re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", mac_address.lower()):
            self.mac_address = mac_address
        else:
            self.mac_address = ''

        if isinstance(alive, bool):
            self.alive = alive
        else:
            self.alive = False

        if date_created > 0:
            self.date_created = date_created
        else:
            self.date_created = time.time()

    def getDateCreated(self):
        return self.date_created

    def setDateCreated(self,date):
        if isinstance(date,float) or isinstance(date,int):
            if date > 0:
                self.date_created = date
                return True
            else:
                return False
        else:
            return False

    def getNombre(self):
        return self.nombre

    def setNombre(self,nombre):
        if nombre:
            self.nombre = str(nombre)
            return True
        else:
            return False

    def getIP(self):
        return self.ip

    def setIP(self,ip):
        try:
            ip = ipaddress.ip_address(ip)
            self.ip = str(ip)
            return True
        except:
            return False

    def getMAC(self):
        return self.mac_address

    def setMAC(self,mac_address):
        # MAC-address regex check
        if re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", mac_address.lower()):
            self.mac_address = mac_address
            return True
        else:
            return False

    def isAlive(self):
        return self.alive

    def setAlive(self,alive):
        if isinstance(alive, bool):
            self.alive = alive
            return True
        else:
            return False

    def getVCPU(self):
        return self.vcpu

    def setVCPU(self,num_cpu):
        if int(num_cpu) > 0:
            self.vcpu = num_cpu
            return True
        else:
            return False

    def getRAM(self):
        return self.ram

    def setRAM(self,ram):
        memoria = int(ram)
        # Comprobamos si la cantidad de memoria es potencia de 2
        if memoria > 0:
            self.ram = ram
            return True
        else:
            return False

    def getUuid(self):
        return self.uuid

    def setUuid(self,uuid):
        if int(uuid) > 0:
            self.uuid = uuid
            return True
        else:
            return False

    def getVmdsk(self):
        return self.vmdsk

    def setVmdsk(self,vmdsk):
        self.vmdsk = vmdsk
        return True

    @staticmethod
    def fromJson(string):
        vm = VM()
        intermediate = json.loads(string)
        for key in intermediate.keys():
            val = intermediate.get(key)
            if key == 'uuid':
                vm.setUuid(val)
            elif key == 'nombre':
                vm.setNombre(val)
            elif key == 'vcpu':
                vm.setVCPU(val)
            elif key == 'ram':
                vm.setRAM(val)
            elif key == 'ip':
                vm.setIP(val)
            elif key == 'vmdsk':
                vm.setVmdsk(val)
            elif key == 'mac_address':
                vm.setMAC(val)
            elif key == 'alive':
                vm.setAlive(val)
            elif key == 'date_created':
                vm.setDateCreated(val)

        return vm

    def toJson(self):
        return str(str(self))

    def __str__(self):
        dict = {
            'uuid'   : self.uuid,
            'ip'     : self.ip,
            'vcpu'   : self.vcpu,
            'nombre' : self.nombre,
            'mac'    : self.mac_address,
            'alive'  : self.alive,
            'ram'    : self.ram,
            'vmdsk'  : self.vmdsk,
            'date_created'  : self.date_created
        }
        return json.dumps(dict)
        # return "{Nombre: "+str(self.nombre)+", Vcpu: "+str(self.vcpu)+", RAM: "+str(self.ram)+", UUID: "+str(self.uuid)+", IP: "+str(self.ip)+", VMDISK: "+str(self.vmdsk)+", MAC: "+str(self.mac_address)+", date_created: "+str(self.date_created)+"}"
