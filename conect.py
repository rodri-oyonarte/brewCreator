
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
class Conexion(object):

    def __init__(self):
        self.engine

    def engine(self):
        self.engine = create_engine("mysql+pymysql://root:root@127.0.0.1/brewCreator?host=localhost?port=3306", echo=True)
        return self.engine
    def Session(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session