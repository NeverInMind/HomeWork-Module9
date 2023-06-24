
MEMORY = {}


def hello(val):
    return 'How can I help you?'


def add(val):
    str_to_obj = val.split(' ')
    if str_to_obj[0] in MEMORY:
        return 'Name already in Contacts'
    test_obj = {str_to_obj[0]: str_to_obj[1]}
    MEMORY.update(test_obj)
    return 'New contact added'


def change(val):
    str_to_obj = val.split(' ')
    MEMORY[str_to_obj[0]] = str_to_obj[1]
    return 'Contact was change'


def show_all(val):
    return MEMORY


def show(val):
    str_to_obj = val.split(' ')
    return MEMORY[str_to_obj[0]]


def close(val):
    return 'Good bye!'


COMMANDS = {'hello': hello,
            'add': add,
            'change': change,
            'phone': show,
            'show_all': show_all,
            'close': close

            }

COMMANDS_KEYWORDS = {'hello': ['hello',  'hi'],
                     'add': ['add'],
                     'change': ['change'],
                     'phone': ['phone', 'phone number'],
                     'show_all': ['show all', 'show'],
                     'close': ['good bye', 'close', 'exit']
                     }

checker = True


def decorator_function(func):
    def wrapper():
        try:
            func()
        except KeyError:
            print('Invalid command')
        except IndexError:
            print('Not enough arguments')
        except UnboundLocalError:
            print('Invalid command')

    return wrapper


def handler(operator):
    return COMMANDS[operator]


@decorator_function
def main():
    global checker
    inp = input('Enter command: ')
    for command, kw in COMMANDS_KEYWORDS.items():
        for w in kw:
            if inp.startswith(w):
                result = handler(command)
                user_str = inp.replace(f'{w} ', '').strip()

    res = result(user_str)
    print(res)
    if res == 'Good bye!':
        checker = False


if __name__ == '__main__':
    while checker is True:
        main()
