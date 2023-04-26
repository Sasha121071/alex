from sqlalchemy import Column, Integer, String, ForeignKey
from models.database import Base


class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    surname = Column(String(250), nullable=False)  # nullable=False - поле обязательное для заполнения
    name = Column(String(250), nullable=False)
    patronymic = Column(String(250), nullable=False)
    age = Column(Integer)
    group = Column(Integer, ForeignKey('groups.id'))

    def __init__(self, full_name, age, id_group):
        self.surname = full_name[0]
        self.name = full_name[1]
        self.patronymic = full_name[2]
        self.age = age
        self.group = id_group

    def __repr__(self):
        return f"Студент (ФИО: {self.surname} {self.name} {self.patronymic}, " \
               f"Возраст: {self.age}, ID группы: {self.group})"


