# Documentación de Proyecto

Este proyecto trata sobre un microservicio para la gestión de máquinas virtuales para un posterior
sistema más complejo

A continuación se va

- [Flask](http://flask.pocoo.org/) como micro-framework web.
  - Se usa debido a su rapidez y sencillez a la hora de la creación de aplicaciones web. Por tanto es óptimo para la creación de muchos microservicios como puede pasar en este sistema
- [Travis-CI](https://travis-ci.org) como sistema de integración continua.
  - Servicio Web gratuito que provee de capacidades de ejecutar tests en repositorios alojados en Github de una forma fácil y sin complicaciones
- [MariaDB](https://github.com/MariaDB/server) como gestor de base de datos.
  - Getor de base de datos de código abierto, altamente conocido y testeado. Creado a partir de un fork al gestor de base de datos MySQL cuando fue comprado por ORACLE. Usado debido a su condición gratuita y a su gran comunidad que puede facilitar la solución de las distintas situaciones
- [Docker](https://github.com/docker/cli) como software de aislamiento de los microservicios.
  - Gestor de contenedores docker que provee de una capa de aislamiento de los procesos con la máquina host. Usado debido a su capacidad de gestionar los contenedores para que sean especificamente configurados para el servicio que vayan dar

## Clase VM

Atributos miembro:

| Variable                                                    |    Tipo     | Valor por defecto |
| ----------------------------------------------------------- | :---------: | :---------------: |
| nombre                                                      | **String**  |       Vacío       |
| vcpu                                                        |  **int **   |        -1         |
| ram                                                         |   **int**   |         0         |
| uuid                                                        |   **int**   |         0         |
| ip                                                          | **String**  |       Vacío       |
| vmdsk (Path a la iso de la máquina virtual)                 | **String**  |       Vacío       |
| mac_address                                                 | **String**  |       Vacío       |
| alive                                                       | **Boolean** |       False       |
| date_created (Fecha indicada en formato epoch, estilo Unix) |  **float**  |    time.time()    |

Como regla general todos los atributos son accedidos mediante sus respectivos métodos **set** y **get**. Generalmente los métodos set devolverán **True** siempre y cuando el valor haya sido cambiado y **False** en caso contrario.

![UML VM](https://raw.githubusercontent.com/jcpulido97/ProyectoIV/master/doc/VM.png)





