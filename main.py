import re
import asyncio



async def phone_number():
    phone = input('ведите номер телефона:')
    check_phone = re.search(r'7\s\d{10}', phone)
    await asyncio.sleep(3)
    print(check_phone[0] if check_phone else 'Это иноагентский номер')
    await fio()

async def fio():
    choose_fio = input('Введите свои ФИО: ')
    check_fio = re.search(r'\D{1,999}\s\D{1,999}\s\D{1,999}', choose_fio)
    print(check_fio[0] if check_fio else 'Вы пожелали остаться безымянными')
    await mail()

async def mail():
    choose_mail = input('Введите свой емейл: ')
    check_mail = re.search(r'.{1,999}@.{1,999}ru', choose_mail)
    print(check_mail[0] if check_mail else 'Вы пожелали иноагентский емейл')

async def main():
    await phone_number()
    print("\n" + "=" * 50 + "\n")
    await order()


async def process_ingredients():
    print("У нас стартовала акция кастомная пицца. Напишите ингредиенты для пиццы через запятую.")
    ingredients = input('Введите 5 ингредиентов для пиццы ЧЕРЕЗ ЗАПЯТУЮ: ')
    check_ingredients = re.search(r'\S{1,999},\S{1,999},\S{1,999},\S{1,999},\S{1,999}', ingredients)

    if check_ingredients:
        print("Принято")
        await asyncio.sleep(2)
        return True
    else:
        print('Не можем понять запись')
        return False


async def prepare_order():
    print('Заказ готовится')
    await asyncio.sleep(4)
    print('Всё готово')


async def order():
    data = input('Введите свою дату рождения: Пример: 66/66/6666: ')
    check_data = re.search(f'\\d{2}/\\d{2}/\\d{4}', data)

    if check_data:
        last_four_chars = data[-4:]
        try:
            birth_year = int(last_four_chars)
            print(f"Год рождения: {birth_year}")

            if await process_ingredients():

                await prepare_order()
            else:
                print("Ошибка в заказе")

        except ValueError:
            print("Ошибка: неверный формат года")
    else:
        print("Неверный формат даты")


if __name__ == '__main__':
    asyncio.run(main())