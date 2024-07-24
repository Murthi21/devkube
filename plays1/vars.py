class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
my_person = Person("Dwight", 35)

my_vars = vars(my_person)

print(my_vars)
# {'name': 'Dwight', 'age': 35}