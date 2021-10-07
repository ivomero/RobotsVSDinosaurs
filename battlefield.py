from fleet import Fleet
from herd import Herd
from robot import Robot


class Battlefield:
    def __init__(self):
        self.fleet = []
        self.herd = []

    def run_game(self):

        run.display_welcome()
        fleet = Fleet()
        fleet.create_fleet()

        herd = Herd()
        herd.create_herd()
        run.show_dino_opponent_options()

    def display_welcome(self):
        print("Welcome to Robots vs Dinosaurs")

    def battle(self):

        pass

    def dino_turn(self, dinosaur):
        fleet.display_robots()
        target_robot = input("What robot would you like to attack?")
        for target in fleet.robots:
            if target_robot == "Merrideth":
                target_robot == target.robot_name
                target.health -= dinosaur.attack_power
                print(target.health)
                break
            elif target_robot == "Delilah":
                target_robot == target.robot_name
                target.health -= dinosaur.attack_power
                print(target.health)
                break
            elif target_robot == "BethBeth":
                target_robot == target.robot_name
                target.health -= dinosaur.attack_power
                print(target.health)

    def robo_turn(self, robot):
        pass

    def show_dino_opponent_options(self):
        fleet.display_robots()
        herd.display_dinosaurs()
        chosen_dinosaur = input("choose dinosaur")
        for name in herd.dinosaurs:
            if chosen_dinosaur == "Ken" and name.dinosaur_name == "Ken":
                chosen_dinosaur == name.dinosaur_name
                print(name.dinosaur_name)
                print("Robots")
                run.dino_turn(name)
                break
            elif chosen_dinosaur == "Dennis" and name.dinosaur_name == "Dennis":
                chosen_dinosaur == name.dinosaur_name
                print(name.dinosaur_name)
                print("Robots")
                run.dino_turn(name)
                break
            elif chosen_dinosaur == "Oscar" and name.dinosaur_name == "Oscar":
                chosen_dinosaur == name.dinosaur_name
                print(name.dinosaur_name)
                print("Robots")
                run.dino_turn(name)
                break

    def show_robo_opponent_options(self):
        pass

    def display_winner(self):
        pass


run = Battlefield()
fleet = Fleet()
fleet.create_fleet()
herd = Herd()
herd.create_herd()
'''
DISPLAY HERD/FLEET
fleet = Fleet()
fleet.create_fleet()
fleet.display_robots()
herd = Herd()
herd.create_herd()
herd.display_dinosaurs()
'''
