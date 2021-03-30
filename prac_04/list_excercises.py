# numbers = []
# while len(numbers) != 5:
#     number = input('Number: ')
#     numbers.append(number)
# print(numbers)
# print('The first number is {}'.format(numbers[0]))
# print('The last number is {}'.format(numbers[-1]))
# print('The smallest number is {}'.format(min(numbers)))
# print('The largest number is {}'.format(max(numbers)))
# print('The average of the number is {}'.format(sum(numbers)))

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
enter_username = input('username: ')
for username in usernames:
    if enter_username == username:
        print('Access Granted')
        break
    else:
        print('Access Denied')
