import re
import asyncio

user_data = {} #создаём список для данных пользователя

async def phone_number(): #Функция запроса и проверки номера телефона
    phone = input('ведите номер телефона:')
    check_phone = re.search(r'7\s\d{10}', phone)
    await asyncio.sleep(2)

    if check_phone:
        user_data['phone'] = phone
        await fio()
    else:
        print('Неправильно введено имя')
        await phone_number()

async def fio(): #Функция для запроса и проверки ФИО
    choose_fio = input('Введите свои ФИО: ') 
    check_fio = re.search(r'\D{1,999}\s\D{1,999}\s\D{1,999}', choose_fio)
    await asyncio.sleep(2)

    if check_fio:
        user_data['fio'] = choose_fio
        await mail()
    else:
        print('Неправильно введено имя')
        await fio()

async def check_old(): #Функция проверки возраста
    age = int(input('Введите свой возраст'))
    if age <= 10:
        user_data['age'] = age
        await new_menu()
    else:
        await old_menu()

async def old_menu(): #Меню для взрослых любителей пиццы
    print('Вы выбрали меню для взрослого любителя пиццы')
    print("У нас стартовала акция кастомная пицца. Напишите ингредиенты для пиццы через запятую.")
    print('Вы можете выбрать ингридиенты такие как: Пепперони, Сыр, Кетчуп, Майонез, Лосось, Секретный ингридиент')
    ingredients = input('Введите 5 ингредиентов для пиццы ЧЕРЕЗ ЗАПЯТУЮ: ')
    check_ingredients = re.search(r'.{1,999},.{1,999},.{1,999},.{1,999},.{1,999}', ingredients)

    if check_ingredients:
        print("Принято")
        await asyncio.sleep(2)
        await prepare_order()
    else:
        print('Не можем понять запись')
        await old_menu()


async def new_menu(): #Меню для маленьких любителей пиццы
    print('Вы выбрали меню для маленького любителя пиццы')
    print("У нас стартовала акция кастомная пицца. Напишите ингредиенты для пиццы через запятую.")
    print('Вы можете выбрать ингридиенты такие как: Пепперони, Сыр, Мёртвый цыплёнок, Живой цыплёнок, Те кто улыбается в уникуме, Кетчуп, Майонез')
    ingredients = input('Введите 5 ингредиентов для пиццы ЧЕРЕЗ ЗАПЯТУЮ: ')
    check_ingredients = re.search(r'.{1,999},.{1,999},.{1,999},.{1,999},.{1,999}', ingredients)

    if check_ingredients:
        print("Принято")
        await asyncio.sleep(2)
        await prepare_order()
    else:
        print('Не можем понять запись')
        await new_menu()


async def mail(): #Функция проверки почты
    choose_mail = input('Введите свой емейл: ')
    check_mail = re.search(r'.{1,999}@.{1,999}ru', choose_mail)
    await asyncio.sleep(2)

    if check_mail:
        user_data['mail'] = choose_mail
        await order()
    else:
        print('Неправильно введена почта')
        await mail()

async def main(): #Главная функция для запуска других
    await phone_number()
    print("\n" + "*" * 50 + "\n")

async def save_data():
    with open('user_data.txt', 'a', encoding='utf-8') as file:
        file.write('Данные пользователя\n')

        for i, j in user_data.items():
            file.write(f'{i}: {j}\n')

async def prepare_order(): #Готовка заказа
    print('Заказ готовится')
    await asyncio.sleep(4)
    print('Всё готово! С вашей карты было снято 999 рублей! Приходите ещё!')
    await save_data()


async def order(): #Подготовка к заказу (запрос даты)
    data = input('Введите свою дату рождения: Пример: 66/66/6666: ')
    check_data = re.search(r'\d{2}/\d{2}/\d{4}', data)

    if check_data:
        user_data['data'] = data
        await check_old()
    else:
        print('Неправильный формат даты')
        await order()


asyncio.run(main()) #Запуск главной функции

