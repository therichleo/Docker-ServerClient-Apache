# Comunicación Cliente-Servidor con Docker usando HTTP y Apache
## 📌Descripcion:
Este proyecto demuestra una arquitectura cliente-servidor simple utilizando el protocolo HTTP. Consta de dos contenedores Docker, ejecutados en distintas máquinas (PC 1 y PC 2), donde:
- Servidor (PC 1): Este PC aloja un servidor HTTP apache que sirve una carpeta HTML la cual contiene un 'index.html' dentro.
- Cliente (PC 2): Actua como cliente, realizando una peticion GET mediante un script en Python 'cliente.py' al servidor alojado en el PC 1.
## 🌐 ¿Qué es HTTP?
HTTP (HyperText Transfer Protocol) es un protocolo de red utilizado para transferir información en la web. Funciona bajo un modelo cliente-servidor:
- El cliente envía una solicitud (por ejemplo, un navegador o un script Python).
- El servidor responde con los recursos solicitados (como una página HTML).
## 🧱 ¿Qué es Apache?
Apache HTTP Server es uno de los servidores web más utilizados. Su función es recibir solicitudes HTTP y devolver contenido web como HTML, imágenes o datos. En este proyecto, Apache está contenido en un contenedor Docker y sirve el archivo index.html.
## 🐳 Arquitectura del Proyecto
```
+-------------+       HTTP GET       +-----------+
|    PC 2     |  ------------------> |   PC 1    |
|  Cliente    |                      | Servidor  |
| Dockerfile  |                      | Dockerfile|
| cliente.py  |                      |  Apache   |
|             |                      | index.html|
+-------------+      Respuesta       +-----------+
```
## 🛠️ Configuración
### PC 1 (Servidor HTTP con Apache):
#### Dockerfile:
```
FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y apache2 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /var/www/html

COPY html/ /var/www/html/

EXPOSE 80

CMD ["apachectl", "-D", "FOREGROUND"]
```
#### index.html:
```
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Hola Mundo</title>
</head>
<body>
    <h1>Hola Mundo</h1>
</body>
</html>
```
### COMANDOS PARA EJECUTAR:
```
sudo docker build -t apacheserver .
sudo docker run -d --name httpserver -p 8080:80 apacheserver
```
### PC 2 (Cliente HTTP en Python):
#### Dockerfile:
```
FROM python:3.11-slim

WORKDIR /app

COPY cliente.py .

RUN python -m  pip install urllib3

CMD ["python", "cliente.py"]
```
#### cliente.py:
```
import urllib3

http = urllib3.PoolManager()
response = http.request('GET', 'http://192.168.92.129:8080/')

print("Status:", response.status)
print("Response data:", response.data.decode('utf-8'))
```

