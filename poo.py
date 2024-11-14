class Cat:
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


my_cat = Cat(name="Grominet")

print(my_cat)
print(my_cat.name, my_cat.legs)

my_cat.speak()

cat2 = Cat()
cat2.name = "Garfield"
cat2.legs -=1
print(cat2.name, cat2.legs)

cat2.speak()

