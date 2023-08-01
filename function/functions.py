import json
from datetime import datetime
# import os

# DATA_OPERATIONS_PATH = os.path.join('../package.json')
# print(DATA_OPERATIONS_PATH)


def get_operations_data(path):
    # operations_data = open('..', 'package.json')
    # operations_data = json.load(operations_data)
    with open(path, 'r', encoding='UTF-8') as file:
        operations_data = json.load(file)
        # print(operations_data)
        # print(len(operations_data))
        # print(type(operations_data))
        # print(operations_data[0])
        # print(type(operations_data[0]))
        return operations_data


# operations_data = get_operations_data()


def get_executed_list(operations_data):
    executed_list = []
    for operation in operations_data:
        for key, value in operation.items():
            if operation[key] == 'EXECUTED':
                executed_list.append(operation)
                # print(executed_list)
                # return executed_list
    # print(executed_list)
    # print(len(executed_list))
    return executed_list


# executed_list = get_executed_list(get_operations_data())


def get_sort_executed_list(executed_list):
    def get_key_for_sort(operation):
        # print(operation['date'])
        return operation['date']
    # print(sorted(executed_list, key=get_key_for_sort, reverse=True))
    return sorted(executed_list, key=get_key_for_sort, reverse=True)


# get_sort_executed_list(get_executed_list(get_operations_data()))


def get_last_operations(operations_list, quantity_of_operations):
    # print(operations_list[0:5])
    return operations_list[0:5]


# get_last_operations(get_sort_executed_list(get_executed_list(get_operations_data())), 5)

def get_date_formatted(operation_date):
    date_formatted = datetime.strptime(operation_date, "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
    return date_formatted


# def get_from_to_formatted():
