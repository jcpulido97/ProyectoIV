# ProyectoIV - Gestión de Máquinas Virtuales

![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)

​	Esta aplicación tiene como objetivo la gestión de máquinas virtuales para una futura integración con un sistema más complejo.

#### Filosofía de diseño

​	Se presentará al usuario con una API REST de forma que se consiga una aplicación modularizada y autosuficiente para su posible integración en un sistema más complejo. Obviamente se hará uso de un estilo de programación orientado a objetos debido a los beneficios que este tipo de diseño conlleva.

En este servicio se podrán realizar las siguientes acciones:

- Registrar Máquina Virtual (VM)

- Pedir información de una VM

- Eliminar una VM ya registrada

- Editar Información sobre la VM


## Herramientas a utilizar

- [Python](https://github.com/python/cpython) como lenguaje de programación.
  - [Flask](http://flask.pocoo.org/) como micro-framework web.
- [MariaDB](https://github.com/MariaDB/server) como gestor de base de datos.
- [Docker](https://github.com/docker/cli) como software de aislamiento de los microservicios.

