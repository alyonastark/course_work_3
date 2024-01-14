import pytest

from utils.functions import get_executed, sort_by_data, modify_date, modify_bill, transform_transaction

@pytest.fixture
def example():
    return [  {
    "id": 893507143,
    "state": "EXECUTED",
    "date": "2018-02-03T07:16:28.366141",
    "operationAmount": {
      "amount": "90297.21",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 37653295304860108767"
  },
  {
    "id": 710136990,
    "state": "CANCELED",
    "date": "2018-08-17T03:57:28.607101",
    "operationAmount": {
      "amount": "66906.45",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1913883747791351",
    "to": "Счет 11492155674319392427"
  },
  {
    "id": 390558607,
    "state": "EXECUTED",
    "date": "2019-02-12T00:08:07.524972",
    "operationAmount": {
      "amount": "16796.95",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 72645194281643232984",
    "to": "Счет 95782287258966264115"
  },
  {
    "id": 902831954,
    "state": "EXECUTED",
    "date": "2018-04-22T17:01:46.885252",
    "operationAmount": {
      "amount": "84732.61",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Visa Platinum 3530191547567121",
    "to": "Счет 46878338893256147528"
  },
  {
    "id": 86608620,
    "state": "EXECUTED",
    "date": "2019-08-16T04:23:41.621065",
    "operationAmount": {
      "amount": "6004.00",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод с карты на счет",
    "from": "MasterCard 8826230888662405",
    "to": "Счет 96119739109420349721"
  },
    {}
   ]

def test_get_executed(example):
  assert get_executed(example) == [  {
    "id": 893507143,
    "state": "EXECUTED",
    "date": "2018-02-03T07:16:28.366141",
    "operationAmount": {
      "amount": "90297.21",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 37653295304860108767"
  },
  {
    "id": 390558607,
    "state": "EXECUTED",
    "date": "2019-02-12T00:08:07.524972",
    "operationAmount": {
      "amount": "16796.95",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 72645194281643232984",
    "to": "Счет 95782287258966264115"
  },
  {
    "id": 902831954,
    "state": "EXECUTED",
    "date": "2018-04-22T17:01:46.885252",
    "operationAmount": {
      "amount": "84732.61",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Visa Platinum 3530191547567121",
    "to": "Счет 46878338893256147528"
  },
  {
    "id": 86608620,
    "state": "EXECUTED",
    "date": "2019-08-16T04:23:41.621065",
    "operationAmount": {
      "amount": "6004.00",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод с карты на счет",
    "from": "MasterCard 8826230888662405",
    "to": "Счет 96119739109420349721"
  },
  ]

def test_sort_by_data(example):
  executed_operations = get_executed(example)
  assert sort_by_data(executed_operations) == [  {
    "id": 86608620,
    "state": "EXECUTED",
    "date": "2019-08-16T04:23:41.621065",
    "operationAmount": {
      "amount": "6004.00",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод с карты на счет",
    "from": "MasterCard 8826230888662405",
    "to": "Счет 96119739109420349721"
  },
  {
    "id": 390558607,
    "state": "EXECUTED",
    "date": "2019-02-12T00:08:07.524972",
    "operationAmount": {
      "amount": "16796.95",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 72645194281643232984",
    "to": "Счет 95782287258966264115"
  },
  {
    "id": 902831954,
    "state": "EXECUTED",
    "date": "2018-04-22T17:01:46.885252",
    "operationAmount": {
      "amount": "84732.61",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Visa Platinum 3530191547567121",
    "to": "Счет 46878338893256147528"
  },
  {
    "id": 893507143,
    "state": "EXECUTED",
    "date": "2018-02-03T07:16:28.366141",
    "operationAmount": {
      "amount": "90297.21",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 37653295304860108767"
  }
  ]

def test_modify_date(example):
  assert modify_date(example[0]['date']) == '03.02.2018'
  assert modify_date(example[3]['date']) == '22.04.2018'

def test_modify_bill(example):
  assert modify_bill(example[0]['to']) == "Счет **8767"
  assert modify_bill(example[1]['from']) == "Maestro 1913 88** **** 1351"

def test_transform_transaction(example):
  assert transform_transaction(example[0]) == "03.02.2018 Открытие вклада\nВнесение наличных -> Счет **8767\n90297.21 руб.\n"
  assert transform_transaction(example[2]) == "12.02.2019 Перевод организации\nСчет **2984 -> Счет **4115\n16796.95 USD\n"

