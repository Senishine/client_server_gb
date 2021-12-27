""" Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах. Написать
скрипт, автоматизирующий его заполнение данными. Для этого:
Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря
в файл orders.json. При записи данных указать величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
"""

import json


def write_order_to_json(item, quantity, price, buyer, date):
    with open('orders.json') as read_file:
        orders_dct = json.load(read_file)
        orders_dct['orders'].append({
            'item': item,
            'quantity': quantity,
            'price': price,
            'buyer': buyer,
            'date': date,
        })
    with open('orders.json', 'w') as out_file:
        json.dump(orders_dct, out_file, indent=4)


if __name__ == "__main__":
    write_order_to_json('Sofa', 15, 30000, 'Elba', '22.12.2020')
    write_order_to_json('Bed', 222, 70000, 'Angstrem', '01.01.2021')
    write_order_to_json('Armchair', 180, 16010, 'Maria', '06.07.2019')
    write_order_to_json('Table', 47, 5000, 'ITmanuf', '30.12.2020')