class Dog:

    def __init__(self, name,):
        # constructeur
        # self = eq. "this"
        self.name = name
        self.speak()

    def speak(self):
        # methods
        # qui connait l'instance (self)
        print(self.name, ": Woof !")