import unittest, json, requests, time

class APItest(unittest.TestCase):
    def setUp(self):
        self.url = 'https://vm-management-tool.herokuapp.com/'
        self.uuid_test = None

    def test_status(self):
        response = requests.get(self.url)
        self.assertEqual(response.status_code, 200, "Devuelve codigo correcto.")
        self.assertEqual(response.json()['status'], 'OK', "Devuelve estado correcto.")

    def test_app_status(self):
        response = requests.get(self.url+'/status')
        self.assertEqual(response.status_code, 200, "Devuelve codigo correcto.")
        self.assertNotEqual(response.json().get('vm_pool_status'), '', "vm_pool_status no definido")

    def test_vm_state(self):
        response = requests.get(self.url+'/status')
        self.uuid_test = response.json().get('vm_pool_status').get('vm_UUIDs')[0]
        if self.uuid_test != None:
            response = requests.get(self.url+'/vm/'+str(self.uuid_test))
            self.assertEqual(response.status_code, 200, "Devuelve codigo correcto.")



if __name__ == '__main__':
    unittest.main()
