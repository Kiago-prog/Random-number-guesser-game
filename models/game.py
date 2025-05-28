# models/game.py
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    target_number = Column(Integer, nullable=False)

    user = relationship('User', back_populates='games')
    guesses = relationship('Guess', back_populates='game')
