import sqlalchemy as db
# from model import User, User_info


engine = db.create_engine('sqlite:///database_one.db')
conn = engine.connect()
metadata = db.MetaData()

users = db.Table('users', metadata,
                  db.Column('user_id', db.Integer, primary_key=True),
                  db.Column('first_name', db.String(255)),
                  db.Column('last_name', db.String(255)),
                  )
user_info = db.Table('user_info', metadata,
                      db.Column('user_id', db.Integer, primary_key=True),
                      db.Column('city', db.String(255)),
                      db.Column('date_of_birth', db.String(255)),
                      db.Column('weight', db.String(255)),
                      )

metadata.create_all(engine)

insert_user = users.insert().values([
    {'first_name':'Иван', 'last_name':'Филипов'},
    {'first_name':'Ирина', 'last_name':'Кандрашева'},
    {'first_name':'Кирил', 'last_name':'Земин'},
])

insert_user_info = user_info.insert().values([
    {'city':'Москва', 'date_of_birth':'15.08.1980','weight':'95'},
    {'city':'Хабаровск', 'date_of_birth':'24.01.1998','weight':'55'},
    {'city':'Киров', 'date_of_birth':'04.04.2004','weight':'75'},
])

conn.execute(insert_user)
conn.execute(insert_user_info)
conn.commit()


