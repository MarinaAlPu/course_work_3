# import pytest
import os
# import function.functions
from function import functions


DATA_OPERATIONS_PATH = os.path.join('../package.json')
OPERATION_KEY = 'EXECUTED'
KEY_FOR_CHECK = 'state'
PARAM_FOR_SORT = 'date'
QUANTITY_OF_OPERATIONS = 5

def test_get_operations_data():
    assert isinstance(functions.get_operations_data(DATA_OPERATIONS_PATH), list) == True


def test_get_executed_list():
    assert isinstance(functions.get_executed_list(functions.get_operations_data(DATA_OPERATIONS_PATH), OPERATION_KEY), list) == True


def test_get_executed_list_by_key():
    executed_list_by_key = functions.get_executed_list(functions.get_operations_data(DATA_OPERATIONS_PATH), OPERATION_KEY)
    for operation in executed_list_by_key:
        # for key, value in operation.items():
        assert operation[KEY_FOR_CHECK] == OPERATION_KEY


# def get_sort_executed_list():
#     assert isinstance(functions.get_executed_list((functions.get_operations_data(DATA_OPERATIONS_PATH), OPERATION_KEY), PARAM_FOR_SORT), list) == True
    # sorted_list = functions.get_sort_executed_list(executed_list, PARAM_FOR_SORT)



