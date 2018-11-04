# Despliegue de aplicación en Heroku

Vamos a realizar un despliegue de nuestra aplicación en la plataforma como servicio de [heroku](https://www.heroku.com/)

## 1. Creación y enlazado de heroku con github

1. Registrarse con una cuenta
2. Crear una nueva aplicación

![1541355682840](https://raw.githubusercontent.com/jcpulido97/ProyectoIV/master/doc/img/1541355682840.png)

3. Elegir un nombre válido que nos servirá como enlace al despliegue final de la aplicación

![1541355756485](https://raw.githubusercontent.com/jcpulido97/ProyectoIV/master/doc/img/1541355756485.png)

4. Enlazar nuestra aplicación con nuestro repositorio GitHub

![1541355799125](https://raw.githubusercontent.com/jcpulido97/ProyectoIV/master/doc/img/1541355799125.png)

![1541355860801](https://raw.githubusercontent.com/jcpulido97/ProyectoIV/master/doc/img/1541355860801.png)

5. Por último activamos la opción de "Automatic Deploys" y marcamos también "Wait for CI to pass before deploy" ya que tenemos activado Travis como servicio que pasa los tests de forma automática.

![1541355952180](https://raw.githubusercontent.com/jcpulido97/ProyectoIV/master/doc/img/1541355952180.png)

**Con esto ya tendremos nuestra aplicación configurada en heroku, solo nos queda añadir unos archivos a nuestro proyecto.**



## 2. Adaptación del proyecto para ejecución en heroku

Para ejecutar flask en heroku hace falta el uso de una dependencia llamada gunicorn así que la añadiremos a nuestro archivo requirements,txt. De tal forma que quedará asi:

```
pytest>=3.8.2
Flask==1.0.2
gunicorn>=19.9.0
```

Seguimos con la forma de decir a Heroku como ejecutar la aplicación. En mi caso como utilizo Python debo añadir un archivo llamado: Procfile con el siguiente contenido

```
web: gunicorn main:app
```

Con este archivo Heroku sabrá como debe de ejecutar mi aplicación, es decir ejecutando el comando gunicorn con el parámetro "main:app". En mi caso mi proyecto consta de un archivo main.py que es donde se ejecuta todo lo relacionado con Flask y donde se ejecuta el app.run(), que se encarga de empezar la ejecución de los servicios de enrutamiento para la API REST.

**Y con esto ya tendremos nuestra aplicación en la nube con integración continua.**

Podremos acceder a ella mediante el siguiente enlace: *https://<nombre-de-la-app>.herokuapp.com/*

## 3.Comprobación del funcionamiento

Gracias a que hemos añadido la ruta / en nuestra aplicación para que devuelva el status, podremos comprobar si ésta se encuentra online o no en la URL que se nos proporciona en el dashboard heroku.

```bash
$curl https://vm-management-tool.herokuapp.com/
{"status":"OK"}
```

Si hemos añadido el /status correctamente podremos ver si la aplicación se ha ejecutado y configurado bien en su totalidad y que no nos indique solo si está ejecutando.

```bash
$ curl  https://vm-management-tool.herokuapp.com/status
{
 "status":"OK",
 "vm_pool_status":
    {
     "VMs_alive":1,
     "in_use_ram":8192,
     "in_use_vcpu":8,
     "total_ram":12288,
     "total_vcpu":12,
     "total_vm":2,
     "vm_UUIDs":[2566,6311]
    }
 }

```

