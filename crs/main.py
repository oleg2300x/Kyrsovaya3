import json

from crs.utils import data_json, get_executed_data, get_last_five, parse_operations_data



def main():
    raw_data = data_json('/crs/test_operations.json')
    executed_data = get_executed_data(raw_data)
    five_operations = get_last_five(executed_data)
    parsed_operations_list = parse_operations_data(five_operations)
    # for operation_message in parsed_operations_list:
    #     print(operation_message)
    #     print()
    print(parsed_operations_list)

if __name__ == '__main__':
    main()