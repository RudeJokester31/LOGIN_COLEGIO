from .entities.User import User
import requests
import json
from config1 import Config


class ModelUser():

    url=Config()

    @classmethod
    def login(self, user):
        try:
            url = self.url.IP+"login"
            param = {"username": user.username, "password": user.password}
            datos = requests.post(url, json=param)
            logged_user = json.loads(datos.text)
            if logged_user["codigo"] == "True":
                user = User(
                    logged_user["id"], logged_user["usuario"], logged_user["password"])
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_by_id(self, id):
        try:
            url = self.url.IP+"get_by_id"
            param = {"id": id}
            datos = requests.post(url, json=param)
            row = json.loads(datos.text)
            if row != None:
                return User(row["id"], row["usuario"], None, row["nombres"])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
