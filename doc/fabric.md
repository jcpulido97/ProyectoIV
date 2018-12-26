# Fabric (Despliegue)

Para realizar el despliegue del microservicio hemos usado [Fabric](https://get.fabric.io/)

Deberemos crear un archivo fabfile que contiene todo el proceso que debe seguirse para correr nuestra aplicación

*fabfile.py*

```python
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
```

Deberemos de crear un archivo de configuración para ssh de forma que fabric sepa como debe conectarse a la máquina, con qué usuario y clave privada. **(~/.ssh/config)**

```
ServerAliveInterval 30

# Staging
Host ubuntu
        HostName 192.168.0.5
        User ubuntu
        IdentityFile ~/.ssh/id_rsa

# Producción
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
$ fab staging update_app   # Actualizaría el docker en las máquinas de staging
$ fab production dock_down # Apagaría nuestro docker en las máquinas de producción
```

> Ejemplo de fab production dock_up

![Fabric](https://github.com/jcpulido97/ProyectoIV/blob/master/doc/img/fabric.PNG?raw=true)