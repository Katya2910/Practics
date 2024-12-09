# -*- coding: utf-8 -*-
"""Копия блокнота "Практика 0.8.0.ipynb"

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CRTnhWd84o7Y_O_VHwsyRwoj4uxv6CEs

**Введите ваше ФИО**
"""

Хихлушка Екатерина

"""# Задание 1

Задача: Создать чат бота для получения информации об исследованиях космоса

Описание: Создайте комплексное приложение командной строки, которое будет использоваться в качестве панели управления исследованиями космоса. Данное приложение будет обращаться к https://api.nasa.gov/ для предоставления пользователям набора информации о космосе, включая:

- Астрономическая картинка дня (APOD): Отображение APOD с пояснениями к нему.
- Фотографии с марсохода: позволяет пользователям выбирать и фильтровать фотографии с марсохода по дате и типу камеры.
- Объекты, сближающиеся с Землей (ОСЗ): Поиск и отображение объектов, сближающихся с Землей, на определенную дату, включая их размеры и потенциальную опасность.
- Данные о космической погоде: Отображают последние данные о космической погоде, включая солнечные вспышки и геомагнитные бури.
Приложение должно позволять пользователям ориентироваться в этих функциях, корректно обрабатывать ошибки и обеспечивать удобство работы.

Требования:
- Пользовательский ввод: Приложение должно предложить пользователю ввести данные, чтобы выбрать, какую функцию он хочет изучить.
- Проверка данных: Убедитесь, что пользовательские данные (например, даты) проверены.
- Обработка ошибок: Корректно обрабатывайте ошибки API и неверные ответы.
- Представление данных: Представляйте данные в четкой и организованной форме.
- Опция выхода: позволяет пользователям выходить из приложения в любое время.
"""

import requests
import datetime

NASA_url="https://api.nasa.gov/planetary/"

NASA_API_key='vl9ROZ8RaeUXD6Fo1cCbSIQWC5n83FWs7UZCv6bz'

def astronomical_picture():
  url="https://api.nasa.gov/planetary/apod"
  params={"api_key": NASA_API_key}
  response=requests.get(url, params=params)
  if response.status_code==200:
    data = response.json()
    print(data['title'])
    print(data['explanation'])
    print(data['url'])
  else:
    print("Ошибка при получении APOD")


def get_mars_photos(date, camera=None):
  url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
  params = {"api_key": NASA_API_key, "earth_date": date}
  if camera:
    params["camera"] = camera
  response = requests.get(url, params=params)
  if response.status_code == 200:
    data = response.json()
    if data["photos"]:
      for photo in data["photos"]:
        print(f"**{photo['img_src']}**")
    else:
      print(f"Фотографий с марсохода на эту дату нет.")
  else:
    print("Ошибка при получении фотографий с марсохода.")

def get_neo_by_date(date):
  url = "https://api.nasa.gov/neo/rest/v1/feed"
  params = {"api_key": NASA_API_key, "start_date": date, "end_date": date}
  response = requests.get(url, params=params)
  if response.status_code == 200:
    data = response.json()
    if data["near_earth_objects"]:
      for date_key, neos in data["near_earth_objects"].items():
        for neo in neos:
          print(f"**{neo['name']}**")
          print(f"Диаметр: {neo['estimated_diameter']['kilometers']['estimated_diameter_max']} км")
          print(f"Потенциальная опасность: {neo['is_potentially_hazardous_asteroid']}")
    else:
      print(f"На эту дату нет данных об объектах, сближающихся с Землей.")
  else:
    print("Ошибка при получении данных об ОСЗ.")

def get_space_weather():
  url = "https://api.nasa.gov/DONKI/SWPC/latest"
  params = {"api_key": NASA_API_key}
  response = requests.get(url, params=params)
  if response.status_code == 200:
    data = response.json()
    print(f"**Космическая погода**")
    print(f"Солнечные вспышки: {data.get('activity', {}).get('active_regions', 'Данные отсутствуют')}")
    print(f"Геомагнитные бури: {data.get('activity', {}).get('geomagnetic_storm', 'Данные отсутствуют')}")
  else:
    print("Ошибка при получении данных о космической погоде.")

print("\n**Панель управления космическими исследованиями**")
print("1. Астрономическая картинка дня (APOD)")
print("2. Фотографии с марсохода")
print("3. Объекты, сближающиеся с Землей (ОСЗ)")
print("4. Данные о космической погоде")
print("5. Выход")

choice = input("Выберите действие: ")

if choice=="1":
      astronomical_picture()
elif choice=="2":
    date_str = input("Введите дату (YYYY-MM-DD): ")
    if validate_date(date_str):
      camera=input("Введите название камеры (необязательно): ")
      get_mars_photos(date_str, camera)
    else:
      print("Неверный формат даты. Используйте YYYY-MM-DD.")
elif choice=="3":
    date_str=input("Введите дату (YYYY-MM-DD): ")
    if validate_date(date_str):
      get_neo_by_date(date_str)
    else:
      print("Неверный формат даты. Используйте YYYY-MM-DD.")
elif choice=="4":
  get_space_weather()
elif choice=="5":
  print("До свидания!")
else:
  print("Неверный выбор. Попробуйте снова.")

"""# Задание 2

Описание задачи

Цель этой задачи - создать скрипт на Python, который взаимодействует с API Чикагского института искусств (https://api.artic.edu/docs/) для извлечения и отображения произведений искусства. Скрипт должен позволять пользователям просматривать работы по страницам, фильтровать их по имени художника и просматривать подробную информацию о выбранных произведениях искусства. Ниже приведены требования и функциональные возможности, которые необходимо реализовать:

Требования:
Извлекать произведения искусства:

- Создайте функцию, которая извлекает список произведений искусства из API Чикагского института искусств.
Функция должна принимать параметр page для разбивки на страницы и возвращать список произведений искусства вместе с информацией о разбивке на страницы.
Фильтровать произведения искусства:

- Реализуйте функцию, которая фильтрует список произведений искусства на основе имени указанного художника. Функция должна возвращать список работ, которые соответствуют имени художника (без учета регистра).
Отображать подробную информацию об оформлении:

- Напишите функцию, которая отображает названия работ для пользователя и позволяет ему выбрать одну из них, введя соответствующий номер.
После выбора функция должна отображать подробную информацию о выбранном произведении, включая название, исполнителя, дату и носитель.
Разбивка на страницы и взаимодействие с пользователем:

- Создайте основную функцию, которая управляет выборкой произведений и взаимодействием с пользователем.

Разрешите пользователям перемещаться по страницам с произведениями искусства, выполнять фильтрацию по исполнителю или выходить из программы.

Если страниц с произведениями искусства несколько, укажите варианты перехода к следующей странице, предыдущей странице, фильтрации по исполнителю или выхода из программы.
"""

import requests

URL="https://api.artic.edu/api/v1/artworks"

def get_artworks(page=1):
  url = f"{URL}?page={page}&limit=10&fields=id,title,artist_title,date_start,medium"
  response = requests.get(url)
  if response.status_code==200:
    data=response.json()
    return data["data"], data["pagination"]
  else:
    print(f"Ошибка: {response.status_code}")
    return [], None


def filter_by_artist(artworks, artist):
  filtered_works = []
  for work in artworks:
    if isinstance(work["artist_title"], str):
      if artist in work["artist_title"]:
        filtered_works.append(work)
    elif isinstance(work["artist_title"], list):
      for name in work["artist_title"]:
        if isinstance(name, str):
          if artist in name:
            filtered_works.append(work)
            break
    elif isinstance(work["artist_title"], dict):
      for key, value in work["artist_title"].items():
        if isinstance(value, str):
          if artist in value:
            filtered_works.append(work)
            break
  return filtered_works

def display_artwork_details(artwork):
  print(f"Название: {artwork['title']}")
  print(f"Исполнитель: {artwork['artist_title']}")
  print(f"Дата: {artwork['date_start']}")
  print(f"Носитель: {artwork['medium']}")

def main():
  current_page=1
  next_page=None
  while True:
    print("Список произведений искусства:")
    artworks, next_page = get_artworks(current_page)

    if artworks:
      for index, artwork in enumerate(artworks):
        print(f"{index + 1}. {artwork['title']} ({artwork['artist_title']})")

      if next_page:
        print("1. Следующая страница")

      print("2. Фильтровать по художнику")
      print("3. Выйти")

      choice = input("Выберите действие: ")

      if choice=="1" and next_page:
        current_page = next_page
      elif choice=="0":
        current_page = 1
      elif choice == "2":
        artist = input("Введите имя художника: ")
        filtered_artworks = filter_by_artist(artworks, artist)
        if filtered_artworks:
          for index, artwork in enumerate(filtered_artworks):
            print(f"{index + 1}. {artwork['title']} ({artwork['artist_title']})")
          artwork_choice = int(input("Выберите номер произведения: ")) - 1
          if 0 <= artwork_choice < len(filtered_artworks):
            display_artwork_details(filtered_artworks[artwork_choice])
        else:
          print(f"Работы {artist} не найдены.")
      elif choice == "3":
        print("До свидания!")
        break
      else:
        print("Неверный выбор. Попробуйте снова.")
    else:
      print("Больше работ не найдено.")

if __name__ == "__main__":
  main()

"""# Задание 3

Задача: Создать программу по управлению портфелем криптовалют

Цель: Создать скрипт на Python, который извлекает цены на криптовалюты в режиме реального времени, позволяет пользователям управлять портфелем криптовалют, вычисляет общую стоимость портфеля, отслеживает изменения цен и предоставляет исторические данные о ценах для анализа.

Требования:
Получение текущих цен на криптовалюты:

Используйте https://docs.coingecko.com/ для получения актуальных цен на список криптовалют.

Управление портфелем:

- Позволяет пользователю создавать портфель криптовалют и управлять им, указывая количество каждой криптовалюты, которой он владеет.
- Расчитывает общую стоимость портфеля в указанной фиатной валюте (например, долларах США).

Отслеживание изменения цен:

- Отображение процентного изменения цены для каждой криптовалюты в портфеле за последние 24 часа.
- Выделите все криптовалюты, стоимость которых значительно увеличилась или снизилась.

Поиск исторических данных о ценах:

- Получение исторических данных о ценах на указанную криптовалюту за последнюю неделю.
- Предоставьте пользователю возможность визуализировать эти данные в простом текстовом формате (например, цены за день).

Взаимодействие с пользователем:

- Реализуйте интерфейс командной строки для ввода данных пользователем.
- Предоставьте опции для получения текущих цен, управления портфелем, просмотра изменений цен или анализа исторических данных.
"""

import requests
from datetime import datetime, timedelta
BASE_URL = "https://api.coingecko.com/api/v3"
def get_current_prices(coins):
  url = f"{BASE_URL}/simple/price?ids={','.join(coins)}&vs_currencies=usd"
  response = requests.get(url)
  if response.status_code == 200:
    return response.json()
  else:
    print(f"Ошибка получения цен: {response.status_code}")
    return {}

def get_historical_prices(coin, days=7):
  end_date = datetime.now()
  start_date = end_date - timedelta(days=days)
  url = f"{BASE_URL}/coins/{coin}/market_chart/range?vs_currency=usd&from={int(start_date.timestamp())}&to={int(end_date.timestamp())}"
  response = requests.get(url)
  if response.status_code == 200:
    return response.json()["prices"]
  else:
    print(f"Ошибка получения исторических данных: {response.status_code}")
    return []

def calculate_portfolio_value(portfolio, prices):
  """Вычисляет общую стоимость портфеля"""
  total_value = 0
  for coin, amount in portfolio.items():
    if coin in prices:
      total_value += prices[coin]["usd"] * amount
  return total_value

def display_portfolio_changes(portfolio, prices, historical_prices):
  print("\nИзменения цен в портфеле:")
  for coin, amount in portfolio.items():
    if coin in prices:
      current_price = prices[coin]["usd"]
      change_24h = prices[coin]["usd_24h_change"]
      print(f"{coin}: Текущая цена - ${current_price:.2f}, Изменение за 24 часа - {change_24h:.2f}%")

def display_historical_prices(coin, historical_prices):

  print(f"История цен {coin} за последнюю неделю:")
  for ts, price in historical_prices:
    date = datetime.fromtimestamp(ts / 1000)
    print(f"{date.strftime('%Y-%m-%d %H:%M')}: ${price:.2f}")

def main():
  """Основная функция для взаимодействия с пользователем"""
  portfolio = {}
  while True:
    print("\nМеню:")
    print("1. Получить текущие цены")
    print("2. Управлять портфелем")
    print("3. Просмотреть изменения цен")
    print("4. Проанализировать исторические данные")
    print("5. Выйти")

    choice = input("Выберите действие: ")

    if choice == "1":
      coins = input("Введите список криптовалют (через запятую): ").split(",")
      prices = get_current_prices(coins)
      if prices:
        for coin, price_data in prices.items():
          print(f"{coin}: ${price_data['usd']:.2f}")
    elif choice == "2":
      while True:
        print("Управление портфелем:")
        print("1. Добавить криптовалюту")
        print("2. Удалить криптовалюту")
        print("3. Обновить количество")
        print("4. Вернуться в главное меню")
        portfolio_choice = input("Выберите действие: ")
        if portfolio_choice == "1":
          coin = input("Введите название криптовалюты: ")
          amount = float(input("Введите количество: "))
          portfolio[coin] = amount
          print(f"{coin} добавлен в портфель")
        elif portfolio_choice == "2":
          coin = input("Введите название криптовалюты для удаления: ")
          if coin in portfolio:
            del portfolio[coin]
            print(f"{coin} удален из портфеля")
          else:
            print(f"{coin} не найден в портфеле")
        elif portfolio_choice == "3":
          coin = input("Введите название криптовалюты для обновления количества: ")
          if coin in portfolio:
            amount = float(input("Введите новое количество: "))
            portfolio[coin] = amount
            print(f"Количество {coin} обновлено")
          else:
            print(f"{coin} не найден в портфеле")
        elif portfolio_choice == "4":
          break
        else:
          print("Неверный выбор")

      if portfolio:
        prices = get_current_prices(list(portfolio.keys()))
        if prices:
          total_value = calculate_portfolio_value(portfolio, prices)
          print(f"Общая стоимость портфеля: ${total_value:.2f}")
    elif choice == "3":
      prices = get_current_prices(list(portfolio.keys()))
      if prices:
        display_portfolio_changes(portfolio, prices, [])
    elif choice == "4":
      coin = input("Введите название криптовалюты для анализа: ")
      historical_prices = get_historical_prices(coin)
      if historical_prices:
        display_historical_prices(coin, historical_prices)
    elif choice == "5":
      break
    else:
      print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
  main()

"""# Задание 4

Задание 4: Проектное

Вам необходимо самостоятельно найти откртое API предоставляющее информацию в открытом доступе и реализовать собственный проект!


Критерии приемки результата:

- Проект включает в себя не менее 5 возможостей для пользователя
- Проект позволяет использовать все возможности проекта пользователю при помощи взаимодействия через коммандную строку
- Проект работает с открытым API (это значит что при проверке вашей работы преподавателем, преподавателю необходимо просто запустить ячейку с кодом вашего проекта и она будет работать без дополнительных манипуляции)
- Проект должен обязательно включать в себя ряд используемых конструкции:
    - Функции
    - Условные конструкции
    - Ввод/вывод
    - Словари/Списки
- Допускается использование библиотек:
    - requests
    - datetime
    - random

**Здесь добавьте описание вашего проекта**
"""

#  А здесь код