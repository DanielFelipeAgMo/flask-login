class Config:
    SECRET_KEY = 'B!1w8NAt1T^%kvhUI*S^'


class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'tdea'
    MYSQL_PASSWORD = '1234'
    MYSQL_DB = 'flask-login'


config = {
    'development': DevelopmentConfig
}
    