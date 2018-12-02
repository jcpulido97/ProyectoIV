FROM tiangolo/uwsgi-nginx-flask:python3.7

# We copy just the requirements.txt first to leverage Docker cache
# RUN git clone https://github.com/jcpulido97/ProyectoIV.git

# RUN git pull origin docker

COPY . ProyectoIV

WORKDIR ProyectoIV

RUN pip install -r requirements.txt

ENV FLASK_APP=main.py
ENV PORT=5000
EXPOSE $PORT/tcp

ENTRYPOINT [ "gunicorn" ]

# CMD [ "sh", "-c", "flask run -p $PORT" ]
CMD [ "main:app" ]
