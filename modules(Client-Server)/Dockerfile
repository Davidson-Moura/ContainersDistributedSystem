FROM python:latest

WORKDIR ./

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 15740

CMD ["python", "./module.py"]

# Contruir container
# docker build -t module .

# Criar rede
# docker network create rede_modules

# Iniciar
# MY_PORT = porta do container
# PORTS = porta dos containers que pode se comunicar

# docker run -p 15741:15740 --net=rede_modules -e MY_PORT=15740 PORTS="[15741,15742,15743,15744]" module

# docker run -it -p 15741:15740 --rm --name=container1 --net=rede_modules -e MY_PORT=15741 -e PORTS="[15742,15744]" module
# docker run -it -p 15742:15740 --rm --name=container2 --net=rede_modules -e MY_PORT=15742 -e PORTS="[15741,15743]" module
# docker run -it -p 15743:15740 --rm --name=container3 --net=rede_modules -e MY_PORT=15743 -e PORTS="[15742,15744]" module
# docker run -it -p 15744:15740 --rm --name=container4 --net=rede_modules -e MY_PORT=15744 -e PORTS="[15741,15743]" module