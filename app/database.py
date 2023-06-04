from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from . import models
from .config import config


# SQLALCHEMY_DATABASE_URL = f'postgresql://{config.dp_user}:{config.db_password}@{config.db_host}:{config.db_port}/{config.db_name}'
SQLALCHEMY_DATABASE_URL = f'postgresql://{config.database_username}:{config.database_password}@{config.database_hostname}/{config.database_name}'
# print(SQLALCHEMY_DATABASE_URL)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def create_tables():
    # if not engine.dialect.has_table(engine, Secret.__tablename__):
        # print("creating table")
        models.Secret.__table__.create(bind=engine, checkfirst=True)


def get_db():
    db = SessionLocal()
    create_tables()
    try:
        yield db
    finally:
        db.close()

# def create_tables():
#     commands = (
#         """
#         CREATE TABLE IF NOT EXISTS secrets (
#             key VARCHAR(32) NOT NULL PRIMARY KEY,
#             code VARCHAR(64) NOT NULL,
#             text VARCHAR(256) NOT NULL
#         )
#         """
#     )
#     for command in commands:
#         cursor.execute(command)
#     conn.commit()


# while True:
#     try:
#         conn = psycopg2.connect(host=config.db_host, database=config.db_name, 
#                                user=config.dp_user, password=config.db_password,
#                                cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Connected to db")
#         break
#     except Exception as error:
#         print("Connecting to database failed")
#         print("Error: ", error)
#         time.sleep(2)