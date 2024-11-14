from animal import Animal, Target

class Cat(Animal, Target):
    legs = 4

    def __init__(self, name, age=0):
        # constructeur
        # self = eq. "this"
        self.name = name
        self.speak()
        # encapsultation = attribut privé
        self.__age = age

    def speak(self):
        # methods
        # qui connait l'instance (self)
        print(self.name, ": Miaou !")
        # print(self.__age) impossible
    
    def get_age(self):
        # guetter / Accesseur
        if self.__age > 50:
            return "Nan..."
        return self.__age

    def set_age(self, age):
        # Setter / Mutateur
        if int(age) and age > 0:
            self.__age = age
        else :
            print("ERREUR")
if __name__ == "__main__":
    my = Cat("Gardfield")
    my.boom()
