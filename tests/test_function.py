import os
import pytest
from function import functions
import datetime

DATA_OPERATIONS_PATH = os.path.join(os.path.dirname(__file__), "..", 'package.json')
OPERATION_KEY = 'EXECUTED'
KEY_FOR_CHECK = 'state'
PARAM_FOR_SORT = 'date'
AS_IS_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"
TO_BE_FORMAT = "%d.%m.%Y"


def test_get_operations_data():
    assert isinstance(functions.get_operations_data(DATA_OPERATIONS_PATH), list) == True, "Метод get_operations_data вернул не список"


def test_get_executed_list(data_test):
    assert isinstance(functions.get_executed_list(data_test, OPERATION_KEY), list) == True, "Метод get_executed_list вернул не список"

    executed_list_by_key = functions.get_executed_list(data_test, 'EXECUTED')
    for operation in executed_list_by_key:
        assert operation[KEY_FOR_CHECK] == 'EXECUTED', "Список отфильтрован не по признаку 'EXECUTED'"

    executed_list_by_key = functions.get_executed_list(data_test, 'CANCELED')
    for operation in executed_list_by_key:
        assert operation[KEY_FOR_CHECK] == 'CANCELED', "Список отфильтрован не по признаку 'CANCELED'"


def test_get_sort_executed_list(data_test):
    assert isinstance(functions.get_sort_executed_list(data_test, PARAM_FOR_SORT), list) == True, "Метод get_sort_executed_list вернул не список"

    assert functions.get_sort_executed_list(data_test, PARAM_FOR_SORT)[0][PARAM_FOR_SORT]\
           > functions.get_sort_executed_list(data_test, PARAM_FOR_SORT)[-1][PARAM_FOR_SORT], "Список отсортирован не по убыванию"


def test_get_last_operations(data_test):
    assert isinstance(functions.get_last_operations(data_test, 3), list) == True, "Метод get_last_operations вернул не список"
    assert len(functions.get_last_operations(data_test, 4)) == 4, "Метод возвращает не заявленное количество элементов." \
                                                                  "Если количество элементов в полученном списке меньше," \
                                                                  "чем было запрошено, следует проверить длину исходного списка" \
                                                                  "- возможно, количество элементов в нём меньше числа запрашиваемых элементов"
    assert len(functions.get_last_operations(data_test, 1)) == 1, "Метод возвращает не заявленное количество элементов." \
                                                                  "Если количество элементов в полученном списке меньше," \
                                                                  "чем было запрошено, следует проверить длину исходного списка" \
                                                                  "- возможно, количество элементов в нём меньше числа запрашиваемых элементов"
    assert len(functions.get_last_operations(data_test, 0)) == 0, "Метод возвращает не заявленное количество элементов." \
                                                                  "Если количество элементов в полученном списке меньше," \
                                                                  "чем было запрошено, следует проверить длину исходного списка" \
                                                                  "- возможно, количество элементов в нём меньше числа запрашиваемых элементов"
    assert len(functions.get_last_operations(data_test, 15)) == 5, "Метод возвращает не заявленное количество элементов." \
                                                                  "Если количество элементов в полученном списке меньше," \
                                                                  "чем было запрошено, следует проверить длину исходного списка" \
                                                                  "- возможно, количество элементов в нём меньше числа запрашиваемых элементов"


def test_get_date_formatted():
    assert functions.get_date_formatted("2019-07-13T18:51:29.313309", AS_IS_FORMAT, TO_BE_FORMAT) == '13.07.2019', "Дата неотформатирована"
    assert functions.get_date_formatted("2017-12-10T18:51:29.3", AS_IS_FORMAT, TO_BE_FORMAT) == '10.12.2017', "Дата неотформатирована"

    with pytest.raises(ValueError) as error:
        functions.get_date_formatted("9999-99-99T18:51:29.3", AS_IS_FORMAT, TO_BE_FORMAT)
        functions.get_date_formatted("9999-99-99T18:51:29.313309", AS_IS_FORMAT, TO_BE_FORMAT)
        functions.get_date_formatted("0000-00-00T00:00:00.000000", AS_IS_FORMAT, TO_BE_FORMAT)
        functions.get_date_formatted("2019-07-13T99:99:99.999999", AS_IS_FORMAT, TO_BE_FORMAT)
        functions.get_date_formatted("2019-07-13T18:51:29", AS_IS_FORMAT, TO_BE_FORMAT)
        functions.get_date_formatted("2019-07-13 13:51:29.313309", AS_IS_FORMAT, TO_BE_FORMAT)
        functions.get_date_formatted("3019-39-75 18:46:29.313309", AS_IS_FORMAT, TO_BE_FORMAT)
        functions.get_date_formatted("2000.12.10j21:51:29.357310", AS_IS_FORMAT, TO_BE_FORMAT)
        functions.get_date_formatted("30/45/9345T21:51:29.357310", AS_IS_FORMAT, TO_BE_FORMAT)
        functions.get_date_formatted("2014-09-10", AS_IS_FORMAT, TO_BE_FORMAT)
        functions.get_date_formatted("пятое ноября 2016г.T21:51:29.357310", AS_IS_FORMAT, TO_BE_FORMAT)

    # try:
    #     datetime.date.fromisoformat("2014-09-10")
    # except ValueError:
    #     raise ValueError("Incorrect data format")


def test_get_from_formatted(data_test):
    assert functions.get_from_formatted(data_test[0]) == 'МИР 5211 27** **** 8469 -> ', "Номер карты / счёта отправителя замаскирован некорректным образом"
    assert functions.get_from_formatted(data_test[1]) == 'Счет  **3262 -> ', "Номер карты / счёта отправителя замаскирован некорректным образом"
    assert functions.get_from_formatted(data_test[2]) == '', "Номер карты / счёта отправителя замаскирован некорректным образом"
    assert functions.get_from_formatted(data_test[3]) == 'Maestro 1308 79** **** 7170 -> ', "Номер карты / счёта отправителя замаскирован некорректным образом"


def test_get_to_formatted(data_test):
    assert functions.get_to_formatted(data_test[1]) == 'Visa Gold 3654 41** **** 1162', "Номер карты / счёта получателя замаскирован некорректным образом"
    assert functions.get_to_formatted(data_test[4]) == 'Счет  **9875', "Номер карты / счёта получателя замаскирован некорректным образом"
