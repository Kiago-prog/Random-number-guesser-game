# 🎯 Random Number Guesser Game (CLI + SQLAlchemy ORM)

A terminal-based number guessing game built with Python that uses SQLAlchemy ORM to track users, games, and guesses in a database. This project demonstrates core CLI functionality, database relationships, and object-oriented design.

---

## 🚀 Features

- CLI interface for playing the number guessing game.
- Tracks player profiles and their game history.
- Stores guesses and calculates the number of attempts.
- Uses SQLAlchemy ORM to manage and persist data.
- Modular project structure with best practices.
- Pipenv for dependency and virtual environment management.

---

## 🧑‍💻 User Stories

1. **As a user, I want to create a username**, so I can save and track my game history.
2. **As a user, I want to receive feedback on each guess**, so I know if I’m getting closer.
3. **As a user, I want to know how many attempts I used**, so I can track my performance.

---

## 🗃️ Database Models

- **User**: Represents a player.
- **Game**: Represents an instance of a game played by a user.
- **Guess**: Tracks individual guesses made in each game.

### Relationships:
- A `User` has many `Games`
- A `Game` has many `Guesses`

---

## 🧱 Tech Stack

- Python 3
- SQLAlchemy
- SQLite (default database)
- Pipenv (virtual environment & package management)

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd number_guessing_game
```

### 2. Install Dependencies with Pipenv
```bash
pipenv install
pipenv shell
```

### 3. Create the Database
``bash
python create_tables.py
```

### 4. Run the Game
```bash
python3 cli.py
```

### 📬 Contact
Created by Kiago Roy