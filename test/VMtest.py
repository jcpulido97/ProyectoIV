import unittest
import time
from src.vm_test import VM

class TestVM(unittest.TestCase):
    def setUp(self):
        self.vm = VM()

    def test_ip(self):
        new_ip="0.0.0.0"
        self.assertTrue(self.vm.setIP(new_ip), 'Fallo en el cambio de ip')
        self.assertEqual(self.vm.getIP(), new_ip, 'Fallo en el cambio de ip')
        bad_formated_ip = "4561.16358.10.-12"
        self.assertFalse(self.vm.setIP(bad_formated_ip), 'Fallo, aceptó una ip mal formateada '+bad_formated_ip)
        self.assertFalse(self.vm.setIP("256.256.256.256"), 'Fallo, aceptó una ip imposible')
        self.assertEqual(self.vm.getIP(), new_ip, 'Fallo en el cambio de ip')

    def test_mac(self):
        new_mac ="ff:ff:ff:ff:ff:ff"
        self.assertTrue(self.vm.setMAC(new_mac), 'Fallo en el cambio de mac')
        self.assertEqual(self.vm.getMAC(), new_mac, 'Fallo en el cambio de mac')
        bad_formated_mac = "aa:aa:aaa:aa:aa:aa"
        self.assertFalse(self.vm.setMAC(bad_formated_mac), 'Fallo, aceptó una mac mal formateada '+bad_formated_mac)
        self.assertEqual(self.vm.getMAC(), new_mac, 'Fallo en el cambio de mac')

    def test_nombre(self):
        nuevo_nombre = "asdf"
        self.assertTrue(self.vm.setNombre(nuevo_nombre), 'Fallo en el cambio de nombre')
        self.assertEqual(self.vm.getNombre(), nuevo_nombre, 'Fallo en el cambio de nombre')
        self.assertFalse(self.vm.setNombre(""), 'Fallo, aceptó un nombre vacío')
        self.assertEqual(self.vm.getNombre(), nuevo_nombre, 'Fallo en el cambio de nombre')

    def test_vcpu(self):
        self.assertTrue(self.vm.setVCPU(8), 'Fallo en el cambio de número de vcpus')
        self.assertEqual(self.vm.getVCPU(), 8, 'Fallo en el cambio de número de vcpu')
        self.assertFalse(self.vm.setVCPU(-1), 'Fallo, aceptó un número de vcpus <= 0')
        self.assertEqual(self.vm.getVCPU(), 8, 'Fallo en el cambio de número de vcpu')

    def test_ram(self):
        self.assertTrue(self.vm.setRAM(8192), 'Fallo en el cambio de cantidad de RAM')
        self.assertEqual(self.vm.getRAM(), 8192, 'Fallo en el cambio de cantidad de RAM')

    def test_uuid(self):
        self.assertTrue(self.vm.setUuid(1234), 'Fallo en el cambio de UUID')
        self.assertEqual(self.vm.getUuid(), 1234, 'Fallo en el cambio de UUID')
        self.assertFalse(self.vm.setUuid(0), 'Fallo, aceptó un UUID inaceptable')
        self.assertEqual(self.vm.getUuid(), 1234, 'Fallo en el cambio de UUID')

    def test_alive(self):
        self.assertTrue(self.vm.setAlive(True), 'Fallo al cambiar el estado alive')
        self.assertEqual(self.vm.isAlive(), True, 'Fallo al cambiar el estado alive')
        self.assertFalse(self.vm.setAlive(None), 'Fallo, aceptó un estado distinto a Verdadero/Falso')
        self.assertEqual(self.vm.isAlive(), True, 'Fallo al cambiar el estado alive')

    def test_date_created(self):
        tiempo = time.time()
        self.assertTrue(self.vm.setDateCreated(tiempo), 'Fallo al cambiar la fecha de creación a '+ str(tiempo))
        self.assertEqual(self.vm.getDateCreated(), tiempo, 'Fallo al cambiar la fecha de creación a '+ str(tiempo))
        tiempo = 1234
        self.assertTrue(self.vm.setDateCreated(tiempo), 'Fallo al cambiar la fecha de creación a ' + str(tiempo))
        self.assertEqual(self.vm.getDateCreated(), tiempo, 'Fallo al cambiar la fecha de creación a '+ str(tiempo))
        self.assertFalse(self.vm.setDateCreated(None), 'Fallo, aceptó una fecha de creación imposible')
        self.assertEqual(self.vm.getDateCreated(), tiempo, 'Fallo al cambiar la fecha de creación a '+ str(tiempo))

    def test_vmdsk(self):
        self.assertTrue(self.vm.setVmdsk("/home/"), 'Fallo al cambiar el path del vmdsk')
        self.assertEqual(self.vm.getVmdsk(), "/home/", 'Fallo al cambiar el path del vmdsk')

    def test_fromJson(self):
        string = '{"uuid": 123, "nombre": "test1", "vcpu": 1, "ram": 4096, "ip": "192.168.1.2", "vmdsk": "/", "mac_address": "08:00:27:81:14:5e", "alive": false, "date_created": 1539104862.8222692}'
        vm = VM.fromJson(string)
        self.assertTrue(isinstance(vm,VM), 'Fallo al deserializar el formato json')
        self.assertEqual(vm.getUuid(), 123, 'Fallo al deserializar el formato json (UUID)')
        self.assertEqual(vm.getNombre(), "test1", 'Fallo al deserializar el formato json (Nombre)')
        self.assertEqual(vm.getVCPU(), 1, 'Fallo al deserializar el formato json (VCPU)')
        self.assertEqual(vm.getRAM(), 4096, 'Fallo al deserializar el formato json (RAM)')
        self.assertEqual(vm.getIP(), "192.168.1.2", 'Fallo al deserializar el formato json (IP)')
        self.assertEqual(vm.getVmdsk(), "/", 'Fallo al deserializar el formato json (Vmdsk)')
        self.assertEqual(vm.getMAC(), "08:00:27:81:14:5e", 'Fallo al deserializar el formato json (MAC)')
        self.assertEqual(vm.isAlive(), False, 'Fallo al deserializar el formato json (Alive)')
        self.assertEqual(vm.getDateCreated(), 1539104862.8222692, 'Fallo al deserializar el formato json (date_created)')

if __name__ == '__main__':
    unittest.main()
