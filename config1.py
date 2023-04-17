class Config:
    SECRET_KEY = "!Bertulio123"
    IP = "http://127.0.0.1:5000/"


class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = "localhost"
    MYSQL_USER = "root"
    MYSQL_PASSWORD = ""
    MYSQL_DB = "colegio"


config = {
    'development': DevelopmentConfig
}
