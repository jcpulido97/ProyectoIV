# coding=utf-8
from os import environ
from fabric.api import *
import os
# Usamos la configuración del archivo hosts de SSH.
env.use_ssh_config = True

# Máquina de staging.
def staging():
    env.hosts = ['ubuntu']

# Máquina de producción.
def production():
    env.hosts = ['vm_management']

# Iniciar el contenedor con el microservicio.
def deploy():
    run('docker pull kronos483/proyectoiv:latest')
	if "DATABASE_URL" in os.environ:
		run('docker run -d -p 80:5000 -e DATABASE_URL=$DATABASE_URL -t kronos483/proyectoiv:latest')
	elif os.path.isfile('/home/vagrant/dbpass'):
		run('source /home/vagrant/dbpass && docker run -d -p 80:5000 -e DATABASE_URL=$DATABASE_URL -t kronos483/proyectoiv:latest')
	else:
		raise SystemExit('DATABASE_URL not provided')

# Parar contenedor con el microservicio.
def stop():
    run('docker stop $(docker ps -a -q)')
    run('docker system prune -f')
