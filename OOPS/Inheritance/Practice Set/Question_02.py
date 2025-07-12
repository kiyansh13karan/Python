# Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from ‘Pets’. Add a method ‘bark’ to class ‘Dog’.



# Base class
class Animals:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# Derived class from Animals
class Pets(Animals):
    def __init__(self, name, owner):
        super().__init__(name)
        self.owner = owner

    def show_owner(self):
        print(f"{self.name} is owned by {self.owner}.")

# Further derived class from Pets
class Dog(Pets):
    def __init__(self, name, owner, breed):
        super().__init__(name, owner)
        self.breed = breed

    def bark(self):
        print(f"{self.name} says: Woof! Woof!")

# Example usage
dog1 = Dog("Buddy", "Alice", "Labrador")
dog1.speak()
dog1.show_owner()
dog1.bark()
