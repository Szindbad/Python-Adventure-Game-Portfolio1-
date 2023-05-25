from typing import List, Any


class player:
    lives = 3
    game_level = 1
    hp = 100

    def __init__(self):
        self.name = '',
        self.hp = 100,
        self.points = 0,
        self.lives = 3,
        self.inventory = []
        self.location = ''
        self.solved_places = {1: False, 2: False, 3: False, 4: False, 5: False, 6: False, 7: False, 8: False, 9: False,
                              10: False, 11: False, 12: False}
        self.game_level = 1

        # this might not be right in here, but I def. need it somewhere,
    # id of screens and bulian, need to access it in higher levels as well, eleg lehet felsorolni hogy mik lettek
    # megoldva,
    # nem kell False/true


myPlayer = player()


class Obstacle:
    level = 1

    def __init__(self, name, type, level, health, damage):
        self.name = name
        self.type = type
        self.level = level
        self.health = health
        self.max_health = Obstacle.level * 3
        self.is_active = True
        self.damage = damage

    def __repr__(self):
       return 'This obstacle is called {name}, you are on level {level}, facing a {type} type creature!'.format(
           name=self.name, level=self.level, type=self.type, damage=self.damage)
