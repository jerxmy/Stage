from cat import Cat
from dog import Dog


# PARTIE CHAT
my_cat = Cat(name="Grominet", age=79)
print(my_cat.get_age())

print(my_cat)
print(my_cat.name, my_cat.legs)

my_cat.speak()

cat2 = Cat(name="Garfield")
cat2.legs -=1
print(cat2.name, cat2.legs)

# PARTIE CHIEN

my_dog = Dog(name="Idefix")
print(my_dog)

print(my_dog)
print(my_dog.name)

my_dog.speak()

dog2 = Dog(name="Pluto")
print(dog2.name)