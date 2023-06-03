from time import sleep
import catacomb_functions
import inventory
from tqdm.asyncio import tqdm
from Catacomb_files import screens
import random

door_choices = {'a': 'first', 'b': 'second', 'c': 'third', 'd': 'fourth'}
action_choices = ['attack', 'befriend']
player_instance = inventory.Player()


if __name__ == '__main__':

    print("\"\"\n"
          "\n"
          "\n"
          "  (`\ .-') /`   ('-.                                  _   .-')       ('-.         .-') _                       _   .-')      ('-.                 .-') _                      ('-.     .-') _      ('-.                            _   .-')   .-. .-')\n"
          "   `.( OO ),' _(  OO)                                ( '.( OO )_   _(  OO)       (  OO) )                     ( '.( OO )_   ( OO ).-.            (  OO) )                    ( OO ).-.(  OO) )    ( OO ).-.                       ( '.( OO )_ \  ( OO )\n"
          ",--./  .--.  (,------.,--.       .-----.  .-'),-----. ,--.   ,--.)(,------.      /     '._  .-'),-----.        ,--.   ,--.) / . --. / ,--. ,--.  /     '._          .-----.  / . --. //     '._   / . --. /   .-----.  .-'),-----. ,--.   ,--.);-----.\\n"
          "|      |  |   |  .---'|  |.-')  '  .--./ ( OO'  .-.  '|   `.'   |  |  .---'      |'--...__)( OO'  .-.  '       |   `.'   |  | \-.  \  |  | |  |  |'--...__)        '  .--./  | \-.  \ |'--...__)  | \-.  \   '  .--./ ( OO'  .-.  '|   `.'   | | .-.  |\n"
          "|  |   |  |,  |  |    |  | OO ) |  |('-. /   |  | |  ||         |  |  |          '--.  .--'/   |  | |  |       |         |.-'-'  |  | |  | | .-')'--.  .--'        |  |('-..-'-'  |  |'--.  .--'.-'-'  |  |  |  |('-. /   |  | |  ||         | | '-' /_)\n"
          "|  |.'.|  |_)(|  '--. |  |`-' |/_) |OO  )\_) |  |\|  ||  |'.'|  | (|  '--.          |  |   \_) |  |\|  |       |  |'.'|  | \| |_.'  | |  |_|( OO )  |  |          /_) |OO  )\| |_.'  |   |  |    \| |_.'  | /_) |OO  )\_) |  |\|  ||  |'.'|  | | .-. `.\n"
          "|         |   |  .--'(|  '---.'||  |`-'|   \ |  | |  ||  |   |  |  |  .--'          |  |     \ |  | |  |       |  |   |  |  |  .-.  | |  | | `-' /  |  |          ||  |`-'|  |  .-.  |   |  |     |  .-.  | ||  |`-'|   \ |  | |  ||  |   |  | | |  \  |\n"
          "|   ,'.   |   |  `---.|      |(_'  '--'\    `'  '-'  '|  |   |  |  |  `---.         |  |      `'  '-'  '       |  |   |  |  |  | |  |('  '-'(_.-'   |  |         (_'  '--'\  |  | |  |   |  |     |  | |  |(_'  '--'\    `'  '-'  '|  |   |  | | '--'  /\n"
          "'--'   '--'   `------'`------'   `-----'      `-----' `--'   `--'  `------'         `--'        `-----'        `--'   `--'  `--' `--'  `-----'      `--'            `-----'  `--' `--'   `--'     `--' `--'   `-----'      `-----' `--'   `--' `------'\n"
          "\n"
          "\n"
          "\n"
          "\n"
          "\n"
          "              "
          "\n"
          )
    sleep(3.0)
    name = input('How can I call you? "\n"')
    print("You wake up in a dark room with 4 doors, labeled as; a, b, c, d." "\n")
    sleep(3.0)
    print("This is not a good place to be, try to get out." "\n")
    sleep(3.0)
    print("Good luck " + name + ", and don't fuck it up!" "\n")
    sleep(3.0)
    count = 0
    while player_instance.hp > 0:
        total = 0
        for num in tqdm([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
            sleep(0.25)
            total = total + num
        choice = input('Which door will you take?')
        while choice.lower() not in door_choices:
            print('Invalid choice. Please choose A, B, C, or D.')
            choice = input('Which door will you take?')
        catacomb_functions.which_door_opens()
        screen_str, random_obstacle = catacomb_functions.create_random_world1_screen()

        sleep(3.0)
        print('You can attack or befriend them.' "\n")
        inventory.Obstacle.obstacle_type_print(catacomb_functions.random_obstacle)
        sleep(3.0)

        catacomb_functions.get_action_choice()

        sleep(3.0)
        sleep(3.0)

        count += 1
        if count % 3 == 0:
            print(random.choice(screens.catacomb_facts))

        elif count % 5 == 0:
            # every 5 times the loop runs
            catacomb_functions.level_up_obstacles()
        elif count % 2 == 0:
            random_number = random.randint(1, 100)
            if random_number < 2:
                player_instance.lose_health()
            for i in range(2, int(random_number ** 0.5) + 1):
                if random_number % i == 0:
                    player_instance.gain_health()
        if player_instance.hp <= 0:
            break

    # execute another function after the loop is done
    catacomb_functions.game_over()
