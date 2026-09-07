# Moduł 9: Databases — Praca z Bazami Danych

## 9.1 SQLite — embeded database

SQLite to baza danych zapisana w jednym pliku — idealna do nauki i małych aplikacji.

```python
import sqlite3

# Połączenie (tworzy plik jeśli nie istnieje)
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Tworzenie tabeli
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE,
        age INTEGER
    )
''')

conn.commit()
```

## 9.2 INSERT — dodawanie danych

```python
import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Dodanie jednego użytkownika
cursor.execute('INSERT INTO users (name, email, age) VALUES (?, ?, ?)',
               ('Alice', 'alice@example.com', 30))

# Dodanie wielu użytkowników
users = [
    ('Bob', 'bob@example.com', 25),
    ('Charlie', 'charlie@example.com', 35),
]
cursor.executemany('INSERT INTO users (name, email, age) VALUES (?, ?, ?)', users)

conn.commit()
print(f"Dodano {cursor.rowcount} rekordów")
```

## 9.3 SELECT — pobieranie danych

```python
import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Wszystkie rekordy
cursor.execute('SELECT * FROM users')
all_users = cursor.fetchall()
for user in all_users:
    print(user)

# Jeden rekord
cursor.execute('SELECT * FROM users WHERE id = ?', (1,))
user = cursor.fetchone()
print(user)  # (1, 'Alice', 'alice@example.com', 30)

# Kilka rekordów
cursor.execute('SELECT * FROM users WHERE age > ?', (25,))
older_users = cursor.fetchall()
print(older_users)

# Jako słowniki
conn.row_factory = sqlite3.Row
cursor.execute('SELECT * FROM users WHERE id = ?', (1,))
user = cursor.fetchone()
print(user['name'])  # Alice
```

## 9.4 UPDATE i DELETE

```python
import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Update
cursor.execute('UPDATE users SET age = ? WHERE name = ?', (31, 'Alice'))
conn.commit()

# Delete
cursor.execute('DELETE FROM users WHERE age < ?', (30,))
conn.commit()
print(f"Usunięto {cursor.rowcount} rekordów")
```

## 9.5 SQL Queries — zaawansowane zapytania

```python
import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# COUNT
cursor.execute('SELECT COUNT(*) FROM users')
total = cursor.fetchone()[0]
print(f"Razem użytkowników: {total}")

# WHERE + AND/OR
cursor.execute('SELECT * FROM users WHERE age > ? AND name LIKE ?', (25, 'A%'))
results = cursor.fetchall()

# ORDER BY
cursor.execute('SELECT * FROM users ORDER BY age DESC LIMIT 5')
top_oldest = cursor.fetchall()

# GROUP BY
cursor.execute('SELECT age, COUNT(*) FROM users GROUP BY age')
age_groups = cursor.fetchall()
```

## 9.6 Transactions — transakcje

```python
import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

try:
    cursor.execute('INSERT INTO users (name, email, age) VALUES (?, ?, ?)',
                   ('David', 'david@example.com', 28))
    cursor.execute('INSERT INTO users (name, email, age) VALUES (?, ?, ?)',
                   ('Eve', 'eve@example.com', 32))
    conn.commit()
except Exception as e:
    conn.rollback()  # Cofnij zmiany
    print(f"Błąd: {e}")
finally:
    conn.close()
```

## 9.7 Context manager dla bazy danych

```python
import sqlite3

def query_db(filename, sql, params=()):
    with sqlite3.connect(filename) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(sql, params)
        return cursor.fetchall()

# Użycie
users = query_db('users.db', 'SELECT * FROM users WHERE age > ?', (25,))
for user in users:
    print(dict(user))
```

## 9.8 Intro do ORM — SQLAlchemy (zaawansowane)

```bash
pip install sqlalchemy
```

```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    age = Column(Integer)

# Tworzenie bazy
engine = create_engine('sqlite:///users.db')
Base.metadata.create_all(engine)

# Sesja
Session = sessionmaker(bind=engine)
session = Session()

# Dodawanie
new_user = User(name='Frank', email='frank@example.com', age=40)
session.add(new_user)
session.commit()

# Zapytania
users = session.query(User).filter(User.age > 25).all()
session.close()
```

---

## Zadania

### Zadanie 9.1: SQLite CRUD
Stwórz bazę `library.db` z tabelą `books` (id, title, author, year)  
Dodaj 5 książek, odczytaj, update rok jednej, usuń jedną

### Zadanie 9.2: Zaawansowane zapytania
Z bazy users.db napisz zapytania:
- Średnia wieku
- Najstarszy użytkownik
- Liczba użytkowników po 30 roku życia
- Top 3 najmłodsi

### Zadanie 9.3: Transakcje
Stwórz dwie tabele: `accounts` (id, name, balance) i `transactions`  
Zaimplementuj transfer z jednego konta na drugie (z transakcją)

### Zadanie 9.4: Context manager
Stwórz funkcję `execute_query(db_file, query, params)` używającą with

