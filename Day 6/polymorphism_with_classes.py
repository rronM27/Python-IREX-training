class Dog:
    def __init__(self, name):
        self.name = name
    def sound(self):
         print(f"{self.name} WOOF!")

class Cat:
    def __init__(self, name):
        self.name = name
    def sound(self):
         print(f"{self.name} MEOWW!")

class Bird:
    def __init__(self, name):
        self.name = name
    def sound(self):
         print(f"{self.name} Chirp!")

dog=Dog("Buddy")  #this is an object
cat=Cat("Bob")
bird=Bird("Tuity")

for animal in (dog,cat,bird):
    animal.sound()
