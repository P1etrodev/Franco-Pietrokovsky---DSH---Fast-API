from sqlalchemy import create_engine, MetaData
import os

USER = os.environ['USER']
PASSWORD = os.environ['PASSWORD']
HOST = os.environ['HOST']
DB = os.environ['DB']

DB_URL = "mysql+pymysql://{}:{}@{}:3306/{}".format(USER, PASSWORD, HOST, DB)

engine = create_engine(DB_URL, pool_pre_ping=True)

meta = MetaData()

db = engine.connect()

meta.create_all(engine)
