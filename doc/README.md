# Documentación de Proyecto

Este proyecto trata sobre un microservicio para la gestión de máquinas virtuales para un posterior
sistema más complejo.

#### Documentación hitos:

- [Hito #1](https://github.com/jcpulido97/ProyectoIV/tree/master/doc/ClaseVM.md)
- Hito #2 (Más abajo)
- [Hito #3](https://github.com/jcpulido97/ProyectoIV/tree/master/doc/heroku.md)
- [Hito #4](https://github.com/jcpulido97/ProyectoIV/tree/master/doc/docker.md)



#### Explicación del por qué del uso de cada herramienta

- [Flask](http://flask.pocoo.org/) como micro-framework web.
  - Se usa debido a su rapidez y sencillez a la hora de la creación de aplicaciones web. Por tanto es óptimo para la creación de muchos microservicios como puede pasar en este sistema
- [Travis-CI](https://travis-ci.org) como sistema de integración continua.
  - Servicio Web gratuito que provee de capacidades de ejecutar tests en repositorios alojados en Github de una forma fácil y sin complicaciones
- [MariaDB](https://github.com/MariaDB/server) como gestor de base de datos.
  - Getor de base de datos de código abierto, altamente conocido y testeado. Creado a partir de un fork al gestor de base de datos MySQL cuando fue comprado por ORACLE. Usado debido a su condición gratuita y a su gran comunidad que puede facilitar la solución de las distintas situaciones
- [Docker](https://github.com/docker/cli) como software de aislamiento de los microservicios.
  - Gestor de contenedores docker que provee de una capa de aislamiento de los procesos con la máquina host. Usado debido a su capacidad de gestionar los contenedores para que sean especificamente configurados para el servicio que vayan dar
  - [DockerHub](https://hub.docker.com/) como repositorio de contenedores online.
  - [Guía de despliegue docker en heroku](https://github.com/jcpulido97/ProyectoIV/tree/master/doc/docker.md)
- [Heroku](https://www.heroku.com/) como plataforma como servicio (PaaS) para integración continua
  - Plataforma como servicio de computación en la Nube que soporta distintos lenguajes de programación
  - [Guía de como configurar una aplicación en heroku](https://github.com/jcpulido97/ProyectoIV/tree/master/doc/heroku.md)

