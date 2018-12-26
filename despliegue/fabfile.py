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
def app_up():
    run('docker run --name vm -p 80:5000 -e DATABASE_URL=$DATABASE_URL -it kronos483/proyectoiv:latest')

# Parar contenedor con el microservicio.
def app_down():
    run('docker stop $(docker ps -a -q)')

# Permisos del socket de Docker.
def dockersock():
    run('sudo chown vagrant:docker /var/run/docker.sock')

# Docker prune, para limpiar contenedores antiguos.
def dockerprune():
    run('docker system prune -f')

# Descarga del contenedor.
def update_app():
    run('docker pull kronos483/proyectoiv:latest')

# Iniciar microservicio.
def dock_up():
    execute(dockersock)
    execute(dockerprune)
    execute(app_up)

# Parar el microservicio.
def dock_down():
    execute(app_down)
