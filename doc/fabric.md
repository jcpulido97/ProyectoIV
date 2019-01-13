# Fabric (Despliegue)

Para realizar el despliegue del microservicio hemos usado [Fabric](https://get.fabric.io/)

Deberemos crear un archivo fabfile que contiene todo el proceso que debe seguirse para correr nuestra aplicación

*fabfile.py*

```python
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
$ fab production deploy   # Ejecutaría nuestro docker en las máquinas de producción
$ fab staging deploy   # Ejecutaría el docker en las máquinas de staging
$ fab production stop # Apagaría nuestro docker en las máquinas de producción
```

> Ejemplo de fab production deploy

![deploy](https://github.com/jcpulido97/ProyectoIV/blob/master/doc/img/deploy.PNG?raw=true)

> Ejemplo de fab production stop

![stop](https://github.com/jcpulido97/ProyectoIV/blob/master/doc/img/stop.PNG?raw=true)



##### Referencias

- https://stackoverflow.com/questions/3077281/connecting-to-a-host-listed-in-ssh-config-when-using-fabric
- http://docs.fabfile.org/en/1.14/usage/fab.html
- https://stackoverflow.com/questions/2326797/how-to-set-target-hosts-in-fabric-file

### 