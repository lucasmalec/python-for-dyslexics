# Moduł 11: Projekty Praktyczne — Aplikacje Real-World

Połączenie wszystkich nauk z poprzednich modułów w pełnoprawne aplikacje.

---

## Projekt 1: Task Manager CLI

Aplikacja do zarządzania zadaniami z pliku JSON.

### Wymagania:
- Dodawanie zadań
- Listowanie zadań
- Oznaczanie jako wykonane
- Usuwanie zadań
- Zapis do `tasks.json`

### Struktura:
```
task_manager/
├── main.py
├── task_manager.py
├── utils.py
└── tasks.json
```

### task_manager.py
```python
import json
from pathlib import Path
from datetime import datetime

class TaskManager:
    def __init__(self, filename='tasks.json'):
        self.filename = Path(__file__).resolve().parent / filename
        self.tasks = self._load()
    
    def _load(self):
        if self.filename.exists():
            with open(self.filename) as f:
                return json.load(f)
        return []
    
    def _save(self):
        with open(self.filename, 'w') as f:
            json.dump(self.tasks, f, indent=2)
    
    def add(self, title, description=''):
        task = {
            'id': len(self.tasks) + 1,
            'title': title,
            'description': description,
            'done': False,
            'created': datetime.now().isoformat()
        }
        self.tasks.append(task)
        self._save()
        return task
    
    def list_all(self):
        return self.tasks
    
    def mark_done(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                task['done'] = True
                self._save()
                return task
        return None
    
    def delete(self, task_id):
        self.tasks = [t for t in self.tasks if t['id'] != task_id]
        self._save()
```

### main.py
```python
from task_manager import TaskManager

def main():
    manager = TaskManager()
    
    while True:
        print("\n1. Dodaj zadanie")
        print("2. Pokaż zadania")
        print("3. Oznacz jako wykonane")
        print("4. Usuń zadanie")
        print("5. Wyjście")
        
        choice = input("Wybór: ")
        
        if choice == '1':
            title = input("Tytuł: ")
            desc = input("Opis: ")
            manager.add(title, desc)
            print("Zadanie dodane!")
        
        elif choice == '2':
            for task in manager.list_all():
                status = "✓" if task['done'] else "○"
                print(f"{status} [{task['id']}] {task['title']}")
        
        elif choice == '3':
            task_id = int(input("ID zadania: "))
            manager.mark_done(task_id)
            print("Oznaczono jako wykonane!")
        
        elif choice == '4':
            task_id = int(input("ID zadania: "))
            manager.delete(task_id)
            print("Zadanie usunięte!")
        
        elif choice == '5':
            break

if __name__ == '__main__':
    main()
```

---

## Projekt 2: Web Scraper + Database

Pobranie danych z internetu i zapis do bazy danych.

### Wymagania:
- Pobieranie artykułów z bloga
- Zapis do SQLite
- Wyszukiwanie/filtrowanie
- Statystyki

### Przykład — News Scraper:
```python
import requests
from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime

class NewsScraper:
    def __init__(self, db_file='news.db'):
        self.db_file = db_file
        self._init_db()
    
    def _init_db(self):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS articles (
                id INTEGER PRIMARY KEY,
                title TEXT,
                url TEXT UNIQUE,
                source TEXT,
                date_scraped DATETIME
            )
        ''')
        conn.commit()
        conn.close()
    
    def scrape(self, url):
        """Pobierz artykuły z URL"""
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        articles = []
        for item in soup.find_all('article')[:10]:
            title = item.find('h2')
            if title:
                articles.append({
                    'title': title.text.strip(),
                    'url': item.find('a')['href'],
                    'source': 'News Site'
                })
        
        return articles
    
    def save_articles(self, articles):
        """Zapisz artykuły do DB"""
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        
        for article in articles:
            try:
                cursor.execute('''
                    INSERT INTO articles (title, url, source, date_scraped)
                    VALUES (?, ?, ?, ?)
                ''', (article['title'], article['url'], article['source'], datetime.now()))
            except sqlite3.IntegrityError:
                pass  # Artykuł już istnieje
        
        conn.commit()
        conn.close()
    
    def search(self, keyword):
        """Wyszukaj artykuły"""
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute(
            'SELECT * FROM articles WHERE title LIKE ?',
            (f'%{keyword}%',)
        )
        results = cursor.fetchall()
        conn.close()
        return results
```

---

## Projekt 3: API Wrapper

Stwórz własną bibliotekę do pracy z publicznym API.

```python
# pokeapi_wrapper.py
import requests
from functools import lru_cache

class PokemonAPI:
    BASE_URL = 'https://pokeapi.co/api/v2'
    
    @lru_cache(maxsize=128)
    def get_pokemon(self, name):
        """Pobierz dane o Pokémonie"""
        try:
            response = requests.get(f'{self.BASE_URL}/pokemon/{name.lower()}')
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return None
    
    def get_pokemon_info(self, name):
        """Zwróć czytelne info o Pokémonie"""
        data = self.get_pokemon(name)
        if not data:
            return None
        
        return {
            'name': data['name'].title(),
            'height': data['height'] / 10,  # dm → m
            'weight': data['weight'] / 10,  # hg → kg
            'types': [t['type']['name'] for t in data['types']],
            'abilities': [a['ability']['name'] for a in data['abilities']]
        }

# Użycie
api = PokemonAPI()
pikachu = api.get_pokemon_info('pikachu')
print(pikachu)
```

---

## Projekt 4: Mini Chat Application

Serwer i klient komunikujący się po TCP.

```python
# server.py
import socket
import threading

class ChatServer:
    def __init__(self, host='localhost', port=5000):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []
    
    def start(self):
        self.server.bind((self.host, self.port))
        self.server.listen(5)
        print(f"Serwer nasłuchuje na {self.host}:{self.port}")
        
        while True:
            client, addr = self.server.accept()
            self.clients.append(client)
            threading.Thread(target=self.handle_client, args=(client, addr)).start()
    
    def handle_client(self, client, addr):
        print(f"Nowe połączenie: {addr}")
        while True:
            try:
                message = client.recv(1024).decode()
                if not message:
                    break
                
                # Wyślij do wszystkich klientów
                for c in self.clients:
                    if c != client:
                        c.send(message.encode())
            except:
                break
        
        self.clients.remove(client)
        client.close()

if __name__ == '__main__':
    server = ChatServer()
    server.start()
```

---

## Projekt 5: Personal Finance Tracker

Śledzenie przychodów i wydatków.

### Wymagania:
- Dodawanie transakcji
- Kategoryzacja (jedzenie, transport, rozrywka)
- Raportowanie (miesięcze, kategoria)
- Eksport do CSV

### Główne komponenty:
- `Transaction` — model transakcji
- `FinanceTracker` — główna logika
- `Analyzer` — analizowanie danych
- `Exporter` — export do CSV

---

## Wytyczne do projektów

### 1. Struktura
```
project_name/
├── README.md
├── requirements.txt
├── .gitignore
├── src/
│   └── module_name/
│       ├── __init__.py
│       └── main.py
└── tests/
    └── test_main.py
```

### 2. Best Practices
- Użyj type hints
- Pisz testy
- Dokumentuj kod (docstrings)
- Obsługuj błędy (try/except)
- Używaj virtual environment

### 3. Git
```bash
git init
git add .
git commit -m "Initial commit"
```

---

## Zadania do realizacji

### Zadanie 11.1: Task Manager
Zaimplementuj pełny Task Manager z CLI

### Zadanie 11.2: Scraper
Stwórz scraper dla wybranej strony + DB

### Zadanie 11.3: API Wrapper
Wybierz publiczne API i stwórz wrapper bibliotekę

### Zadanie 11.4: Własny projekt
Wymyśl i zaimplementuj aplikację łączącą:
- OOP
- File handling (JSON/CSV)
- Database (SQLite)
- Error handling
- Testy

Powodzenia! 🎉

