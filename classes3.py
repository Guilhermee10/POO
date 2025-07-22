class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def description(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"
    

class JackRussellTerrier(Dog):
    def speak(self, sound='arf'):
        return f'{self.name} says {sound}'

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass


miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)

print(miles.speak())

print(type(miles))



# kirk = ["James Kirk", 34, "Captain", 2265]
# spock = ["Spock", 35, "Science Officer", 2254]
# mccoy = ["Leonard McCoy", "Chief Medical Officer", 2266]

# dog() #falta fornecer valores para classe, exemplo a baixo


# miles.species = "Felis silvestris"
# print (miles.species)
# print(miles.description())
# print (miles.speak("Woof Woof"))





