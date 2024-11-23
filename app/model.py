# import sqlalchemy as db
#
#
# class User(db.Model):
#     __tablename__ = 'users'
#     user_id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String(255), nullable=False)
#     last_name = db.Column(db.String(255), nullable=False)
#
# class User_info(db.Model):
#     __tablename__ = 'user_info'
#     user_id = db.Column(db.Integer, primary_key=True)
#     city = db.Column(db.String(255), nullable=False)
#     date_of_birth = db.Column(db.Date, nullable=False)
#     weight = db.Column(db.Float, nullable=False)

с1 = users(
    first_name = 'Сергей',
    last_name = 'Живицкий',
    city = 'Москва',
    date_of_birth = '15.01.2010',
    weight = '60'
)
с2 = user_info(
    city = 'Москва',
    date_of_birth = '15.01.2010',
    weight = '60'
)