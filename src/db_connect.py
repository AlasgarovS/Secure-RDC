import os
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Connection(Base):
    __tablename__ = 'connection'
    
    id = Column(Integer, primary_key=True)
    default_username = Column(String(100), default=None)
    log_username = Column(String(100), default=None)
    ip_address = Column(String(100), default=None)
    port_number = Column(String(100), default=None)


def get_db_path(file_path):
    if not os.path.exists(file_path):
        # If the file does not exist, create it
        with open(file_path, 'w') as file:
            file.write('')
        return ''

    with open(file_path, 'r') as file:
        return file.readline().strip()

db_path = get_db_path('db_path.txt')
DB_NAME = 'secure.db'

# Create a SQLite database using the path from the text file and the static database name
engine = create_engine(f'sqlite:///{os.path.join(db_path, DB_NAME)}')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


# Create a new connection with the current user's login name
with Session() as session:
    user = session.query(Connection).first()
    if user:
        user.log_username = None
    else:
        current_user = str(os.getlogin()).upper() 
        user = Connection(default_username=current_user)
    session.add(user)
    session.commit()
