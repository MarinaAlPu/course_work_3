import os
from datetime import date
from function.functions import *


DATA_OPERATIONS_PATH = os.path.join('package.json')
QUANTITY_OF_OPERATIONS = 5


def get_list_operations():
    operations_data = get_operations_data(DATA_OPERATIONS_PATH)
    executed_list = get_executed_list(operations_data)
    sort_executed_list = get_sort_executed_list(executed_list)
    last_operations = get_last_operations(sort_executed_list, QUANTITY_OF_OPERATIONS)

    count = 0
    while count < QUANTITY_OF_OPERATIONS:
        for operation in last_operations:
            operation_date = get_date_formatted(operation['date'])
            description = operation['description']
            from_where = get_from_formatted(operation)
            # print(operation)
            to = get_to_formatted(operation)
            # print(operation)
            # print(type(operation))
            # print(to)
            amount = operation['operationAmount']['amount']
            currency = operation['operationAmount']['currency']['name']

            # if 'from' in list(operation.keys()):
            #     # from_where = operation['from']
            #     if 'Счет' in operation['from']:
            #         from_where_value = operation['from'][-20:]
            #         from_where = f"{operation['from'][:-20:]} **{from_where_value[-4:]}"
            #         print(f'{operation_date} {description}\n{from_where} -> {to}\n{amount} {currency}\n')
            #         return f'{operation_date} {description}\n{from_where} -> {to}\n{amount} {currency}\n'
            #     else:
            #         from_where_value = operation['from'][-16:]
            #         from_where = f"{operation['from'][:-16]} {from_where_value[0: 4]} {from_where_value[4: 6]} ** **** {from_where_value[-4:]}"
            print(f'{operation_date} {description}\n{from_where}{to}\n{amount} {currency}\n')
            #         return f'{operation_date} {description}\n{from_where} -> {to}\n{amount} {currency}\n'
            #
            # else:
            #     print(f'{operation_date} {description}\n{to}\n{amount} {currency}\n')
            count += 1

    # # < дата перевода > < описание перевода >
    # # < откуда > -> < куда >
    # # < сумма перевода > < валюта >

    # # Пример вывода для одной операции:
    # # 14.10.2018 Перевод организации
    # # Visa Platinum 7000 79 ** **** 6361 -> Счет ** 9638
    # # 82771.72 руб.


get_list_operations()
