# Docker

Creamos el dockerfile de nuestra aplicación

```dockerfile
FROM tiangolo/uwsgi-nginx-flask:python3.7

RUN git clone https://github.com/jcpulido97/ProyectoIV.git

WORKDIR ProyectoIV

RUN pip install -r requirements.txt

ENV FLASK_APP=main.py
ENV PORT=5000         # Puerto por defecto 5000 aunque heroku lo sobreescribirá
EXPOSE $PORT/tcp

ENTRYPOINT [ "gunicorn" ]

CMD [ "main:app" ]
```

He usado un docker preparado para desplegar aplicaciones Flask de Python, por lo que único que debemos hacer es descargar nuestras dependencias y ejecutar gunicorn. Del resto del proceso ya se encarga la imagen ya preparada.

## Despliegue en Heroku

Instalamos el cliente de Heroku en nuestra terminal como indica la web oficial [aquí](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)

```bash
$ heroku login
# Se nos pedirá nuestro usuario y contraseña
```

Después indicamos que queremos iniciar en el modo para contenedores

```bash
$ heroku container:login
```

Tras esto creo una nueva aplicación en Heroku 

```bash
$ heroku create
Creating pacific-shore-31497... done, stack is cedar-14
https://pacific-shore-31497.herokuapp.com/
```

hacemos un push del contenedor a la app que se nos ha proporcionado en el comando anterior:

```bash
$ heroku container:push web --app pacific-shore-31497
```

Una vez está subido publicamos la app:

```bash
$ heroku container:release web --app pacific-shore-31497
```

Ya tendríamos nuestro docker desplegado en la url que se nos ha proporcionado en al crear la aplicación o 

también podemos hacer:

```bash
$ heroku open	#Se nos abrirá la web de la aplicación en nuestro navegador 
```

---

Podéis ver que mi docker está desplegado [aquí](https://pacific-shore-31497.herokuapp.com/status)

![Despliegue docker](https://raw.githubusercontent.com/jcpulido97/ProyectoIV/master/doc/img/despliegue_docker.PNG)

