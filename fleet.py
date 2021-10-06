from robot import Robot


class Fleet:
    def __init__(self):
        self.robots = []

    def create_fleet(self):
        robot_one = Robot("Merrideth")
        robot_two = Robot("Delilah")
        robot_three = Robot("BethBeth")
        self.robots.append(robot_one)
        self.robots.append(robot_two)
        self.robots.append(robot_three)

    def display_robots(self):
        for robot in self.robots:
            print(robot.robot_name + ' ' + str(robot.health) +
                  ' ' + str(robot.weapon.attack_power))
