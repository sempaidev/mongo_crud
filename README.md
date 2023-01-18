# API en FASTAPI con MONGO en docker

Ejemplo de un api rest en contenedores usando la tecnologia de fastapi y mongodb. 


## Tecnologías

* docker-compose
* docker
* python 3.8
* fastapi
* mongodb

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
```http://<ip>:90/docs``` remplaze <ip> por el ip de su maquina o servidor