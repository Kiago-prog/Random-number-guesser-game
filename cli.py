import random
from db import Session, engine
from models.user import User
from models.game import Game
from models.guess import Guess
from models import user, game, guess

def main():
    Base.metadata.create_all(engine)
    session = Session()

    username = input("Enter your username: ")
    player = session.query(User).filter_by(username=username).first()
    if not player:
        player = User(username=username)
        session.add(player)
        session.commit()

    print("Welcome,", player.username)
    target = random.randint(1, 100)
    new_game = Game(user=player, target_number=target)
    session.add(new_game)
    session.commit()