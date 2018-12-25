from fabric.api import *

# Uso la configuración de hosts de SSH.
env.use_ssh_config = True

# Defino la máquina de staging.
def staging():
    env.hosts = ['ubuntu']

# Defino la máquina de producción.
def production():
    env.hosts = ['vm_management']

# Iniciar el contenedor con el microservicio.
def app_up():
    run('docker run -p 5000:5000 -e DATABASE_URL=$DATABASE_URL -it kronos483/proyectoiv:latest')

# Parar contenedor con el microservicio.
def app_down():
    run('docker stop vm')

# Cambiar permisos del socker de Docker.
def dockersock():
    run('sudo chown vagrant:docker /var/run/docker.sock')

# Docker prune, para limpiar contenedores antiguos.
def dockerprune():
    run('docker system prune -f')

# Docker images, para consultar las imágenes existentes.
def dockerimages():
    run('docker images')

# Docker ps, para consultar los contenedores en ejecución.
def dockerps():
    run('docker ps')

# Descarga del contenedor.
def update_app():
    run('docker pull kronos483/proyectoiv:latest')

# Iniciar microservicio.
# 1. Cambio permisos socket.
# 2. Ejecuto docker prune.
# 3. Arranco el contenedor.
def dock_up():
    execute(dockersock)
    execute(dockerprune)
    execute(app_up)

# Apago el microservicio.
def dock_down():
    execute(app_down)
