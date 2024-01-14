from utils.functions import open_json, get_executed, sort_by_data, transform_transaction

def main():
    """
    Основной код проекта
    :return: пять последних операций в нужном формате
    """
    all_transactions = open_json("operations.json")
    executed_transactions = get_executed(all_transactions)
    last_sorted_transactions = sort_by_data(executed_transactions)
    for transaction in last_sorted_transactions:
        transformed_transaction = transform_transaction(transaction)
        print(transformed_transaction)


if __name__ == '__main__':
    main()