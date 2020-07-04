import requests

def weather():
    KEY = 'key from your personal'    # Key з сайту openweather.org
    city = input('Назва міста: ')    # Ввід назви міста
    URL = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=' + KEY    # Силка
                                                                                                   # api з містом

    response = requests.get(URL).json() # Запит на дані (.json() перетворює дані json в простий словник)
    print(f'Температура в місті {city} {int(response["main"]["temp"])}°C Хмарність {response["clouds"]["all"]}%')
    print(f'Швидкість вітру {(response["wind"]["speed"])} m/s')
weather()
