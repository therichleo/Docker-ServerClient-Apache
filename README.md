# Comunicación Cliente-Servidor con Docker usando HTTP y Apache
## 📌Descripcion:
Este proyecto demuestra una arquitectura cliente-servidor simple utilizando el protocolo HTTP. Consta de dos contenedores Docker, ejecutados en distintas máquinas (PC 1 y PC 2), donde:
- Servidor (PC 1): Este PC aloja un servidor HTTP apache que sirve una carpeta HTML la cual contiene un 'index.html' dentro.
- Cliente (PC 2): Actua como cliente, realizando una peticion GET mediante un script en Python 'cliente.py' al servidor alojado en el PC 1.
- 
