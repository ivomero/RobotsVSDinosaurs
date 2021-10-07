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
            if target_robot == "Merrideth" and target.robot_name == "Merrideth":
                target_robot == target.robot_name
                target.health -= dinosaur.attack_power
                run.show_robo_opponent_options()
                break
            elif target_robot == "Delilah" and target.robot_name == "Delilah":
                target_robot == target.robot_name
                target.health -= dinosaur.attack_power
                run.show_robo_opponent_options()
                break
            elif target_robot == "BethBeth" and target.robot_name == "BethBeth":
                target_robot == target.robot_name
                target.health -= dinosaur.attack_power
                print(target.health)
                run.show_robo_opponent_options()
                break

    def robo_turn(self, robot):
        herd.display_dinosaurs()
        target_dinosaur = input("What dinosaur would you like to attack?")
        for target in herd.dinosaurs:
            if target_dinosaur == "Ken" and target.dinosaur_name == "Ken":
                target_dinosaur == target.dinosaur_name
                target.health -= robot.weapon.attack_power
                run.show_dino_opponent_options()
                break
            elif target_dinosaur == "Dennis" and target.dinosaur_name == "Dennis":
                target_dinosaur == target.dinosaur_name
                target.health -= robot.weapon.attack_power
                run.show_dino_opponent_options()
                break
            elif target_dinosaur == "Oscar" and target.dinosaur_name == "Oscar":
                target_dinosaur == target.robot_name
                target.health -= robot.weapon.attack_power
                print(target.health)
                run.show_dino_opponent_options()
                break

    def show_dino_opponent_options(self):
        fleet.display_robots()
        herd.display_dinosaurs()
        chosen_dinosaur = input("choose dinosaur")
        for name in herd.dinosaurs:
            if chosen_dinosaur == "Ken" and name.dinosaur_name == "Ken":

                print("Robots")
                run.dino_turn(name)
                break
            elif chosen_dinosaur == "Dennis" and name.dinosaur_name == "Dennis":

                print("Robots")
                run.dino_turn(name)
                break
            elif chosen_dinosaur == "Oscar" and name.dinosaur_name == "Oscar":

                print("Robots")
                run.dino_turn(name)
                break

    def show_robo_opponent_options(self):
        fleet.display_robots()
        herd.display_dinosaurs()
        chosen_robot = input("choose robot")
        for name in fleet.robots:
            if chosen_robot == "Merrideth" and name.robot_name == "Merrideth":

                print("Dinosaurs")
                run.robo_turn(name)
                break
            elif chosen_robot == "Delilah" and name.robot_name == "Delilah":

                print("Dinosaurs")
                run.robo_turn(name)
                break
            elif chosen_robot == "BethBeth" and name.robot_name == "BethBeth":

                print("Dinosaurs")
                run.robo_turn(name)
                break

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
