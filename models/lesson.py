from sqlalchemy import Column, Integer, String, ForeignKey, Table
from models.database import Base
from sqlalchemy.orm import relationship

association_table = Table('association', Base.metadata,
                          Column('lesson_id', Integer, ForeignKey('lessons.id')),
                          Column('group_id', Integer, ForeignKey('groups.id')))


class Lesson(Base):
    __tablename__ = 'lessons'

    id = Column(Integer, primary_key=True)
    lesson_title = Column(String(250), nullable=False)
    groups = relationship('Group', secondary=association_table, backref='group_lesson')

    def __repr__(self):
        return f"Предмет (ID: {self.id}, Название: {self.lesson_title})"
