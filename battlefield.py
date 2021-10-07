from fleet import Fleet
from herd import Herd


class Battlefield:
    def __init__(self):
        self.fleet = []
        self.herd = []
        self.dino_dead = []
        self.robo_dead = []

    def run_game(self):

        self.display_welcome()
        self.fleet = Fleet()
        self.fleet.create_fleet()

        self.herd = Herd()
        self.herd.create_herd()
        self.show_dino_opponent_options()

    def display_welcome(self):
        print("Welcome to Robots vs Dinosaurs")

    def end_or_continue_1(self, dinosaur):
        if dinosaur.health <= 0:
            self.dino_dead.append(dinosaur)
            self.herd.dinosaurs.remove(dinosaur)
        else:
            self.show_dino_opponent_options()

        if len(self.dino_dead) == 3:
            print("ROBOTS WIN!")
        else:
            self.show_dino_opponent_options()

    def end_or_continue_2(self, robot):

        if robot.health <= 0:
            self.robo_dead.append(robot)
            self.fleet.robots.remove(robot)
        else:
            self.show_robo_opponent_options()
        if len(self.robo_dead) == 3:
            print("DINOSAURS WIN!")
        else:
            self.show_robo_opponent_options()

    def dino_turn(self, dinosaur):
        self.fleet.display_robots()
        target_robot = input("What robot would you like to attack?")
        for target in self.fleet.robots:
            if target_robot == target.robot_name:
                target.health -= dinosaur.attack_power
                self.end_or_continue_2(target)
                break

    def robo_turn(self, robot):
        self.herd.display_dinosaurs()
        target_dinosaur = input("What dinosaur would you like to attack?")
        for target in self.herd.dinosaurs:
            if target_dinosaur == target.dinosaur_name:
                target.health -= robot.weapon.attack_power
                self.end_or_continue_1(target)
                break

    def show_dino_opponent_options(self):
        print("Robots:")
        self.fleet.display_robots()
        print("Dinosaurs:")
        self.herd.display_dinosaurs()
        chosen_dinosaur = input("choose dinosaur")
        for name in self.herd.dinosaurs:
            if chosen_dinosaur == name.dinosaur_name:
                print("Robots:")
                self.dino_turn(name)
                break

    def show_robo_opponent_options(self):
        print("Robots:")
        self.fleet.display_robots()
        print("Dinosaurs:")
        self.herd.display_dinosaurs()
        chosen_robot = input("choose robot")
        for name in self.fleet.robots:
            if chosen_robot == name.robot_name:
                print("Dinosaurs:")
                self.robo_turn(name)
                break
            # else:
            #     print("not a valid robot, try again")
            #     self.show_robo_opponent_options()
            #     break

    def display_winner(self):
        pass


# run = Battlefield()
# fleet = Fleet()
# fleet.create_fleet()
# herd = Herd()
# herd.create_herd()

# DISPLAY HERD/FLEET
# fleet = Fleet()
# fleet.create_fleet()
# fleet.display_robots()
# herd = Herd()
# herd.create_herd()
# herd.display_dinosaurs()
# '''

# robot = run.dino_turn()

# robo_dead = []
# if robot.health <= 0:
#     robo_dead.append(robot)
# else:
#     run.show_robo_opponent_options()

# if len(robo_dead) == 3:
#     print("DINOSAURS WIN!")

# else:
#     run.show_robo_opponent_options()
