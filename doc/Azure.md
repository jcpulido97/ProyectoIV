# Despliegue final Azure

## Infraestructura como servicio IAAS

Para este caso se ha utilizado la plataforma de Microsoft, Azure ya que es la que se nos ha suministrado para la clase. En mi opinión no creo que sea la mejor plataforma ya que su interfaz web puede llegar a ser bastante tediosa y poco clara, gracias a Vagrant nos podemos librar de este obstáculo. 

El hecho de configurar Vagrant para que se pueda comunicar con Azure sigue siendo poco pulido por lo que puede llevar a malas experiencias y perdida de tiempo para solucionar errores poco conocidos.



## Sistema Operativo

He usado **Ubuntu 16.0.4** ya que es un sistema con bastante soporte que está muy bien documentado por la comunidad, lo que supone que si en algún momento nos encontramos con algún error o algún programa de terceros, es bastante probable que alguien ya haya pasado por el mismo camino y haya preparado alguna solución para los demás.

Probé intentar usar **CentOS** pero había algunos paquetes de software que no eran fáciles de descargar y tenías que compilarlos tu mismo, lo que podía ocasionar muchos más problemas a largo plazo.



## Docker

Se usa el sistema de contenedores Docker ampliamente utilizado en este mundo ya que asegura que lo que se ejecute, se haga siempre en las mismas condiciones previamente definidas, para evitar mayormente problemas de dependencias, configuraciones, etc.



## Gestor de base de datos

Intenté usar las bases de datos que provee Azure ya que son fáciles de instalar,  ya que no debemos de hacer nada y fáciles de configurar. Pero como el gestor de base de datos que ofrecen es Microsoft SQL, no tiene soporte por la librería SQLAlchemy y por tanto haciendo imposible conectarse con la aplicación

Finalmente se ha usado un usual servidor MySQL llamado Mariadb que tiene amplio soporte por la librería SQLAlchemy de python.



### Pasos del despliegue:

1. [Creación de Vagrantfile y configuración de Vagrant](https://github.com/jcpulido97/ProyectoIV/tree/master/doc/Vagrant.md)
2. [Provisionamiento de la máquina con Ansible](https://github.com/jcpulido97/ProyectoIV/tree/master/doc/Ansible.md)
3. [Despliegue de aplicación con Fabric](https://github.com/jcpulido97/ProyectoIV/tree/master/doc/fabric.md)