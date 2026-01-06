phonebook = {
     "bob": 7387,
     "alice": 3719,
     "jack": 7052,
 }

squares = {x: x * x for x in range(6)}

print(phonebook["alice"])
print(squares)


# Los diccionarios estan implementados como hash tables.
# Busquedas, Inserciones y actualizaciones son O(1) promedio