from dinosaur import Dinosaur


class Herd:
    def __init__(self):
        self.dinosaurs = []

    def create_herd(self):
        dinosaur_one = Dinosaur("Ken", 100)
        dinosaur_two = Dinosaur("Dennis", 150)
        dinosaur_three = Dinosaur("Oscar", 200)
        self.dinosaurs.append(dinosaur_one)
        self.dinosaurs.append(dinosaur_two)
        self.dinosaurs.append(dinosaur_three)

    def display_dinosaurs(self):
        for dinosaur in self.dinosaurs:
            print(dinosaur.dinosaur_name + ' ' + str(dinosaur.health) +
                  ' ' + str(dinosaur.attack_power))
