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

    print("Guess a number between 1 and 100:")
    while True:
        try:
            number = int(input("Your guess: "))
            session.add(Guess(game=new_game, guess_number=number))
            session.commit()

            if number < target:
                print("Too low!")
            elif number > target:
                print("Too high!")
            else:
                print("Correct!")
                break
        except ValueError:
            print("Invalid input.")

    attempts = session.query(Guess).filter_by(game_id=new_game.id).count()
    print(f"You guessed the number in {attempts} attempts.")

if __name__ == "__main__":
    from db import Base
    main()