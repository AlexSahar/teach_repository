from random import randint
from art import logo
from os import system
system("cls")
print(logo)

def difficult(choise_diff):
    if choise_diff == 'hard':
        return 5
    else:
        return 10 

def decide_num(num):
    if number_rand > num:
        return "больше"
    elif number_rand < num:
        return "меньше"

while True:
    number_rand = randint(1,100)
    choise_diff = input("Выберите сложность: hard или easy => ")
    tried = difficult(choise_diff)
    print(f"У вас {tried} попыток")

    is_over = False
    while not is_over:
        num = int(input("Введите число: "))
        if number_rand == num:
            print("Выйграл")
            break
        print(decide_num(num))
        tried -=1
        print(f"Попыток осталось {tried}")
        if tried == 0:
            print(f"Ты проиграл ответ был {number_rand}")
            is_over = True

    asked = input("Еще раз? да / нет =>")
    if asked == 'нет' or 'n':
        print("Всего доброго")
        break