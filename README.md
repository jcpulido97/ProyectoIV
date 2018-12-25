# ProyectoIV - Gestión de Máquinas Virtuales

[![Build Status](https://travis-ci.org/jcpulido97/ProyectoIV.svg?branch=master)](https://travis-ci.org/jcpulido97/ProyectoIV)

![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)

​	Esta aplicación tiene como objetivo la gestión de máquinas virtuales para una futura integración con un sistema más complejo. 

​	La clase [VM](https://github.com/jcpulido97/ProyectoIV/blob/master/src/vm.py) contiene toda la información en lo que se refiere a las máquinas virtuales que serán almacenadas/usadas por el sistema, por tanto será la clase testeada (por [VMtest.py](https://github.com/jcpulido97/ProyectoIV/blob/master/test/VMtest.py)) de forma profunda para asegurar el completo y correcto funcionamiento del elemento central del proyecto.

Despliegue de la aplicación: https://vm-management-tool.herokuapp.com/

Contenedor: https://pacific-shore-31497.herokuapp.com/

Despliegue dockerhub: https://hub.docker.com/r/kronos483/proyectoiv/ 

Despliegue final: 137.116.185.97

**Para más información acceder a la [documentación](https://github.com/jcpulido97/ProyectoIV/tree/master/doc) del proyecto.**

[Despliegue final en Azure](https://github.com/jcpulido97/ProyectoIV/tree/master/doc/Azure.md)

#### Filosofía de diseño

​	Se presentará al usuario con una API REST de forma que se consiga una aplicación modularizada y autosuficiente para su posible integración en un sistema más complejo. Obviamente se hará uso de un estilo de programación orientado a objetos debido a los beneficios que este tipo de diseño conlleva.

En este servicio se podrán realizar las siguientes acciones:

- Registrar Máquina Virtual (VM)
- Pedir información de una VM
- Eliminar una VM ya registrada
- Editar Información sobre la VM



### Tests

```bash
$ pip install -r requirements.txt # Para instalar las dependencias
```

Ejemplo de ejecución

```bash
vagrant@vagrant:/vagrant/ProyectoIV$ pytest test/VMtest.py test/APItest.py
============================= test session starts ==============================
platform linux -- Python 3.6.5, pytest-3.8.2, py-1.6.0, pluggy-0.7.1
rootdir: /vagrant/ProyectoIV, inifile:
collected 20 items

test/VMtest.py ..........                                                [ 76%]
test/APItest.py ...                                                      [100%]

========================== 13 passed in 4.19 seconds ===========================
```



## Herramientas a utilizar

- [Python](https://github.com/python/cpython) como lenguaje de programación.
  - [Flask](http://flask.pocoo.org/) como micro-framework web.
- [Travis-CI](https://travis-ci.org) como sistema de integración continua.
- [Heroku](https://www.heroku.com/) como plataforma como servicio (PaaS) para integración continua
  - [Guía de como configurar una aplicación en heroku](https://github.com/jcpulido97/ProyectoIV/tree/master/doc/heroku.md)
- [Docker](https://github.com/docker/cli) como software de aislamiento de los microservicios
  - [Guía de despliegue docker en heroku](https://github.com/jcpulido97/ProyectoIV/tree/master/doc/docker.md)
- [DockerHub](https://hub.docker.com/) como repositorio de contenedores online.
- [Vagrant](https://www.vagrantup.com/) para orquestación
- [Ansible](https://www.ansible.com/) para provisionamiento
- [Fabric](https://fabric.io/) para despliegue
