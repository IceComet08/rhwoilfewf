import random

response = "y"

while response == "y":

    numero = random.randint(1,6)
    if numero == 1:
        print("|----|")
        print("|    |")
        print("|  0 |")
        print("|    |")
        print("|----|")
    elif numero == 2:
        print("|----|")
        print("| 0  |")
        print("|    |")
        print("|   0|")
        print("|----|")
    elif numero == 3:
        print("|----|")
        print("| 0  |")
        print("|  0 |")
        print("|   0|")
        print("|----|")
    elif numero == 4:
        print("|----|")
        print("|0  0|")
        print("|    |")
        print("|0  0|")
        print("|----|")
    elif numero == 5:
        print("|----|")
        print("|0  0|")
        print("|  0 |")
        print("|0  0|")
        print("|----|")
    else:
        print("|----|")
        print("|0  0|")
        print("|0  0|")
        print("|0  0|")
        print("|----|")
response = input("Se quiser jogar de novo, aperte Y :), mas caso queira parar, aperte n >:( : )").lower()
print("obrigado por jogar")