import os
from function.functions import *


DATA_OPERATIONS_PATH = os.path.join('package.json')
OPERATION_KEY = 'EXECUTED'
PARAM_FOR_SORT = 'date'
QUANTITY_OF_OPERATIONS = 5
AS_IS_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"
TO_BE_FORMAT = "%d.%m.%Y"


def get_list_operations():
    operations_data = get_operations_data(DATA_OPERATIONS_PATH)
    executed_list = get_executed_list(operations_data, OPERATION_KEY)
    sort_executed_list = get_sort_executed_list(executed_list, PARAM_FOR_SORT)
    last_operations = get_last_operations(sort_executed_list, QUANTITY_OF_OPERATIONS)

    count = 0
    while count < QUANTITY_OF_OPERATIONS:
        for operation in last_operations:
            operation_date = get_date_formatted(operation['date'], AS_IS_FORMAT, TO_BE_FORMAT)
            description = operation['description']
            from_where = get_from_formatted(operation)
            to = get_to_formatted(operation)
            amount = operation['operationAmount']['amount']
            currency = operation['operationAmount']['currency']['name']

            print(f'{operation_date} {description}\n{from_where}{to}\n{amount} {currency}\n')
            count += 1


get_list_operations()
