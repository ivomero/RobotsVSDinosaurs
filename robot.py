from weapon import Weapon


class Robot:
    def __init__(self, name):
        self.robot_name = name
        self.health = 100
        self.weapon = Weapon("Slingshot", 150)

    def attack_dinosaur(self, dinosaur):
        remaining_health = dinosaur.health - self.weapon.attack_power
        return remaining_health
