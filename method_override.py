class Adult:
    def __init__(self, name, age, eye_colour, hair_colour):
        self.name = name
        self.age = age
        self.eye_colour = eye_colour
        self.hair_colour = hair_colour

    def can_drive(self):
        print(f"{self.name} is old enough to drive!")

class Child(Adult):
    def can_drive(self):
        print(f"{self.name} is too young to drive!")

# get user input
name = input("Please enter your name:\t")
age = int(input("Please enter your age:\t"))
eye_colour = input("Please enter your eye colour:\t")
hair_colour = input("Please enter your hair colour:\t")

# if user is 18 or over, create an Adult, otherwise a Child
if age >= 18:
    person = Adult(name, age, eye_colour, hair_colour)
    person.can_drive()
else:
    person = Child(name, age, eye_colour, hair_colour)
    person.can_drive()
