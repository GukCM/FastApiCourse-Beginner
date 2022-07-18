# Lists Assignment
# - Create a list of 5 animals called zoo
# - Delete the animal at the 3rd index.
# - Append a new animal at the end of the list
# - Delete the animal at the beginning of the list.
# - Print all the animals
# - Print only the first 3 animals

zoo = ["Pig", "Cow", "Unicorn", "Lion", "Moose"]
print(zoo)
print("-"*50)
zoo.pop(2)
print(zoo)
print("-"*50)
zoo.append("Leopard")
print(zoo)
print("-"*50)
zoo.pop(0)
print(zoo)
print("-"*50)
print(zoo)
print("-"*50)
print(zoo[0:3])
print("-"*50)