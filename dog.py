from animal import Animal

class Dog(Animal):

    def __init__(self, name,):
        # constructeur
        # self = eq. "this"
        self.name = name
        self.speak()

    def speak(self):
        # methods
        # qui connait l'instance (self)
        print(self.name, ": Woof !")
if __name__ == "__main__" :
    # ne s'execute uniquement si "dog.py" est le fichier principal
    my_dog = Dog("Idefix")
    my_dog.speak()