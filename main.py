import re
import asyncio



async def phone_number():
    phone = input('ведите номер телефона:')
    check_phone = re.search(r'7\s\d{10}', phone)
    await asyncio.sleep(2)

    if check_phone:
        await fio()
    else:
        print('Неправильно введено имя')
        await phone_number()

async def fio():
    choose_fio = input('Введите свои ФИО: ')
    check_fio = re.search(r'\D{1,999}\s\D{1,999}\s\D{1,999}', choose_fio)
    await asyncio.sleep(2)

    if check_fio:
        await mail()
    else:
        print('Неправильно введено имя')
        await fio()

async def check_old():
    age = int(input('Введите свой возраст'))
    if age >= 2007:
        await new_menu()
    else:
        await old_menu()

async def old_menu():
    print('Вы выбрали меню для маленького любителя пиццы')
    print("У нас стартовала акция кастомная пицца. Напишите ингредиенты для пиццы через запятую.")
    print('Вы можете выбрать ингридиенты такие как: Пепперони, Сыр, Кетчуп, Майонез, Лосось, Секретный ингридиент')
    ingredients = input('Введите 5 ингредиентов для пиццы ЧЕРЕЗ ЗАПЯТУЮ: ')
    check_ingredients = re.search(r'.{1,999},.{1,999},.{1,999},.{1,999},.{1,999}', ingredients)

async def new_menu():
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


async def mail():
    choose_mail = input('Введите свой емейл: ')
    check_mail = re.search(r'.{1,999}@.{1,999}ru', choose_mail)
    await asyncio.sleep(2)

    if check_mail:
        await order()
    else:
        print('Неправильно введена почта')
        await mail()

async def main():
    await phone_number()
    print("\n" + "=" * 50 + "\n")




async def prepare_order():
    print('Заказ готовится')
    await asyncio.sleep(4)
    print('Всё готово! С вашей карты было снято 999 рублей! Приходите ещё!')


async def order():
    data = input('Введите свою дату рождения: Пример: 66/66/6666: ')
    check_data = re.search(r'\d{2}/\d{2}/\d{4}', data)

    if check_data:
        await new_menu()
    else:
        print('Неправильный формат даты')
        await order()


asyncio.run(main())