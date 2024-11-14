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

my_cat = Cat(name="Grominet", age=79)
print(my_cat.get_age())

print(my_cat)
print(my_cat.name, my_cat.legs)

my_cat.speak()

cat2 = Cat(name="Garfield")
cat2.legs -=1
print(cat2.name, cat2.legs)

