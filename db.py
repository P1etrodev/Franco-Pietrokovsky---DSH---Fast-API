from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

USER = "***REMOVED***123"
PASSWORD = "***REMOVED***"
HOST = "***REMOVED***"
DB = "***REMOVED***"

DB_URL = "mysql+pymysql://{}:{}@{}:3306/{}".format(USER, PASSWORD, HOST, DB)

engine = create_engine(DB_URL, pool_pre_ping=True)

meta = MetaData()

db = engine.connect()

meta.create_all(engine)
