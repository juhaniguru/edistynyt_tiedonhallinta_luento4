import datetime
import uuid

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from faker import Faker

engine = create_engine('mysql+mysqlconnector://root:@localhost/laplanduas_rental3002')
db_session = sessionmaker(bind=engine)
fake = Faker()

# avataan tietokantayhteys
_db = db_session()

_query = "INSERT INTO auth_users(username, password, roles_id) VALUES(:username, :password, :roles_id)"
_statement = text(_query)

start = datetime.datetime.now()

for i in range(100000):
    _random_str = str(uuid.uuid4())

    _db.execute(_statement,
                {'username': f'{fake.first_name()}{_random_str}', 'password': fake.first_name(), 'roles_id': 1})
_db.commit()

end = datetime.datetime.now()
print("aikaa kulunut:", end - start)

# suljetaan
_db.close()
