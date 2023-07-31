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
    # print(last_operations)

    count = 0
    while count < QUANTITY_OF_OPERATIONS:
        for operation in last_operations:
            operation_date = operation['date']
            description = operation['description']
            # from_where = operation['from']
            to = operation['to']
            amount = operation['operationAmount']['amount']
            currency = operation['operationAmount']['currency']['name']

            if 'from' in list(operation.keys()):
                from_where = operation['from']
                print(f'{operation_date} {description}\n{from_where} -> {to}\n{amount} {currency}\n')
                # count += 1

            else:
                print(f'{operation_date} {description}\n{to}\n{amount} {currency}\n')
            count += 1

        # print(list(operation.keys()))
    #
    #     print(operation_date)
    #     print(description)
    #     # print(from_where)
    #     print(to)
    #     print(amount)
    #     print(currency)
    #     print()
    #
    # # < дата перевода > < описание перевода >
    # # < откуда > -> < куда >
    # # < сумма перевода > < валюта >
    #
    # # Пример вывода для одной операции:
    # # 14.10.2018 Перевод организации
    # # Visa Platinum 7000 79 ** ** ** 6361 -> Счет ** 9638
    # # 82771.72 руб.


print(get_list_operations())
