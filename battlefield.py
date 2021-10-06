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
        fleet.display_robots()
        herd = Herd()
        herd.create_herd()
        herd.display_dinosaurs()

    def display_welcome(self):
        print("Welcome to Robots vs Dinosaurs")

    def battle(self):
       # yesno = input("Start game? Y/N")
        # if yesno == "Y":
        #    dino_turn()
        # else:
        #    robotsvsdinosaurs.run_game()
        pass

    def dino_turn(self, dinosaur):
        pass

    def robo_turn(self, robot):
        pass

    def show_dino_opponent_options(self):
        pass

    def show_robo_opponent_options(self):
        pass

    def display_winner(self):
        pass


run = Battlefield()
