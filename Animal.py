import self
class Animal:

    def  __init__(self, name, age, espèce):
        self.name = name
        self.age = age
        self.espèce = espèce



    def say_hello(self):
        if self.age > 2:
            print(f"Bonjour, mon nom est {self.name}, j'ai {self.age} et je suis une {self.espèce}.")
        else:
            print(
                f"Bonjour, mon nom est {self.name}, je suis encore un bébé {self.espèce}.")

Snow = Animal("Snow",3,"Chat")
Scooby = Animal("Scooby",8,"Chien")
Annie = Animal("Annie",1,"Girafe")

Snow.say_hello()
Scooby.say_hello()
Annie.say_hello()