import random

secret = random.randint(1, 100)
guess = 0

while guess != secret:
    guess = int(input("Введите число от 1 до 100: "))
    if guess < secret:
        print("Больше")
    elif guess > secret:
        print("Меньше")
    else:
        print("Угадал!")
