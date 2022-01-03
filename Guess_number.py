# Игра: камень(R), ножницы(S), бумага(P)

import random

should_continue = True

while should_continue:
    player_choice = input('Player choise: [R/S/P]').lower() #приводим к нижнему регистру что бы не ввел игрок

    if player_choice not in ['r', 's', 'p']:  #валидация на ввод
        print('Incorrect input. Try again')
        continue

    gen =  {1:'r', 2:'s', 3:'p'}: #сопоставили символы с цифрами
    comp_choice = gen[random.randint(1,3)]  #по другому можно: comp_choice =  random.choice(['r', 's', 'p'])

    print (f'Comp choice = {comp_choice}')

    winning_combinations = [('p', 'r'), ('r', 's'), ('s', 'p')]

    if  player_choice == comp_choice:
        print('Nichia')

    elif (player_choice, comp_choice) in winning_combinations:
        print('Player wins! :)')
    else:
        print('Comp wins =(')

    should_continue = input('Want to proceed? [y/n]').lower == 'y'



