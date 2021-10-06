from weapon import Weapon


class Robot:
    def __init__(self, name):
        self.robot_name = name
        self.health = 1000
        self.weapon = Weapon()

    def attack_dinosaur(self, dinosaur):
        pass
