# Fabric (Despliegue)

Para realizar el despliegue del microservicio hemos usado [Fabric](https://get.fabric.io/), una herramienta que se puede usar como librería o como CLI.

Deberemos crear un archivo fabfile que contiene todo el proceso que debe seguirse para correr nuestra aplicación

*fabfile.py*

```python
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
```

Deberemos de crear un archivo de configuración para ssh de forma que fabric sepa como debe conectarse a la máquina, con qué usuario y clave privada. **(~/.ssh/config)**

```
ServerAliveInterval 30

# Máquina de staging
Host ubuntu
        HostName 192.168.56.105
        User ubuntu
        IdentityFile ~/.ssh/id_rsa

# Máquina de producción
Host vm_management
        HostName 137.116.185.97
        User vagrant
        IdentityFile ~/.ssh/id_rsa
```

El uso de fabric es el siguiente:

```bash
$ fab <host> [comandos]
```

Donde los comandos son cada uno de los métodos definidos en el fabfile. Por ejemplo:

```bash
$ fab production dock_up   # Ejecutaría nuestro docker en las máquinas de producción
$ fab stagin update_app    # Actualizaría el docker en las máquinas de staging
$ fab production dock_down # Apagaría nuestro docker en las máquinas de producción
```

> Ejemplo de fab production dock_up

![Fabric](https://github.com/jcpulido97/ProyectoIV/blob/master/doc/img/fabric.PNG?raw=true)