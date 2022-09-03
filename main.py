import random

print("Выбери бандита, которого надо посадить(номер):\n1. Carlos\n2. Mikel\n3. Triesta")

NumberOfBandit = random.randint(1, 3)
userGuess = -1

while userGuess != NumberOfBandit:
    userGuess = int(input())
    if userGuess < NumberOfBandit:
        print("Вы посадили не правильного бандита! Вы проиграли.\nВсе бандит вышел на свободу и продолжил творить хаос!\nВерный ответ:")
        print(NumberOfBandit)
    elif userGuess > NumberOfBandit:
        print("Вы посадили не правильного бандита! Вы проиграли.\nВсе бандит вышел на свободу и продолжил творить хаос!\nВерный ответ:")
        print(NumberOfBandit)
    else:
        print("Вы посадили верного бандита! Вы выиграли!")
    break