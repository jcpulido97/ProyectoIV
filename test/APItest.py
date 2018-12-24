import unittest, json, requests, time
from src.vm import VM
from random import randint

class APItest(unittest.TestCase):
    def setUp(self):
        # self.url = 'http://127.0.0.1:5000'
        self.url = 'https://vm-management-tool.herokuapp.com/'
        self.new_uuid = str(randint(0, 9999))
        response = requests.get(self.url+'/status')
        self.uuids = response.json().get('vm_pool_status').get('vm_UUIDs')

    def test_status(self):
        response = requests.get(self.url)
        self.assertEqual(response.status_code, 200, "Devuelve codigo correcto.")
        self.assertEqual(response.json()['status'], 'OK', "Devuelve estado correcto.")

    def test_app_status(self):
        response = requests.get(self.url+'/status')
        self.assertEqual(response.status_code, 200, "Devuelve codigo correcto.")
        self.assertNotEqual(response.json().get('vm_pool_status'), '', "vm_pool_status no definido")

    def test_vm_state(self):
        for uuid in self.uuids:
            if uuid:
                response = requests.get(self.url+'/vm/'+str(uuid))
                dict = response.json()
                vm = VM.fromJson(response.text)
                self.assertEqual(dict.get('uuid'), uuid, "UUID no es igual al de la VM")
                self.assertEqual(dict.get('nombre'), vm.getNombre(), "Nombre no es igual al de la VM")
                self.assertEqual(dict.get('vcpu'), vm.getVCPU(), "Vcpu no es igual al de la VM")
                self.assertEqual(dict.get('ram'), vm.getRAM(), "ram no es igual al de la VM")
                self.assertEqual(dict.get('ip'), vm.getIP(), "ip no es igual al de la VM")
                self.assertEqual(dict.get('vmdsk'), vm.getVmdsk(), "vmdsk no es igual al de la VM")
                self.assertEqual(dict.get('mac_address',''), vm.getMAC(), "mac_address no es igual al de la VM")
                self.assertEqual(dict.get('alive'), vm.isAlive(), "alive no es igual al de la VM")
                self.assertEqual(dict.get('date_created',0.0), vm.getDateCreated(), "date_created no es igual al de la VM")
            else:
                with self.assertRaises(Exception) as context:
                    raise Exception('UUID not found')


    def test_vm_registration(self):
        response = requests.put(self.url+'/vm/'+self.new_uuid).json()
        
        while response.get('code') != 200:
            self.new_uuid = str(randint(0, 9999))
            response = requests.put(self.url+'/vm/'+self.new_uuid).json()

        self.assertTrue(response.get('success'),'Máquina no fue registrada')
        res = requests.post(self.url+'/vm/'+self.new_uuid, data={'nombre' : 'rgb'})
        self.assertTrue(response.get('success'),'Nombre - Máquina no fue editada')
        res = requests.post(self.url+'/vm/'+self.new_uuid, data={'ram' : 1024})
        self.assertTrue(response.get('success'),'RAM - Máquina no fue editada')
        res = requests.post(self.url+'/vm/'+self.new_uuid, data={'vcpu' : 2})
        self.assertTrue(response.get('success'),'Vcpu - Máquina no fue editada')
        response = requests.delete(self.url+'/vm/'+self.new_uuid).json()
        self.assertTrue(response.get('success'),'Máquina no fue borrada')


if __name__ == '__main__':
    unittest.main()
