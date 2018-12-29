# coding=utf-8
from fabric.api import *

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
    run('source /home/vagrant/dbpass && docker run -d -p 80:5000 -e DATABASE_URL=$DATABASE_URL -t kronos483/proyectoiv:latest')

# Parar contenedor con el microservicio.
def stop():
    run('docker stop $(docker ps -a -q)')
    run('docker system prune -f')
