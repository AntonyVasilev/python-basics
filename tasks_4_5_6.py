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

    def __init__(self, name, address, phone, email, n_cells):
        """
        Класс Склад. Описывает основные характеристики склада хранения оргтехники
        :param name: Название склада
        :param address: адрес склада
        :param phone: номер телефона
        :param email: адрес электронной почты
        :param n_cells: количество ячеек хранения
        """
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        self.n_cells = n_cells

    @staticmethod
    def _create_product(product_type: int):
        """
        Запрашивает у пользователя данные и возвращает экземпляр класса-наследника класса Оргтехника
        :param product_type: тип класса Оргтехника: 1 - принтер, 2 - сканер, 3 - копир
        :return: экземпляр класса-наследника класса Оргтехника
        """
        print()
        while True:
            try:
                name = input('Введите наименование устройства: ')
                weight = float(input('Введите вес устройства: '))
                dimensions = input('Введите размеры устройства: ')
                paper_format = input('Введите поддерживаемые форматы документов: ')
                connections = input('Введите поддерживаемые типы подключения: ')
                if product_type == 1:
                    print_speed = float(input('Введите скорость печати (листов в минуту): '))
                    maximum_load = int(input('Введите максимальную нагрузку (страниц в месяц): '))
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

    def receipt(self, product_type, product=None, prod_quantity=None, prod_price=None, cell_num=None):
        """
        Метод, добавляющий товар на склад. По-умолчанию параметры prod_quantity, prod_price и new_sell_num
        запрашиваются у пользователя напрямую в методе, но при необходимости можно передать их при вызове метода.
        :param product_type: тип класса Оргтехника: 1 - принтер, 2 - сканер, 3 - копир
        :param product: экземпляр класса Оргтехника
        :param prod_quantity: количество
        :param prod_price: цена
        :param cell_num: номер ячейки, в которой будет хранится данный товар
        """
        if len(self.goods.keys()) < self.n_cells:
            if product is None:
                product = self._create_product(product_type)
            if prod_quantity is None:
                prod_quantity = int(input('Введите количество: '))
            if prod_price is None:
                prod_price = float(input('Введите стоимость: '))
            if cell_num is None:
                cell_num = int(input('Введите номер ячейки: '))
            if cell_num not in self.goods.keys():
                self.goods[cell_num] = {
                    'product': product,
                    'quantity': prod_quantity,
                    'price': prod_price}
                # Дополнительная проверка, чтобы предупредить пользователя, что он занял последнюю свободную ячейку
                if len(self.goods.keys()) == self.n_cells:
                    print('На складе не осталось свободных ячеек!')
            else:
                print(f'Данная ячейка занята!\nСписок занятых ячеек:{list(self.goods.keys())}')
                try:
                    new_sell_num = int(input('Введите номер ячейки: '))
                except ValueError as error:
                    print(error)
                else:
                    self.receipt(product_type, product, prod_quantity, prod_price, new_sell_num)
        else:
            print('Все ячейки заняты, добавление не возможно!')

    def issue(self, cell_num, prod_quantity):
        """
        Метод для передачи товара в другие подразделения компании. Если товар передается частично, то уменьшает
        количество товара в ячейке. Если полностью, то удаляет его из указаной ячейки хранения
        :param cell_num: номер ячейки хранения
        :param prod_quantity: количество передаваемого товара
        """
        if cell_num in self.goods.keys():
            if self.goods[cell_num]['quantity'] > prod_quantity:
                self.goods[cell_num]['quantity'] -= prod_quantity
            elif self.goods[cell_num]['quantity'] == prod_quantity:
                self.goods.pop(cell_num)
            else:
                print(f'Не достаточное количество товара {self.goods[cell_num]["product"].name} в ячейке '
                      f'{cell_num}. Отпуск товара невозможен!\nТекущий остаток: '
                      f'{self.goods[cell_num]["quantity"]}')
        else:
            print(f'Данная ячейка пустая. Список занятых ячеек: {list(self.goods.keys())}')
            try:
                new_cell_num = int(input('Введите номер ячейки или 0 для отмены: '))
            except ValueError as error:
                print(error)
            else:
                if new_cell_num == 0:
                    return
                else:
                    self.issue(new_cell_num, prod_quantity)

    def _warehouse_balances(self):
        """
        Формирует словарь с товарами, хранящимися на складе
        :return: список со словарями,
        """
        report_list = []
        for cell_num, product in self.goods.items():
            report_dict = {
                'cell_num': cell_num,
                'product_name': product['product'].name,
                'quantity': product['quantity'],
                'price': product['price']}
            report_list.append(report_dict)
        return report_list

    def get_warehouse_balances(self):
        """
        Выводит в терминал отчет об остатках товаров на складе
        """
        report = self._warehouse_balances()
        print(f'\nКоличество занятых ячеек: {len(self.goods.keys())}')
        print(f'Количество свободных ячеек: {self.n_cells - len(self.goods.keys())}')
        for product in report:
            print(f'Номер ячейки: {product["cell_num"]}, наименование: {product["product_name"]}, '
                  f'количество: {product["quantity"]}, цена: {product["price"]}')

    @classmethod
    def create_warehouse(cls):
        """
        Создает экземпляр класса Warehouse
        :return: экземпляр класса
        """
        name = input('Введите название склада: ')
        address = input('Введите адрес склада: ')
        try:
            phone = input('Введите номер телефона(только цифры): ')
            if len(phone) < 10 and not phone.isnumeric():
                raise MyException('Не корректный ввод номера телефона!')
            email = input('Введите email: ')
            if '@' not in email:
                raise MyException('Не корректный ввод email!')
            n_cells = int(input('Введите количество ячеек хранения: '))
        except (MyException, ValueError) as error:
            print(error)
            return
        else:
            return cls(name, address, phone, email, n_cells)


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


def start():
    """
    Функция, выполняющая программу
    """
    # Создание экземпляра объекта Склад
    wh = Warehouse.create_warehouse()
    if wh is None:
        return

    else:
        while True:
            print('\nМеню:\n0. Выход\n1. Добавить товар на склад\n2. Передать товар со склада\n3. Вывести отчет')
            user_choice = input('Выберите действие: ')

            if user_choice == '0':
                return
            elif user_choice == '1':
                try:
                    print('\nВид товара:\n0. Назад\n1. Принтер\n2. Сканер\n3. Копир')
                    product_num = int(input('Введите вид товара: '))
                    if product_num < 0 or product_num >= 4:
                        raise MyException('Ошибка ввода! Такого товара не существует!')
                except (ValueError, MyException) as err1:
                    print(err1)
                    continue
                else:
                    if product_num == 0:
                        continue
                    wh.receipt(product_num)
            elif user_choice == '2':
                try:
                    cell_number = int(input('Введите номер ячейки: '))
                    quantity = int(input('Введите количество: '))
                except ValueError as err2:
                    print(err2)
                else:
                    wh.issue(cell_number, quantity)
            elif user_choice == '3':
                wh.get_warehouse_balances()
            else:
                print('Такого действия нет!')


if __name__ == '__main__':
    start()
