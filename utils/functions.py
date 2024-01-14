import json

from operator import itemgetter

import arrow

import datetime

from datetime import date


def open_json(file_name):
    """
    Загружает данные из файла json
    :param file_name: файл в формате json
    :return: данные файла
    """
    with open(file_name, 'r', encoding='utf-8') as file:
        data_in_python = json.loads(file.read())
        return data_in_python


def get_executed(operations_list):
    """
    Возвращает список с исполненным операциями
    :param operations_list: список с операциями
    :return: список с исполненными операциями
    """
    executed_operations = []
    for transaction in operations_list:
        if transaction.get('state') == 'EXECUTED':
            executed_operations.append(transaction)
    return executed_operations

def sort_by_data(executed_operations):
    """
    Сортирует список с исполенными операциями по дате
    :param executed_operations:
    :return:
    """
    sorted_operations = sorted(executed_operations, key=itemgetter('date'), reverse=True)[:5]
    return sorted_operations

def modify_date(date):
    """
    Переводит дату в необходимый формат
    :param date: дата в исходном формате
    :return: дата внужном формате
    """
    simple_date_time = arrow.get(date)
    modified_date = simple_date_time.date().strftime('%d.%m.%Y')
    return modified_date

def modify_bill(bill):
    """
    Скрывает счет или номер карты
    :param bill: счет или номер карты
    :return: счет или номер карты со скрытыми цифрами
    """
    if bill[:4] == "Счет":
        modified_bill = bill.replace(bill[-21:-4], ' **')
    else:
        modified_card_number = bill.replace(bill[-10:-4], '** **** ')
        modified_bill = modified_card_number[:-14] + ' ' + modified_card_number[-14:]
    return modified_bill

def transform_transaction(transaction):
    """
    преобразует информацию об операции в нужный вариант
    :param transaction: информация о транзакции
    :return: преобразованная информация
    """
    mod_date = modify_date(transaction['date'])
    send_to = modify_bill(transaction['to'])
    if transaction.get('from'):
        send_from = modify_bill(transaction['from'])
    else:
        send_from = "Внесение наличных"
    return f"{mod_date} {transaction['description']}\n{send_from} -> {send_to}\n{transaction["operationAmount"]['amount']} {transaction["operationAmount"]["currency"]["name"]}\n"

