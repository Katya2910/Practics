# -*- coding: utf-8 -*-
"""Копия блокнота "Практика 0.3.0.ipynb"

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Q3_5YGPFFTHJGjbFbxmz_9fDLTHZOzze

ФИО
"""

Хихлушка Екатерина Дмитриевна

"""**Во всей практике нельзя применять библиотеки предоставляющие готовые решения!**

# **Задача 1.**

Типы данных Напишите программу на Python, которая принимает список чисел в качестве входных данных от пользователя, а затем выводит сумму, среднее значение и максимальное значение из списка.

***Нельзя использовать: len(), min(), max(), average(), sum()***

Ввод:
```
1 2 3 4 5 6 7
```
Вывод:

```
Сумма чисел: 28
Среднее арифм.: 4.0
Максимальное значение: 7
```
"""

A=[int(a) for a in input().split()]
sum=0
count=0
max=A[0]
for a in A:
  count+=1
  sum+=a
average=sum/count
for i in range(count):
  if A[i]>max:
    max=A[i]
print("Сумма чисел: ",sum)
print("Среднее арифм.: ",average)
print("Максимальное значение: ",max)

"""# **Задача 2.**

Напишите программу на Python, которая принимает список слов в качестве входных данных от пользователя, а затем распечатывает список в обратном порядке.

Ввод:

```
апельсин мандарин яблоко
```

Вывод:

```
яблоко мандарин апельсин
```
"""

A = (str(a) for a in input().split())
count = 0
B = []

list_A = list(A)
count = len(list_A)

for i in range(count - 1, -1, -1):
    B.append(list_A[i])

print(B)

"""# **Задача 3**

Простой чат-бот
Создайте простого чат-бота, который отвечает на основные запросы пользователей. Программа должна использовать условные выражения для определения намерений пользователя и последующего соответствующего ответа.

Чат бот может:

- помогать складывать числа
- подсказывать фильм, музыку и тд (из заранее созданного списка)
- создавать список дел (а также выводить его, обновлять, очищать)

Интерфейс чат-бота на ваше усмотрение, это могут быть как заранее определенные команды, так и к примеру вызов команды по номеру

*Реализовать без использования функций*

Пример:

Ввод:

```
Олег, какую мызыку посоветуешь?
```

Вывод:

```
Я бы посоветовал вам: Led Zeppelin Stairway to Heaven
```
"""

import random
print('Добрый день! Чем Вам помочь сегодня? Выберите нужную команду по номеру: 1) Помоги сложить числа; 2) Посоветуй классный фильм/музыку и др.; 3)Создай список дел')
N=int(input("Введите номер нужной  команды: "))
print("Хорошо, сейчас посчитаем!")
if N==1:
  count_of_numbers=int(input("Введите количество чисел, которые Вы хотели бы сложить: "))
  sum=0
  for i in range(count_of_numbers):
    a=int(input("Введите число: "))
    sum+=a
  print("Сумма всех введённых Вами чисел равна",sum)
if N==2:
  commands=["музыка","фильм","книга","кафе в Екатеринбурге","сайт по изучению английского языка"]
  print("Хорошо, давайте помогу Вам с выбором! Но для начала выберите одну команду из списка (ввести номер команды)")
  print(commands)
  advice=int(input("Введите номер нужной команды: "))
  if advice==1:
    B=['Led Zeppelin Stairway to Heaven','Mona Lisa','I Want It All','The Winner Takes It All','Every Time You Turn Around']
    print('Я бы посоветовал Вам:',random.choice(B))
  if advice==2:
    C=["Властелин колец","Гарри Поттер","Патриот","Головоломка 2","Технарь"]
    print("Я бы посоветовал Вам:",random.choice(C))
  if advice==3:
    D=["Оскар Уайльд 'Кантервильское привидение'","А.С.Пушкин 'Евгений Онегин'","М.Ю.Лермонтов 'Герой нашего времени'","Дж.Фаулз 'Коллекционер'","С.Моэм 'Маг'"]
    print('Я бы посоветовал Вам:',random.choice(D))
  if advice==4:
    E=["Engels Coffee","Французский пекарь","Simple Coffee","Intouch","Maccheroni"]
    print("Я бы посоветовал Вам:",random.choice(E))
  if advice==5:
    K=["Englex.ru","Duolingo.com","Englishspeak.com","Lingualeo.com","BBC Learning English"]
    print("Я бы посоветовал Вам:",random.choice(K))
if N==3:
  print("Ух ты, Вы правильно поступаете! День планировать необходимо! ")
  activities = input("Введите список дел, разделяя их запятой: ").split(',')
  count=0
  for activity in activities:
    count+=1
  list_of__activities=list(activities)
  todo_list=[]
  for i in range(count):
    todo_list.append(list_of__activities[i])
  print("Отлично! Подскажите, какую команду Вы бы хотели произвести? 1) Вывести список дел; 2) Обновить его; 3) Удалить какое-то дело?")
  number_of_list=int(input("Введите номер команды, которую Вы бы хотели произвести: "))
  if number_of_list==1:
    for i in range(count):
      print(i+1,")",todo_list[i])
  if number_of_list==2:
    count_of_todo = int(input("Сколько дел Вы бы хотели добавить? :)"))
    for i in range(count_of_todo):
        task = input("Какое дело Вы бы хотели добавить в свой список? :)")
        todo_list.append(task)
    count = len(todo_list)
    for i in range(count):
        print(i+1, ")", todo_list[i])
  if number_of_list==3:
    count_of_delete=int(input("Укажите количество дел, которые Вы хотите удалить: "))
    for i in range(count_of_delete):
      delete_number=int(input("Укажите, под каким номером находится у Вас в списке дело, которое Вы хотите удалить: "))
      del todo_list[delete_number - 1]
    print(todo_list)

"""# **Задача 4.**

Камень, ножницы, бумага

Создайте игру в Камень, ножницы, бумагу, в которой пользователь может играть против компьютера. Программа должна запросить выбор пользователя, а затем сгенерировать выбор компьютера. Затем программа должна определить победителя на основе правил игры.

**Этап 1:**

Определение победителя

**Этап 2:**
  
Игра до 3 побед


Ввод для "Этап 1":

```
Камень
```

Вывод:

```
Компьютер: Ножницы
Игрок: Камень
Победа: Игрок
```
"""

import random
print("Привет! Ну что, поиграем сегодня? :)")
commands=["Камень","Ножницы","Бумага"]
count_computer=0
count_you=0
while count_computer<3 and count_you<3:
  your_command=input("Введи свою команду (Камень/Ножницы/Бумага): ")
  computer_command=random.choice(commands)
  print("Компьютер: ",computer_command)
  print("Игрок: ", your_command)
  if your_command==computer_command:
    print("Победа: Нет.Ничья")
  elif ((your_command == "Ножницы" and computer_command == "Бумага")
        or (your_command == "Бумага" and computer_command == "Камень")
        or (your_command == "Камень" and computer_command == "Ножницы")
  ):
        print("Победа: Игрок")
        count_you += 1
  else:
    print("Победа: Компьютер")
    count_computer += 1

print("Игра окончена!")
if count_computer == 3:
  print("Победил компьютер!")
else:
   print("Победил игрок!")

"""# **Задача 5.**

Создайте игру "Палач" или "Виселица", в которой пользователь должен угадать слово, предлагая буквы. Программа должна выбрать случайное слово, а затем разрешить пользователю угадывать буквы. После каждого угадывания программа должна сообщать пользователю, есть ли в слове буква или нет.

**Этап 1**
Создать саму игру (игра должна иметь привлекательный интерфейс, соотвесвующий классической висилице)

**Этап 2:**
Ввести подсчет количества очков и ограничения на попытки

**Этап 3:** Добавить возможность сразу угадать слово
"""

import random
print("Добро пожаловать в игру 'Виселица!'")
words = ["мармелад", "город", "математика", "модуль", "кольцо", "фильм"]
word = random.choice(words)
hidden_word = [" _ "] * len(word)
guessed_letters = []
print("Сегодня Вам предстоит угадать следующее слово:", " ",hidden_word)
scores = 0
attempts = 6
print("Количество попыток: ", attempts)

while attempts > 0:
    letter = input("Введите букву или слово: ")
    if len(letter) == 1:
      if letter in guessed_letters:
          print("Вы уже вводили эту букву. Попробуйте другую.")
      elif letter in word:
          print("Буква есть в слове!")
          scores += 15
          print("Ваши очки: ", scores)
          for i in range(len(word)):
              if word[i] == letter:
                  hidden_word[i] = letter
          print("Угадайте слово:", hidden_word)
          guessed_letters.append(letter)
      else:
            print("Неверно!")
            attempts -= 1
            print("Количество оставшихся попыток:", attempts)
            print("Угадайте слово:", " ",hidden_word)
            guessed_letters.append(letter)
    elif len(letter) > 1:
        if letter == word:
            print("Поздравляю! Вы угадали слово!")
            break
        else:
            print("Неправильное слово.")
            attempts -= 1
            print("Количество оставшихся попыток:", attempts)
            print("Угадайте слово:", " ",hidden_word)

    if attempts == 0:
        print("Вы проиграли! Слово было:", word)

"""# **Дополнительно: Задача 6 (для тех, кто не сделал в прошлый раз)**

**Цифра на определенном месте:**

Последовательно записан натуральный ряд чисел.

Какая цифра стоит в N позиции


Вввод:

```
Введите номер позиции: 1234567890
```

Вывод:

```
8
```
"""

задача сделана на прошлой практике