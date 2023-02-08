class Config:
    SECRET_KEY = "!Bertulio123"


class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = "localhost"
    MYSQL_USER = "root"
    MYSQL_PASSWORD = ""
    MYSQL_DB = "colegio"


config = {
    'development': DevelopmentConfig
}
