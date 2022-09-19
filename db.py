from sqlalchemy import create_engine, MetaData
import os

USER = 'root'#os.environ['USER']
PASSWORD = 'eEITBL9hIeOrKDCmtifM'#os.environ['PASSWORD']
HOST = 'containers-us-west-61.railway.app'#os.environ['HOST']
DB = 'railway'#os.environ['DB']

DB_URL = "mysql+pymysql://{}:{}@{}:3306/{}".format(USER, PASSWORD, HOST, DB)

engine = create_engine(DB_URL, pool_pre_ping=True)

meta = MetaData()

db = engine.connect()

meta.create_all(engine)
