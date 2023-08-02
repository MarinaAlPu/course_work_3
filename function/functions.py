import json
from datetime import datetime


def get_operations_data(path):
    """
    Получает данные о транзакциях из файла .json
    :param path: путь, по которому открывает файл для чтения
    :return: данные о транзакциях из файла .json
    """
    with open(path, 'r', encoding='UTF-8') as file:
        operations_data = json.load(file)
        return operations_data


def get_executed_list(operations_data, operation_key):
    """
    Получает из списка операций список операций в соответствии с определённым статусом
    :param operations_data: список всех операций
    :param operation_key: статус операций
    :return:  список операций с определённым статусом
    """
    executed_list = []
    for operation in operations_data:
        for key, value in operation.items():
            if operation[key] == operation_key:
                executed_list.append(operation)
    return executed_list


def get_sort_executed_list(executed_list, param_for_sort):
    """
    Сортирует список выполненных операций по определённому параметру по убыванию
    :param executed_list: список выполненных операций
    :param param_for_sort: параметр, по которому сортируется список
    :return: отсортированный по убыванию список выполненных операций
    """
    def get_key_for_sort(operation):
        return operation[param_for_sort]
    return sorted(executed_list, key=get_key_for_sort, reverse=True)


def get_last_operations(operations_list, quantity_of_operations):
    """
    Получает определённое количество последних операций
    :param operations_list: отсортированный по убыванию список выполненных операций
    :param quantity_of_operations: количество операций для вывода н аэкран
    :return: список операций, которые будут выведена на экран
    """
    return operations_list[0:quantity_of_operations]


def get_date_formatted(operation_date, as_is_format, to_be_format):
    """
    Форматирует дату, полученную из БД
    :param operation_date: дата из БД
    :param as_is_format:
    :param to_be_format:
    :return:  дата в нужном формате
    """
    date_formatted = datetime.strptime(operation_date, as_is_format).strftime(to_be_format)
    return date_formatted


def get_from_formatted(operation):
    """
    Получает источник, из которого была проведена операция
    :param operation: список операций
    :return: источник перевода
    """
    if 'from' in list(operation.keys()):
        if 'Счет' in operation['from']:
            from_where_value = operation['from'][-20:]
            from_where = f"{operation['from'][:-20:]} **{from_where_value[-4:]}"
            return f"{from_where} -> "
        else:
            from_where_value = operation['from'][-16:]
            from_where = f"{operation['from'][:-16]}{from_where_value[0: 4]} {from_where_value[4: 6]}** **** {from_where_value[-4:]}"
            return f"{from_where} -> "
    else:
        return ''


def get_to_formatted(operation):
    """
    Получает адресата перевода
    :param operation: список опреаций
    :return: получатель перевода
    """
    if 'Счет' in operation['to']:
        to_value = operation['to'][-20:]
        to = f"{operation['to'][:-20]} **{to_value[-4:]}"
        return to
    else:
        to_value = operation['to'][-16:]
        to = f"{operation['to'][:-16]}{to_value[0: 4]} {to_value[4: 6]}** **** {to_value[-4:]}"
        return to
