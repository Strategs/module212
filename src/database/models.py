from sqlalchemy import Boolean, Column, Integer, String, DateTime, func, event, ForeignKey
from sqlalchemy.orm import declarative_base,relationship

Base = declarative_base()


class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String)
    birthday = Column(DateTime, nullable=False)
    description = Column(String)
    favorites = Column(Boolean, default=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    user_id = Column('user_id', ForeignKey("users.id", ondelete='CASCADE'), default=None)
    user = relationship("User", backref="contacts")


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(25))
    email = Column(String(150), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    created_at = Column('creates_at', DateTime, default=func.now())
    refresh_token = Column(String(255), nullable=True)


'''
наступний блок реалізовано для розуміння роботи event
'''

@event.listens_for(Contact, 'before_insert')
def updated_favorites(mapper, conn, target):
    family = ['Кохана', 'Батько', 'Мама']
    if target.first_name in family:
        target.favorites = True



