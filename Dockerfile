FROM tiangolo/uwsgi-nginx-flask:python3.7

ARG db_url

COPY . ProyectoIV

WORKDIR ProyectoIV

RUN pip install -r requirements.txt

ENV FLASK_APP=main.py
ENV PORT=5000
ENV DATABASE_URL=$db_url
EXPOSE $PORT/tcp

ENTRYPOINT [ "gunicorn" ]

# CMD [ "sh", "-c", "flask run -p $PORT" ]
CMD [ "main:app" ]
