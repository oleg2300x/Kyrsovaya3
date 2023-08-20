import json


def data_json(file_name):
    with open(file_name, 'r', encoding='UTF-8') as file:
        filejson = json.load(file)
        return filejson


def get_executed_data(data):
    executed_operations = []
    for i in data:
        if i.get('state'):
            if i["state"] == 'EXECUTED':
                executed_operations.append(i)
    return executed_operations


def get_last_five(executed_data):
    sorted_operations = sorted(executed_data, key=lambda x: x["date"], reverse=True)
    last_five = sorted_operations[0:5]
    return last_five


def parse_operations_data(last_five):
    list_of_data = []
    for operation_data in last_five:
        date = operation_data.get('date').split('T')[0]
        formatted_date = '.'.join(date.split('-')[::-1])
        description = operation_data.get('description')
        operations_amount = operation_data['operationAmount']['amount']
        currency = operation_data['operationAmount']['currency']['name']
        card_to = operation_data.get('to').split()[-1]
        card_type_to = ' '.join(operation_data.get('to').split()[:-1])
        star_card_to = '*' * 2 + card_to[-4:]
        if operation_data.get('from') is None:
            star_card_from = 'NoName'
            card_type_from = ''
        else:
            card_type_from = ' '.join(operation_data.get('from').split()[:-1])
            type_card = operation_data.get('from').split()[0]
            if type_card in 'Счет':
                card_number = operation_data.get('from').split()[-1]
                star_card_from = f' {"*" * 2}{card_number[-4:]}'
            else:
                card_number = operation_data.get('from').split()[-1]
                star_card_from = f' {card_number[0:4]} {card_number[4:6]}** **** {card_number[-4:]}'

        list_of_data.append(f'''{formatted_date} {description}
{card_type_from}{star_card_from} -> {card_type_to} {star_card_to}
{operations_amount} {currency}''')

    return list_of_data

