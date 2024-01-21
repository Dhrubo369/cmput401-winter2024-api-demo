# Ready-To-Deploy Django, gunicorn, NGINX, Docker Application
Getting a Django 4.2 app up in no time. In this project, gunicorn is used as a WSGI. NGINX is used as a reverse proxy server.

## Credit
This repository is modified from the code created by [Watt Iamsuri](https://github.com/wiamsuri/django-gunicorn-nginx-docker).

## For Development
In the root level of this repository, copy the file named `django.env.example` to `django.env` and adjust file variables
```
cp django.env.example django.env
```

Build and run the container
```
docker compose up --build
```

## Installing Docker
Here are the commands to install Docker. After running these commands, exit from ssh and reconnect to the instance.

For Ubuntu
```
sudo curl -sSL https://get.docker.com/ | sh
sudo usermod -a -G docker $(whoami)
sudo service docker start
```
