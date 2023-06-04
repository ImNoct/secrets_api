# class Config():
#     db_host = 'postgres'
#     db_name = 'secrets'
#     dp_user = 'secretsowner'
#     db_password = '1234'
#     db_port = '8000'
#     secret_key = 'ksfqpp9neli91'
#     algorithm = 'HS256'
#     secret_expire = 1

# config = Config()

from pydantic import BaseSettings


class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str

    class Config:
        env_file = "./.env"


config = Settings()