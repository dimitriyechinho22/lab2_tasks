"""
Lab2, second task
"""

import json
import pprint

def read_file() -> list:
    """
    Function that reads the file and returns list
    """
    with open('twitter1 (2).json', 'r', encoding='utf-8') as file:
        info = json.load(file)
    return info


def analyzing_the_dict(main_dict_new):
    """
    Analazying the dict and return what user needs.
    :param main_dict_new: list from json
    :return: the needed str
    """
    if type(main_dict_new) == list:
        main_dict_new = read_file()
        while True:
            try:
                print('What kind of data would you like to have?(index of list)?')
                user_response = input()
                if user_response not in '0123456789' or len(main_dict_new) < int(user_response):
                    print('Write correcttly\n')
                else:
                    break
            except:
                continue
        main_dict_new = main_dict_new[int(user_response)]
        pprint.pprint(main_dict_new)
        print('There are the keys that follows you to the info you can use: \n')
        main_dict_keys = main_dict_new.keys()
        print(main_dict_keys)
        print('\n')
        while True:
                print('Which one do you need?')
                user_response_1 = input()
                if user_response_1 not in list(main_dict_keys):
                    print('Write something that we have')
                else:
                    break
        if type(main_dict_new[user_response_1]) == dict:
            analyzing_the_dict(main_dict_new[user_response_1])
        elif type(main_dict_new[user_response_1]) == list:
            if main_dict_new[user_response_1][0] == dict:
                analyzing_the_dict(main_dict_new[user_response_1][0])
        else:
            print(main_dict_new[user_response_1])
    else:
        pprint.pprint(main_dict_new)
        print('There are the keys that follows you to the info you can use: \n')
        main_dict_keys = main_dict_new.keys()
        print(main_dict_keys)
        print('\n')
        while True:
                print('Which one do you need?')
                user_response_1 = input()
                if user_response_1 not in list(main_dict_keys):
                    print('Write something that we have?')
                else:
                    break
        if type(main_dict_new[user_response_1]) == dict:
            analyzing_the_dict(main_dict_new[user_response_1])
        elif type(main_dict_new[user_response_1]) == list:
            if type(main_dict_new[user_response_1][0]) == dict:
                analyzing_the_dict(main_dict_new[user_response_1][0])
        else:
            print(main_dict_new[user_response_1])

if __name__ == '__main__':
    analyzing_the_dict(read_file())
