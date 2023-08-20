import os.path

import json

import pytest

from crs.utils import data_json, get_executed_data, get_last_five, parse_operations_data


def test_file_exists():
    assert os.path.exists('test_operations.json'), f'Файл не нейден'

def test_data_json():
    file_name = "test_operations.json"
    expected_output = [{'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041', 'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'}, {'id': 41428829, 'state': 'asdagfew', 'date': '2019-07-03T18:35:29.512364', 'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'MasterCard 7158300734726758', 'to': 'Счет 35383033474447895560'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572', 'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'}, {'id': 587085106, 'state': 'EXECUTED', 'date': '2018-03-23T10:45:06.972075', 'operationAmount': {'amount': '48223.05', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Открытие вклада', 'to': 'Счет 41421565395219882431'}, {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878', 'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542', 'to': 'Счет 75651667383060284188'}]
    assert data_json(file_name) == expected_output
    assert isinstance(data_json('test_operations.json'), list)
    assert  len(data_json('test_operations.json')) == 5

    file_name = "nonexistent.json"
    with pytest.raises(FileNotFoundError):
        data_json(file_name)

def test_get_executed_data_only_executed():
    data = [
        {"state": "PENDING"},
        {"state": "EXECUTED"},
        {"state": "FAILED"}
    ]
    expected_result = [{"state": "EXECUTED"}]
    assert get_executed_data(data) == expected_result


def test_get_executed_data_empty_result():
    data = [
        {"state": "PENDING"},
        {"state": "FAILED"}
    ]
    expected_result = []
    assert get_executed_data(data) == expected_result


def test_get_executed_data_empty_input():
    data = []
    expected_result = []
    assert get_executed_data(data) == expected_result


def test_get_executed_data_large_dataset():
    data = [{"state": "EXECUTED"}] * 1000000
    expected_result = [{"state": "EXECUTED"}] * 1000000
    assert get_executed_data(data) == expected_result


def test_get_executed_data_invalid_input():
    data = [
        {"status": "PENDING"},
        {"status": "EXECUTED"},
        {"status": "FAILED"}
    ]
    expected_result = []
    assert get_executed_data(data) == expected_result


def test_get_last_five():
    executed_data = [
        {"date": "2022-01-01", "value": 1},
        {"date": "2022-01-02", "value": 2},
        {"date": "2022-01-03", "value": 3},
        {"date": "2022-01-04", "value": 4},
        {"date": "2022-01-05", "value": 5},
        {"date": "2022-01-06", "value": 6},
        {"date": "2022-01-07", "value": 7},
    ]

    result = get_last_five(executed_data)

    assert len(result) == 5

    assert result[0]["date"] == "2022-01-07"
    assert result[1]["date"] == "2022-01-06"
    assert result[2]["date"] == "2022-01-05"
    assert result[3]["date"] == "2022-01-04"
    assert result[4]["date"] == "2022-01-03"

    assert result[0]["value"] == 7
    assert result[1]["value"] == 6
    assert result[2]["value"] == 5
    assert result[3]["value"] == 4
    assert result[4]["value"] == 3


@pytest.fixture
def sample_data():
    return [
        {
            "id": 27192367,
            "state": "CANCELED",
            "date": "2018-12-24T20:16:18.819037",
            "operationAmount": {
                "amount": "991.49",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 71687416928274675290",
            "to": "Счет 87448526688763159781"
        },
        {
            "id": 176798279,
            "state": "CANCELED",
            "date": "2019-04-18T11:22:18.800453",
            "operationAmount": {
                "amount": "73778.48",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 90417871337969064865"
        }
    ]


def test_parse_operations_data(sample_data):
    result = parse_operations_data(sample_data)

    assert isinstance(result, list)
    assert len(result) == len(sample_data)
