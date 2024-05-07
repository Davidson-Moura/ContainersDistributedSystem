# Modulos distribuídos (modules(Client-Server))

## Contruir container

- Dentro da pasta modules(Client-Server)
- docker build -t module .

## Criar rede

- docker network create rede_modules

## Iniciar

MY_PORT = porta do container
PORTS = porta dos containers que pode se comunicar

### Iniciar 4 containers

- docker run -it -p 15741:15740 --rm --name=container1 --net=rede_modules -e MY_PORT=15741 -e PORTS="[15742,15744]" module
- docker run -it -p 15742:15740 --rm --name=container2 --net=rede_modules -e MY_PORT=15742 -e PORTS="[15741,15743]" module
- docker run -it -p 15743:15740 --rm --name=container3 --net=rede_modules -e MY_PORT=15743 -e PORTS="[15742,15744]" module
- docker run -it -p 15744:15740 --rm --name=container4 --net=rede_modules -e MY_PORT=15744 -e PORTS="[15741,15743]" module

# Utilitários para testar os containers (Utils)

## Adicionar a cada 10 segundos (addCounter)

- Dentro da pasta Utils/addCounter
- docker build -t addcounter .
- docker run --net=rede_modules -it addcounter

## Exibir contador de todos os containers a cada 3 segundos (addCounter)

- Dentro da pasta Utils/observerCounter
- docker build -t observercounter .
- docker run --net=rede_modules -it observercounter
