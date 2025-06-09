class Organism:
    def eat(self):
        print("munch munch")
    def breathe(self):
        pass

class Carnivore(Organism):
    def eat(self):
        print("I eat meat")

class Herbivore(Organism):
    def eat(self):
        print("I eat veggies")
    

def party(invitee: Organism):
    invitee.eat()


carnivore = Carnivore()
herb = Herbivore()

party(carnivore)
