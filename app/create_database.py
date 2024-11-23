import sqlalchemy as db
# from sqlalchemy.orm import Session, sessionmaker
# from model import User, User_info

#Создание движка sqlite
engine = db.create_engine('sqlite:///database_one.db')
#Подключение к движку
conn = engine.connect()
#Метаданные
metadata = db.MetaData()

#создание таблицы users и user_info
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
#Создание объектов таблиц
metadata.create_all(engine)

#Заполнение таблиц данными списком словарей
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

#Выполнение запроса на добавление данных и принять изменения
conn.execute(insert_user)
conn.execute(insert_user_info)
conn.commit()
#
# #бъект session для работы с базой
# session = Session(bind=engine)
#Класс sessionmaker который создает класс Session
# session = sessionmaker(bind=engine)
# session = Session()


#Запрос вывести таблицу users
select = conn.execute(db.select(users))
print(select.fetchall())

#Запрос с фильтром
select_filter = conn.execute(db.select(users).filter(users.c.last_name == 'Кандрашева'))
print(select_filter.fetchall())

#Запрос с сортировкой по солбцу с именем пользователей, в обратном порядке
select_order_by = conn.execute(db.select(users).order_by(users.c.last_name.asc() ))
print(select_order_by.fetchall())


#all
select_all = conn.execute(db.select(user_info).filter(user_info.c.city == 'Москва').all())
print(select_all.fetchall())