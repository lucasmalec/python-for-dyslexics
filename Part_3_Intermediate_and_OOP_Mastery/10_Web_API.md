# Moduł 10: Web & API — Praca z Internetem

## 10.1 requests library — HTTP requests

```bash
pip install requests
```

```python
import requests

# GET request
response = requests.get('https://api.github.com/users/github')
print(response.status_code)    # 200
print(response.json())         # Słownik z danymi
print(response.text)           # Tekst HTML/JSON
print(response.headers)        # Nagłówki

# Sprawdzenie statusu
if response.status_code == 200:
    print("Sukces!")
```

## 10.2 GET — pobieranie danych

```python
import requests

# Parametry zapytania
params = {
    'q': 'python',
    'sort': 'stars',
    'order': 'desc'
}

response = requests.get('https://api.github.com/search/repositories', params=params)
data = response.json()

print(data['total_count'])  # Liczba wyników
for repo in data['items'][:5]:
    print(f"{repo['name']} — {repo['stargazers_count']} gwiazdek")
```

## 10.3 POST — wysyłanie danych

```python
import requests
import json

# Wysyłanie JSON
url = 'https://httpbin.org/post'
data = {
    'name': 'Alice',
    'age': 30,
    'email': 'alice@example.com'
}

response = requests.post(url, json=data)
print(response.json())

# Wysyłanie formularza
form_data = {
    'username': 'alice',
    'password': 'secret'
}

response = requests.post('https://example.com/login', data=form_data)
```

## 10.4 Nagłówki (Headers)

```python
import requests

headers = {
    'User-Agent': 'MyApp/1.0',
    'Authorization': 'Bearer token123'
}

response = requests.get('https://api.example.com/data', headers=headers)
print(response.json())
```

## 10.5 Obsługa błędów

```python
import requests
from requests.exceptions import RequestException, ConnectionError, Timeout

try:
    response = requests.get('https://api.example.com/data', timeout=5)
    response.raise_for_status()  # Rzuć błąd jeśli status >= 400
    data = response.json()
except ConnectionError:
    print("Brak połączenia")
except Timeout:
    print("Timeout — serwer nie odpowiada")
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")
except requests.exceptions.RequestException as e:
    print(f"Błąd: {e}")
```

## 10.6 Sessions — optymalizacja

```python
import requests

# Bez sessions — nowe połączenie za każdym razem
for i in range(5):
    response = requests.get(f'https://api.example.com/user/{i}')

# Z sessions — reuse połączenia
session = requests.Session()
session.headers.update({'Authorization': 'Bearer token123'})

for i in range(5):
    response = session.get(f'https://api.example.com/user/{i}')

session.close()
```

## 10.7 Pobieranie plików

```python
import requests

# Pobierz plik
url = 'https://example.com/file.pdf'
response = requests.get(url)

if response.status_code == 200:
    with open('downloaded_file.pdf', 'wb') as f:
        f.write(response.content)

# Pobieranie dużych plików — stream
response = requests.get(url, stream=True)
with open('large_file.bin', 'wb') as f:
    for chunk in response.iter_content(chunk_size=8192):
        if chunk:
            f.write(chunk)
```

## 10.8 API — praktyczny przykład

```python
import requests
import json

class WeatherAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api.openweathermap.org/data/2.5/weather'
    
    def get_weather(self, city):
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric'
        }
        
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Błąd API: {e}")
            return None
    
    def get_temperature(self, city):
        data = self.get_weather(city)
        if data:
            return data['main']['temp']
        return None

# Użycie
weather = WeatherAPI('your_api_key')
temp = weather.get_temperature('Warsaw')
print(f"Temperatura w Warszawie: {temp}°C")
```

---

## Zadania

### Zadanie 10.1: GET request
Pobierz dane z `https://api.github.com/users/torvalds`  
Wypisz: login, name, followers, public repos

### Zadanie 10.2: Search API
Używając GitHub API, wyszukaj 10 top repozytoriów Pythona  
Wypisz nazwę i liczbę gwiazdek

### Zadanie 10.3: POST request
Wyślij POST do `https://httpbin.org/post` z danymi:
```json
{
  "name": "Twoje imię",
  "age": 25,
  "hobby": "coding"
}
```

### Zadanie 10.4: Error handling
Stwórz funkcję, która pobiera dane z API z timeout=5  
Obsłuż: ConnectionError, Timeout, HTTPError

### Zadanie 10.5: Sessions
Pobierz dane z 5 różnych GitHub użytkowników używając session

