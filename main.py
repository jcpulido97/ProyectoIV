from flask import *
from src.vm import VM
import json, signal, sys

app = Flask(__name__)
vm_pool = {}
vm_pool_json_path = "src/vm_pool.json"

def graceful_exit(sig, frame):
    global vm_pool
    global vm_pool_json_path
    print("\n--- Updating vm_pool.json")
    f = open(vm_pool_json_path, 'r+')
    try:
        for linea in f:
            vm = VM.fromJson(linea)
            if vm.getUuid() in vm_pool:
                del vm_pool[vm.getUuid()]
        for i in vm_pool.keys():
            json = str(vm_pool.get(i))
            print("["+str(i)+"] : "+ json +'\n')
            f.write(json + "\n")
        f.close()
    except IOError as err:
       print("Error file: " + str(err))

    sys.exit(0)

signal.signal(signal.SIGINT, graceful_exit)

with open(vm_pool_json_path) as f:
    for linea in f:
        vm = VM.fromJson(linea)
        vm_pool[vm.getUuid()] = vm


@app.route('/', methods = ['GET'])
def status():
    response =  {"status" : "OK"}
    return jsonify(response);

@app.route('/status', methods = ['GET'])
def status_vm():
    num_vm_alive = 0
    ram_used = 0
    total_vcpu = 0
    vcpu_in_use = 0
    ram_in_use = 0
    for i in vm_pool.keys():
        ram_used += vm_pool.get(i).getRAM()
        total_vcpu += vm_pool.get(i).getVCPU()
        if(vm_pool.get(i).isAlive()):
            num_vm_alive += 1
            vcpu_in_use += vm_pool.get(i).getVCPU()
            ram_in_use += vm_pool.get(i).getRAM()
    response =  {"status" : "OK",
                 "vm_pool_status" :
                    {
                     "total_vm" : len(vm_pool),
                     "VMs_alive" : num_vm_alive,
                     "total_ram" : ram_used,
                     "total_vcpu" : total_vcpu,
                     "in_use_ram" : ram_in_use,
                     "in_use_vcpu" : vcpu_in_use,
                     "vm_UUIDs" : list(vm_pool.keys())
                     }
                 }
    return jsonify(response);

@app.route('/vm/<uuid>', methods = ['GET'])
def serve_vm(uuid):
    global vm_pool
    vm = vm_pool.get(int(uuid))
    if vm != None:
        return Response(str(vm),mimetype="application/json")
    else:
        response = "Failed UUID not found"
        return return_status(response,404)

@app.route('/vm_ip/<uuid>/<ip>', methods = ['GET'])
def change_ip_vm(uuid,ip):
    global vm_pool
    vm = vm_pool.get(int(uuid))
    if vm != None:
        if vm.setIP(str(ip)):
            response = "Successful change of ip"
            return return_status(response,202)
        else:
            response = "Failed to change ip. Bad Formatted"
            return return_status(response,406)
    else:
        response = "Failed to change ip. UUID not found"
        return return_status(response,404)

@app.route('/register_vm/<uuid>', methods = ['GET'])
def register_vm(uuid):
    global vm_pool
    uuid = int(uuid)
    vm = vm_pool.get(uuid)
    if vm == None:
        vm_pool[uuid] = VM()
        vm_pool.get(uuid).setUuid(uuid)
        for i in vm_pool.keys():
            print("["+str(i)+"] : "+str(vm_pool.get(i)) +'\n')
        return return_status("Máquina registrada", 200)
    else:
        return return_status("Máquina ya existente", 304)

def return_status(message, code):
    if code >= 200 and code < 300:
        success =  True
    else:
        success =  False
    response = {'success' : success,
                'code' : code,
                'message' : message}
    return jsonify(response);

if __name__ == '__main__':
    app.run()
