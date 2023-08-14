import json


def data_json(file_name):
    with open(file_name, 'r', encoding='UTF-8') as file:
        filejson = json.load(file)
        return filejson


def get_state(data):
    executed_operations = []
    for i in data:
        if i.get('state'):
            if i["state"] == 'EXECUTED':
                executed_operations.append(i)
    return executed_operations


def last_five_operations(executed_data):
    sorted_operations = sorted(executed_data, key=lambda x: x["date"], reverse=True)
    last_five = sorted_operations[0:5]
    return last_five


def all_data(last_five):
    list_of_data = []
    for i in last_five:
        date = i.get('date')
        formated_date = date.replace('-', '.')
        description = i.get('description')
        operations_amount = i['operationAmount']['amount']
        currency = i['operationAmount']['currency']['name']
        to_ = i['to']
        if i.get('from') is None:
            from_ = ''.join('NoName')
        else:
            from_ = i['from']
            card_from = from_.split(' ')[-1]
            star_card = card_from[0:7] + len(card_from[7:14]) * '*' + card_from[-4:]

            # print(f'{formated_date},{description},{operations_amount}, {currency}, {to_}, {from_}')
            print(star_card)


gtx = data_json('operations.json')
gtx1 = get_state(gtx)
gtx2 = last_five_operations(gtx1)
# print(gtx2)
# for i in gtx2:
#     print(i)
all_data(gtx2)
