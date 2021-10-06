class Dinosaur:
    def __init__(self, name, attack_power):
        self.dinosaur_name = name
        self.health = 1000
        self.attack_power = attack_power

    def attack_robot(self, robot):
        remaining_health = robot.health - self.attack_power
        robot.health = remaining_health
        return robot.health
