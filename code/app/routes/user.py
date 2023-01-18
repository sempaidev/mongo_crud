from fastapi import APIRouter, Response, status
from app.config.db import conn
from app.schemas.user import userEntity, usersEntity
from app.models.user import User
from passlib.hash import sha256_crypt
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT
user = APIRouter()

@user.get('/users', response_model= list[User], tags=['Usuario'])
def get_users():
    """
    Devuelve una lista de todos los usuarios en la base de datos.
    :return: Una lista de usuarios
    """
    return usersEntity(conn.local.user.find())

@user.post('/users', response_model=User, tags=['Usuario'])
def create_user(user: User):
    """
    Tomamos un objeto de usuario, lo convertimos en un diccionario, encriptamos la contraseña,
    eliminamos la identificación y luego la insertamos en la base de datos
    
    :param user: Usuario
    :type user: User
    :return: El usuario que se creó
    """
    #Covertimos en diccionario los datos obtenidos
    new_user = dict(user)
    #encriptamos la contraseña
    new_user["password"] = sha256_crypt.encrypt(new_user['password'])
    del new_user['id']
    #llamamos a la conexion y guardamos
    id = conn.local.user.insert_one(
        new_user
    ).inserted_id

    user = conn.local.user.find_one({"_id": id})
    
    return userEntity(user)

    

@user.get('/users/{id}', response_model=User, tags=['Usuario'])
def get_user(id: str):
    """
    `get_user` devuelve un objeto `userEntity` de la colección `user` en la base de datos `local`
    
    :param id: Id del usuario a consultar
    :type id: str
    :return: Un objeto de entidad de usuario
    """
    return userEntity(conn.local.user.find_one({"_id": ObjectId(id)}))

@user.put('/users/{id}', response_model=User, tags=['Usuario'])
def update_user(id: str, user: User):
    """
    Toma una identificación y un usuario, y actualiza al usuario con la identificación dada
    
    :param id: str - El id del usuario a actualizar
    :type id: str
    :param user: Usuario
    :type user: User
    :return: Se devuelve la entidad de usuario.
    """
    conn.local.user.find_one_and_update(
        {"_id": id},
        {"$set": dict(user)}
    )
    return userEntity(conn.local.user.find_one({"_id": ObjectId(id)}))

@user.delete('/users/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['Usuario'])
def delete_user(id: str):
    """
    Eliminar un usuario por id
    
    :param id: Id del usuario a eliminar
    :type id: str
    :return: Codigo de status.
    """
    userEntity(conn.local.user.find_one_and_delete({"_id": ObjectId(id)}))
    return Response( status_code=HTTP_204_NO_CONTENT)