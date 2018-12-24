import flask
from src.db import app, db
from flask import jsonify, Response, request
from src.vm import VM

import json, signal, sys

def get_vm(uuid):
    return VM.query.get(int(uuid))

def add_vm(vm):
    global vm_pool
    if VM.query.filter(VM.uuid==vm.getUuid()).count() != 0:
        return False
    else:
        db.session.add(vm)
        db.session.commit()
        return True

def delete_vm(uuid):
    if VM.query.filter(VM.uuid==uuid).count() != 0:
        obj = VM.query.filter(VM.uuid==uuid).first()
        db.session.delete(obj)
        db.session.commit()
        return True
    else:
        return False

@app.route('/', methods = ['GET'])
def status():
    response =  {"status" : "OK"}
    return jsonify(response);

@app.route('/status', methods = ['GET'])
def status_vm():
    vm_pool = VM.query.all()
    num_vm_alive = 0
    ram_used = 0
    total_vcpu = 0
    vcpu_in_use = 0
    ram_in_use = 0
    uuids = []
    for i in vm_pool:
        uuids.append(i.getUuid())
        ram_used += i.getRAM()
        total_vcpu += i.getVCPU()
        if(i.isAlive()):
            num_vm_alive += 1
            vcpu_in_use += i.getVCPU()
            ram_in_use += i.getRAM()

    response =  {"status" : "OK",
                 "vm_pool_status" :
                    {
                     "total_vm"     : len(vm_pool),
                     "VMs_alive"    : num_vm_alive,
                     "total_ram"    : ram_used,
                     "total_vcpu"   : total_vcpu,
                     "in_use_ram"   : ram_in_use,
                     "in_use_vcpu"  : vcpu_in_use,
                     "vm_UUIDs"     : uuids
                     }
                 }
    return jsonify(response);

@app.route('/vm/<uuid>', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def serve_vm(uuid):
    if flask.request.method == 'GET':
        vm = get_vm(uuid)
        if vm != None:
            respones = str(vm)
            return Response(respones,mimetype="application/json")
        else:
            response = "Failed VM not found"
            return return_status(response,404)
    elif flask.request.method == 'PUT':
        return register_vm(int(uuid))
    elif flask.request.method == 'POST':
        vm = get_vm(uuid)
        if vm != None:
            state={
                'ip'     : request.form.get('ip'),
                'vcpu'   : request.form.get('vcpu'),
                'nombre' : request.form.get('nombre'),
                'mac'    : request.form.get('mac'),
                'alive'  : request.form.get('alive'),
                'ram'    : request.form.get('ram'),
                'vmdsk'  : request.form.get('vmdsk')
            }
            return edit_vm(vm,state)
        else:
            response = "Failed VM not found"
            return return_status(response,404)
    elif flask.request.method == 'DELETE':
        if delete_vm(uuid):
            return return_status('Máquina borrada correctamente',200)
        else:
            response = "Failed VM not found"
            return return_status(response,404)

@app.route('/vm/<uuid>/<resource>', methods = ['GET'])
def serve_vm_resource(uuid, resource):
    vm = get_vm(uuid)
    if vm != None:
        resource = str(resource).lower()
        response = {}
        if resource == 'ip':
            response['ip'] = vm.getIP()
        elif resource == 'vcpu':
            response['vcpu'] = vm.getVCPU()
        elif resource == 'nombre':
            response['nombre'] = vm.getNombre()
        elif resource == 'mac':
            response['mac'] = vm.getMAC()
        elif resource == 'isalive':
            response['alive'] = vm.isAlive()
        elif resource == 'ram':
            response['ram'] = vm.getRAM()
        elif resource == 'vmdsk':
            response['vmdsk'] = vm.getVmdsk()
        else:
            return return_status('Resource not found',404)

        response['success'] = True
        return jsonify(response)
    else:
        response = "Failed VM not found"
        return return_status(response,404)

def edit_vm(vm,state):
    if vm != None:
        response = []
        errors = []
        if(state.get('ip')):
            if vm.setIP(str(state.get('ip'))):
                response.append("Successful change of ip")
            else:
                errors.append("Failed to change ip. Bad Formatted")

        elif(state.get('nombre')):
            if vm.setNombre(str(state.get('nombre'))):
                response.append("Successful change of nombre")
            else:
                errors.append("Failed to change Nombre. Empty")

        elif(state.get('mac')):
            if vm.setNombre(str(state.get('mac'))):
                response.append("Successful change of MAC")
            else:
                errors.append("Failed to change MAC. Bad Formatted")

        elif(state.get('alive')):
            if vm.setAlive(state.get('alive')):
                response.append("Successful change of Alive State")
            else:
                errors.append("Failed to change Alive State. Boolean only")

        elif(state.get('vcpu')):
            if vm.setVCPU(state.get('vcpu')):
                response.append("Successful change of VCPU")
            else:
                errors.append("Failed to change VCPU. Only integer positive")

        elif(state.get('ram')):
            if vm.setRAM(state.get('ram')):
                response.append("Successful change of RAM")
            else:
                errors.append("Failed to change RAM. Only integer positive")

        elif(state.get('vmdsk')):
            if vm.setVmdsk(str(state.get('vmdsk'))):
                response.append("Successful change of VMDSK path")
            else:
                errors.append("Failed to change VMDSK path. VMDSK path not accesible")

        else:
            errors.append("Bad URL")

        db.session.commit()
        res = {}
        res['success'] = True if len(errors) == 0 else False
        res['messages'] = list(response)
        if len(errors) != 0:
            res['errors'] = list(errors)
        return jsonify(res)
    else:
        response = "Failed to change ip. UUID not found"
        return return_status(response,404)

def register_vm(uuid):
    uuid = int(uuid)
    vm = get_vm(uuid)
    if vm == None:
        vm = VM()
        vm.setUuid(uuid)
        add_vm(vm)
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
    app.run(host='0.0.0.0',debug=True)
