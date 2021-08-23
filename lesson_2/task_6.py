#!/usr/bin/python3.8
import random

# 6. В программе генерируется случайное целое число от 0 до 100. 
# Пользователь должен его отгадать не более чем за 10 попыток. 
# После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, 
# чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.


def random_number():
    return random.randint(1, 100)


def game_number(number: int, result: int) -> str:
    if number == result:
        print('Win!!!')
    else:
        print('Больше' if number < result else 'Меньше')
        

if __name__ == '__main__':
    step = 0
    result = random_number()
    
    while True:
        number = int(input('Введите число: '))
        game_number(number, result)
        step += 1
        if step == 10:
            print(f'Проиграли {result}')
            break
