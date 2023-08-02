import pytest


@pytest.fixture
def data_test():
    data_test_operations = [
        {
        "id": 179194306,
        "state": "EXECUTED",
        "date": "2019-05-19T12:51:49.023880",
        "operationAmount": {
          "amount": "6381.58",
          "currency": {
            "name": "USD",
            "code": "USD"
          }
        },
        "description": "Перевод организации",
        "from": "МИР 5211277418228469",
        "to": "Счет 58518872592028002662"
      },
      {
        "id": 921286598,
        "state": "EXECUTED",
        "date": "2018-03-09T23:57:37.537412",
        "operationAmount": {
          "amount": "25780.71",
          "currency": {
            "name": "руб.",
            "code": "RUB"
          }
        },
        "description": "Перевод организации",
        "from": "Счет 26406253703545413262",
        "to": "Visa Gold 3654412434951162"
      },
      {
        "id": 207126257,
        "state": "EXECUTED",
        "date": "2019-07-15T11:47:40.496961",
        "operationAmount": {
          "amount": "92688.46",
          "currency": {
            "name": "USD",
            "code": "USD"
          }
        },
        "description": "Открытие вклада",
        "to": "Счет 35737585785074382265"
      },
      {
        "id": 667307132,
        "state": "EXECUTED",
        "date": "2019-07-13T18:51:29.313309",
        "operationAmount": {
          "amount": "97853.86",
          "currency": {
            "name": "руб.",
            "code": "RUB"
          }
        },
        "description": "Перевод с карты на счет",
        "from": "Maestro 1308795367077170",
        "to": "Счет 96527012349577388612"
      },
      {
        "id": 661357102,
        "state": "EXECUTED",
        "date": "2013-04-17T20:23:39.393400",
        "operationAmount": {
            "amount": "13954.53",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод с карты на счет",
        "to": "Счет 93462876157363219875"
      }
    ]

    return data_test_operations
