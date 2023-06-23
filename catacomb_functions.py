import screens
import inventory
import random
import main

screen_str, random_obstacle = inventory.Obstacle.create_random_world1_screen()

player_instance = inventory.Player()


# after an unsuccessful attack or befriend, this gives the player the choice to do an action again
def another_chance():
    another_chance_action_str = input(
        'It seems like this creature is tougher than it looks, but do not worry! You can choose to attack or befriend them again' "\n")
    flag = False
    while not flag:
        if another_chance_action_str.lower() not in main.action_choices:
            print('Invalid choice. Please choose "attack" or "befriend".\n')
            another_chance_action_str = input('Which will it be? ' "\n")
        else:
            if another_chance_action_str.lower() == main.action_choices[0]:
                print(attack_world1())
            elif another_chance_action_str.lower() == main.action_choices[1]:
                print(befriend_world1(random_obstacle=random_obstacle))
            flag = True


# action functions related to obstacles
def befriend_world1(**kwargs):
    random_obstacle = kwargs.get('random_obstacle', None)

    if random_obstacle is None:
        print("Emptiness stares back at you.\n")
        return

    random_number = random.randint(0, 5)
    if random_number == 0:
        print("You became friends with " + random_obstacle.name + ", how lovely!" "\n")
    elif random_number == 1:
        print("You became associates with " + random_obstacle.name + ", how interesting!" "\n")
    elif random_number == 2:
        print(
            "You know each other from now on! Awkwardly wave next time you see " + random_obstacle.name + " on the bus!" "\n")
    else:
        print("They don't like you!" "\n")
        player_instance.obstacle_attack()


def get_action_choice():
    action_choices = ['attack', 'befriend']
    while True:
        choice_action = input('Which will it be?\n')
        if choice_action.lower() not in action_choices:
            print('Invalid choice. Please choose "attack" or "befriend".\n')
        elif choice_action.lower() == action_choices[0]:
            attack_world1(random_obstacle=random_obstacle)
            return
        elif choice_action.lower() == action_choices[1]:
            another_chance()
            return


def attack_world1(**kwargs):
    random_obstacle = kwargs.get('random_obstacle')
    attack_power = random.randint(1, 5)

    if attack_power >= random_obstacle.health:
        print("You vanquished your enemy!\n")
        screens.defeated_obstacles.append(random_obstacle.name)
    else:
        print(random.choice(screens.attack_sentences))
        player_instance.obstacle_attack()


def which_door_opens():
    loop = 1
    flag = False

    while not flag:
        if random.random() < 0.60:
            door_closed_str = random.choice(screens.door_closed_strings)
            print(door_closed_str)
            choice = input('Which door will you take?')
            screens.door_choices.append(choice)
            while choice.lower() not in main.door_choices:
                print('Invalid choice. Please choose A, B, C, or D.')
                choice = input('Which door will you take?')
                screens.door_choices.append(choice)
            chosen_door = main.door_choices[choice.lower()]
            print(f'You chose {chosen_door}.')  # embed the value of the chosen_door inside the string
        else:
            door_open_str = random.choice(screens.door_open_strings)
            print(door_open_str)
            flag = True  # set the flag to True to exit the while loop

    while loop == 1:
        break


screen = {
    "id": screens.random_screens_id,
    "title": screens.titles,
    "description": screens.description,
    "obstacle": screens.obstacles,
    "doors": screens.doors
}


# after certain number of loops, this should happen
def level_up_obstacles():
    """Levels up the obstacles"""
    count_list_elements = lambda x: len(x)

    for main.random_obstacle in screens.defeated_obstacles:
        if count_list_elements(screens.defeated_obstacles) > player_instance.game_level:
            random_obstacle.level += 4
            print('You progress deeper into the unknown, get ready for some tougher enemies!\n')

    return main.random_obstacle.level


def game_over():
    """if player is dead, game end"""
    if inventory.Player.hp <= 0:
        print('''
        ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
        ███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
        ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
        ██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
        ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
        ███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
        ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
        ███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
        ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
        ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
        ██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
        ███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄ ''')
