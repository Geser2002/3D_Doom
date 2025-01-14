import con_pygame
import doom_matplotlib

#print(f"Введите цифру для выбора:\n1 - Игра жизни Конвея\n2 - Неполный 3д дума\n")
#a = int(input())
a = 2

if a == 1:
    con_pygame.game()
elif a == 2:
    a = 2
    #print("matplotlib")
else:
    print("lox net takogo")