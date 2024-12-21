import requests

# Отправляем GET-запрос
response = requests.get('https://jsonplaceholder.typicode.com/posts')
# Проверяем статус - код
if response.status_code == 200:
    print(response.json())  # Выводим данные в консоль