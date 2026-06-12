from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url = 'mysql+pymysql://root:root@localhost:3306/mydb'
engine = create_engine(url = db_url)
session = sessionmaker(bind = engine)