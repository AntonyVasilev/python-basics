"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
данных, можно использовать любую подходящую структуру, например словарь.
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на
уроках по ООП.
"""

from abc import ABC, abstractmethod


class MyException(Exception):
    def __init__(self, text):
        self.text = text


class Warehouse:

    goods = {}

    def __init__(self, name, address, phone, email, n_rows, n_levels, n_cells):
        """
        Класс Склад. Описывает основные характеристики склада хранения оргтехники
        :param name: Название склада
        :param address: адрес склада
        :param phone: номер телефона
        :param email: адрес электронной почты
        :param n_rows: количество рядов стеллажей
        :param n_levels: количество уровней хранения
        :param n_cells: количество ячеек хранения
        """
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        self.n_rows = n_rows
        self.n_levels = n_levels
        self.n_cells = n_cells

    def receipt(self, product, count, price, cell_number):
        """
        Метод, добавляющий товар на склад
        :param product: экземпляр класса Огртехника
        :param count: количество
        :param price: цена
        :param cell_number: номер ячейки, в которой будет хранится данный товар
        """
        self.goods[cell_number] = {
            'product': product,
            'count': count,
            'price': price}

    def issue(self, cell_number, count):
        """
        Метод для передачи товара в другие подразделения компании. Если товар передается частично, то уменьшает
        количество товара в ячейке. Если полностью, то удаляет его из указаной ячейки хранения
        :param cell_number: номер ячейки хранения
        :param count: количество передаваемого товара
        """
        if self.goods[cell_number]['count'] > count:
            self.goods[cell_number]['count'] -= count
        elif self.goods[cell_number]['count'] == count:
            self.goods.pop(count)
        else:
            print(f'Не достаточное количество товара {self.goods[cell_number]["product"].name} в ячейке '
                  f'{self.goods[cell_number]}. Отпуск товара невозможен!\nТекущий остаток: '
                  f'{self.goods[cell_number]["count"]}')

    def warehouse_balances(self):
        used_cells = self.goods.keys()
        empty_cells = set(range(1, len(self.n_cells))).symmetric_difference(set(self.goods.keys()))
        report_list = []
        for cell_num, product in self.goods:
            report_dict = {
                'used_cells': used_cells,
                'empty_cells': empty_cells,
                'product_name': product['product'].name,
                'count': product['count'],
                'price': product['price']}
            report_list.append(report_dict)
        return report_list


class OfficeEquipment(ABC):

    @abstractmethod
    def __init__(self, name, weight, dimensions, paper_format, connections):
        """
        Базовый класс Оргтехника
        :param name: Название
        :param weight: вес единицы товара
        :param dimensions: размеры товара
        :param paper_format: поддерживаемые размеры бумаги
        :param connections: поддерживаемые типы подключения
        """
        self.name = name
        self.weight = weight
        self.dimensions = dimensions
        self.paper_format = paper_format
        self.connections = connections


class Printer(OfficeEquipment):

    def __init__(self, name, weight, dimensions, paper_format, connections, print_speed, maximum_load):
        """
        Класс-наследник класса Оргтехника.
        :param print_speed: скорость печати (листов в минуту)
        :param maximum_load: максимальная нагрузка (страниц в месяц)
        """
        super().__init__(name, weight, dimensions, paper_format, connections)
        self.print_speed = print_speed
        self.maximum_load = maximum_load


class Scanner(OfficeEquipment):

    def __init__(self, name, weight, dimensions, paper_format, connections, scanner_type, scan_speed):
        """
        Класс-наследник класса Оргтехника.
        :param scanner_type: тип сканера
        :param scan_speed: скорость сканирования (страниц в минуту)
        """
        super().__init__(name, weight, dimensions, paper_format, connections)
        self.scanner_type = scanner_type
        self.scan_speed = scan_speed


class Copier(OfficeEquipment):

    def __init__(self, name, weight, dimensions, paper_format, connections, copier_type, copy_speed):
        """
        Класс-наследник класса Оргтехника.
        :param copier_type: тир копира
        :param copy_speed: скорость копирования (страниц в минуту)
        """
        super().__init__(name, weight, dimensions, paper_format, connections)
        self.copier_type = copier_type
        self.copy_speed = copy_speed


def create_warehouse() -> list:
    name = input('Введите название склада: ')
    address = input('Введите адрес склада: ')
    try:
        phone = input('Введите номер телефона(только цифры): ')
        if len(phone) < 10 and not phone.isalpha():
            raise MyException('Не корректный ввод номера телефона!')
        email = input('Введите email: ')
        if '@' not in email:
            raise MyException('Не корректный ввод email!')
        n_rows = int(input('Введите количество рядов стеллажей: '))
        n_levels = int(input('Введите количество уровней хранения: '))
        n_cells = int(input('Введите количество ячеек хранения: '))
    except (MyException, ValueError) as error:
        print(error)
    else:
        return [name, address, phone, email, n_rows, n_levels, n_cells]


def create_product(product_type: int):
    while True:
        try:
            name = input('Введите наименование устройства: ')
            weight = float(input('Введите вес устройства'))
            dimensions = input('Введите размеры устройства: ')
            paper_format = input('Введите поддерживаемые форматы документов: ')
            connections = input('Введите поддерживаемые типы подключения: ')
            if product_type == 1:
                print_speed = float(input('Введите скорость печати (листов в минуту): '))
                maximum_load = int(input('Введите максимальную нагрузку (страниц в месяц)'))
                return Printer(name, weight, dimensions, paper_format, connections, print_speed, maximum_load)
            elif product_type == 2:
                scanner_type = input('Введите тип сканера: ')
                scan_speed = float(input('Введите скорость сканирования (страниц в минуту): '))
                return Scanner(name, weight, dimensions, paper_format, connections, scanner_type, scan_speed)
            elif product_type == 3:
                copier_type = input('Введите тип копира: ')
                copy_speed = float(input('Введите скорость копирования (страниц в минуту): '))
                return Copier(name, weight, dimensions, paper_format, connections, copier_type, copy_speed)
        except ValueError as error:
            print(error)


if __name__ == '__main__':
    # Создание экземпляра объекта Склад
    wh_data = create_warehouse()
    try:
        wh = Warehouse(wh_data[0], wh_data[1], wh_data[2], wh_data[3], wh_data[4], wh_data[5], wh_data[6])
    except TypeError as err:
        print(err)
    else:
        while True:
            print('Меню:0. Выход\n1. Добавить товар на склад\n2. Передать товар со склада\n3. Вывести отчет')
            try:
                user_choice = int(input('Выберите действие: '))
            except ValueError:
                print('Ошибка ввода!')
                continue

            if user_choice == 0:
                try:
                    print('Вид товара:\n0. Назад\n1. Принтер\n2. Сканер\n3. Копир')
                    product_num = int(input('Введите вид товара: '))
                    if product_num < 0 or product_num >= 4:
                        raise MyException('Ошибка ввода! Такого товара не существует!')
                    count = int(input('Введите количество: '))
                    price = float(input('Введите стоимость: '))
                    cell_number = int(input('Введите номер ячейки: '))
                except (ValueError, MyException) as err1:
                    print(err1)
                    continue
                else:
                    wh.receipt(create_product(product_num), count, price, cell_number)
            elif user_choice == 1:
                pass
            elif user_choice == 2:
                pass
            elif user_choice == 3:
                pass
            else:
                print('Такого действия нет!')
