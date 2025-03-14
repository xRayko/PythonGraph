from Animal import Animal


class Poule(Animal):
    "Représentation d'une poule"
    def say_hello(self):
        if self.age < 1:
            print("je suis un poussin")
        else:
         super().say_hello()
        print("CotCot " "Je suis une poule." "Poule")

Poule = Poule("CotCot", 0.5, "Poule")
Poule.say_hello()