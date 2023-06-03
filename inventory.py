from typing import List, Any

import self

import catacomb_functions
import random


class Player:
    game_level = 1
    hp = 100

    def __init__(self):
        self.name = ''
        self.hp = 100
        self.points = 0
        self.lives = 3
        self.inventory = []
        self.location = ''
        self.solved_places = {1: False, 2: False, 3: False, 4: False, 5: False, 6: False, 7: False, 8: False, 9: False,
                              10: False, 11: False, 12: False}
        self.game_level = 1

    def lose_health(self):
        """Reduces the player's health by the given amount."""
        self.hp -= 3
        if self.hp <= 0:
            print(f"{self.name} has died!\n")
        else:
            print(f"A mysterious voice murmurs through the walls; We have {self.hp} health remaining.\n")

    def gain_health(self):
        """Increases the player's health by the given amount."""
        self.hp += 3
        print(f"A mysterious voice murmurs through the walls; We have gained {3} health. "
              f"We have now {self.hp} health.\n")

    def obstacle_attack(self):
        damage = random.randint(0, 5)
        self.hp -= damage
        print(f"The enemy strikes for {damage} damage! Your HP is now {self.hp}." "\n")
        if damage >= self.hp:
            print("The light of the Valar is fading in you!" "\n")
            print(catacomb_functions.game_over())
        else:
            catacomb_functions.another_chance()


class Obstacle:
    level = 1

    def __init__(self, name, type, level, health, damage):
        self.name = name
        self.type = type
        self.level = 1
        self.health = health
        self.max_health = Obstacle.level * 3
        self.is_active = True
        self.damage = damage

    def obstacle_type_print(random_obstacle):
        obstacle_type = random_obstacle.type
        if obstacle_type == "Existentialist":
            print('It is saying something! One is not born, but rather becomes, a woman.')
        elif obstacle_type == "Nihilist":
            print('It is saying something! God is dead.')
        elif obstacle_type == "Absurdist":
            print('It is saying something! I rebel; therefore, I exist.')
        elif obstacle_type == "Skeptic":
            print('It is saying something! Doubt is not a pleasant condition, but certainty is absurd.')
        elif obstacle_type == "Solipsist":
            print("It is saying something! I am the master of my fate; I am the captain of my soul.")
        elif obstacle_type == "Postmodernist":
            print("It is saying something! There are no facts, only interpretations.")
        elif obstacle_type == "Deconstructionist":
            print("It is saying something! There is nothing outside the text.")
        elif obstacle_type == "Pragmatist":
            print("It is saying something! The meaning of a proposition is the method of its verification")
        elif obstacle_type == "Moral Relativist":
            print("It is saying something! There is no objective moral truth!")
        elif obstacle_type == "Determinist":
            print(
                "It is saying something! We are all just machines made of flesh and blood, following the laws of nature.")
        elif obstacle_type == "Free Thinker":
            print("It is saying something! Dare to think for yourself.")
        elif obstacle_type == "Idealist":
            print("It is saying something! Reality is merely an illusion, albeit a very persistent one.")
        elif obstacle_type == "Materialist":
            print("It is saying something and accompanied by a ghost! Matter is the only reality, "
                  "and everything can be reduced to material elements.")
        elif obstacle_type == "Hedonist":
            print("It is saying something! Eat, drink, and be merry, for tomorrow we die.")
        elif obstacle_type == "Stoic":
            print("It is saying something! The obstacle is the way.")
        elif obstacle_type == "Cynic":
            print(
                "It is saying something! I threw my cup away when I saw a child drinking from his hands at the trough.")
        elif obstacle_type == "Epicurean":
            print("It is saying something! ")
        elif obstacle_type == "Sophist":
            print("It is saying something! Man is the measure of all things.")
        elif obstacle_type == "Utilitarian":
            print("It is saying something! The art of living well and the art of dying well are one.")
        elif obstacle_type == "Transcendentalist":
            print("It is saying something! Do not go where the path may lead, go instead "
                  "where there is no path and leave a trail.")
