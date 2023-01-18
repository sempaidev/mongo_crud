# API en FASTAPI con MONGO en docker

Ejemplo de un api rest en contenedores usando la tecnologia de fastapi y mongodb. 


## Tecnologías

* docker-compose
* docker
* python 3.8
* fastapi
* mongodb

### Docker:
Docker es una plataforma que nos permite empaquetar software en unidades estandarizadas llamadas contenedores, que incluyen todo lo necesario para que el software se ejecute, incluyendo bibliotecas, herramientas de sistema, código y tiempo de ejecución.
### docker-compose:
Docker-compose es una herramienta que nos permite definir entornos multi-contenedor. En nuestro archivo docker-compose.yaml podemos indicar la configuración de nuestro despliegue y con un simple comando, levantamos toda la infraestructura.

## Instalación

* Clone el proyecto 
```git clone https://github.com/sempaidev/mongo_crud.git ```
* Muévase dentro del directorio por consola o terminal
```cd mongo_crud```
* Compile las imagenes 
```docker-compose build```
* Corra el proyecto 
```docker-compose up -d```

Puede probar los metodos del proyecto accediento a la ruta 
```http://<ip>:90/docs``` 
remplaze <ip> por el ip de su maquina o servidor