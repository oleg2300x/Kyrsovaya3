import os.path

from crs.utils import data_json, get_executed_data, get_last_five

def test_file_exists():
    assert os.path.exists('test_operations.json'), f'Файл не нейден'


def test_data_json():
    file = data_json('test_operations.json')
    assert isinstance(file, list)
    assert len(file) == 5


def test_get_executed_data():
    file = data_json('test_operations.json')
    result = get_executed_data(file)
    for i in result:
        assert i['state'] == 'EXECUTED'
    expected_length = 4
    assert len(result) == expected_length


def test_get_last_five():
    file = get_executed_data(data_json('test_operations.json'))
    result = get_last_five(file)
    assert result == [{'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041',
                       'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                       'description': 'Перевод организации', 'from': 'Maestro 1596837868705199',
                       'to': 'Счет 64686473678894779589'},
                      {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878',
                       'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}},
                       'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542',
                       'to': 'Счет 75651667383060284188'},
                      {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572',
                       'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},
                       'description': 'Перевод организации', 'from': 'Счет 75106830613657916952',
                       'to': 'Счет 11776614605963066702'},
                      {'id': 587085106, 'state': 'EXECUTED', 'date': '2018-03-23T10:45:06.972075',
                       'operationAmount': {'amount': '48223.05', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                       'description': 'Открытие вклада', 'to': 'Счет 41421565395219882431'}]


def test_paste_operations_data():
    file = get_last_five(get_executed_data(data_json('test_operations.json')))
    assert file[0]['date'] == '2019-08-26T10:50:58.294041'
    assert file == [{'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041',
                     'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                     'description': 'Перевод организации', 'from': 'Maestro 1596837868705199',
                     'to': 'Счет 64686473678894779589'},
                    {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878',
                     'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}},
                     'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542',
                     'to': 'Счет 75651667383060284188'},
                    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572',
                     'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},
                     'description': 'Перевод организации', 'from': 'Счет 75106830613657916952',
                     'to': 'Счет 11776614605963066702'},
                    {'id': 587085106, 'state': 'EXECUTED', 'date': '2018-03-23T10:45:06.972075',
                     'operationAmount': {'amount': '48223.05', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                     'description': 'Открытие вклада', 'to': 'Счет 41421565395219882431'}]