# models/guess.py
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class Guess(Base):
    __tablename__ = 'guesses'

    id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey('games.id'))
    guess_number = Column(Integer, nullable=False)

    game = relationship('Game', back_populates='guesses')
