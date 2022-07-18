"""
Lists are collection of data

"""

people_list = ["Erick", "Angel", "Bob"]
print(people_list)


my_list = [10, 12, 15, 25, 35]
#Agrega un valor al indice al final del todo
my_list.append(1000)
print(my_list)
#Agrega un valor en cierta posicion del indice (primer valor = posicion, segundo valor = valor añadido)
my_list.insert(2, 1000)
print(my_list)
#Elimina el valor especificado
my_list.remove(25)
print(my_list)
#Eliminar el valor del indice indicado
my_list.pop(0)
print(my_list)
#Ordena el arreglo
my_list.sort()
print(my_list)