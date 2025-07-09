# multiple inheritance in python :-

# Multiple Inheritance is a feature where a child class can inherit from more than one parent class.



# First parent class
class Father:
    def skills(self):
        print("Father: Gardening, Cooking")

# Second parent class
class Mother:
    def hobbies(self):
        print("Mother: Painting, Dancing")

# Child class inheriting from both Father and Mother
class Child(Father, Mother):
    def own_interest(self):
        print("Child: Playing football")

# Creating object of child class
c = Child()
c.skills()         # Inherited from Father
c.hobbies()        # Inherited from Mother
c.own_interest()   # Defined in Child

'''
Output : -

Father: Gardening, Cooking
Mother: Painting, Dancing
Child: Playing football
'''