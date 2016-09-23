FROM nginx
COPY app/requirements.txt /requirements.txt
RUN apt-get update -y && apt-get install python-dev python-pip -y && pip install -r requirements.txt 
EXPOSE 8000
WORKDIR /app
ENTRYPOINT [ "gunicorn","--bind", "0.0.0.0:8000", "wsgi"] 
COPY app /app
