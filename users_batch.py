import uuid
from datetime import datetime

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from faker import Faker

engine = create_engine('mysql+mysqlconnector://root:@localhost/laplanduas_rental3002')
db_session = sessionmaker(bind=engine)
fake = Faker()

_db = db_session()

start = datetime.now()

for _round in range(100):
    _query = "INSERT INTO auth_users(username, password, roles_id) VALUES"
    values = {}
    for i in range(1000):
        _query = _query + f'(:username{i}, :password{i}, :roles_id{i}),'
        values[f'username{i}'] = fake.first_name() + str(uuid.uuid4())
        values[f'password{i}'] = 'salasana'
        values[f'roles_id{i}'] = 1

    # viimeinen pilkku poistetaan
    _query = _query[:-1]
    _db.execute(text(_query), values)
    print("# valmis")
    _db.commit()

_db.close()

end = datetime.now()
print("########aika kului:", end - start)
