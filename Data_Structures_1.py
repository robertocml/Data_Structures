# ==========================================
# ESTRUCTURAS DE DATOS NATIVAS EN PYTHON
# Parte 1: list, tuple, set, dict
# ==========================================

print("\n=== LISTAS (list) ===")

# Una lista es ordenada y mutable
numbers = [10, 20, 30, 40]
print("Lista original:", numbers)

# Acceso O(1)
print("Elemento en índice 2:", numbers[2])

# Append (O(1) amortizado)
numbers.append(50)
print("Después de append:", numbers)

# Insertar al inicio (O(n))
numbers.insert(1, 15)
print("Después de insert al inicio:", numbers)

# Búsqueda (O(n))
print("¿30 está en la lista?", 30 in numbers)







print("\n=== TUPLAS (tuple) ===")

# Una tupla es ordenada e inmutable
point = (10, 20)
print("Tupla:", point)

# Acceso por índice
print("x:", point[0])
print("y:", point[1])

# Desempaquetado (muy común en Python)
x, y = point
print("Desempaquetado -> x:", x, ", y:", y)

# Intentar modificar (esto falla)
try:
    point[0] = 99
except TypeError as e:
    print("Error al modificar tupla:", e)










print("\n=== SETS (set) ===")

# Un set no permite duplicados
ids = {1, 2, 3, 3, 4}
print("Set (sin duplicados):", ids)

# Agregar elementos
ids.add(5)
print("Después de add:", ids)

# Búsqueda O(1) promedio
print("¿3 está en el set?", 3 in ids)

# Eliminar duplicados de una lista usando set
numbers_with_duplicates = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers_with_duplicates)
print("Lista original:", numbers_with_duplicates)
print("Sin duplicados:", unique_numbers)

# Operaciones de conjuntos
a = {1, 2, 3}
b = {3, 4, 5}

print("Intersección:", a & b)
print("Unión:", a | b)
print("Diferencia:", a - b)









print("\n=== DICCIONARIOS (dict) ===")

# Diccionario clave -> valor
user = {
    "name": "Roberto",
    "age": 28,
    "country": "México"
}

print("Usuario:", user)

# Acceso por clave (O(1))
print("Nombre:", user["name"])

# Agregar o modificar
user["age"] = 29
user["role"] = "Backend Developer"
print("Usuario actualizado:", user)

# Acceso seguro
print("Teléfono:", user.get("phone", "No existe"))

# Iterar diccionario
print("\nIterando diccionario:")
for key, value in user.items():
    print(f"{key} -> {value}")

# Keys deben ser hashables
location = (25.42, -100.99)
places = {
    location: "Saltillo"
}
print("\nDiccionario con tupla como key:", places)

# Esto NO funcionaría:
# places = {[1, 2]: "Error"}


print("\n=== COMPARACIÓN RÁPIDA ===")

data = [1, 2, 3, 4, 5]
data_set = set(data)
data_dict = {x: True for x in data}

print("Buscar 3 en list:", 3 in data)
print("Buscar 3 en set:", 3 in data_set)
print("Buscar 3 en dict:", 3 in data_dict)


print("\n=== CONCLUSIÓN ===")
print("Elegir bien la estructura de datos importa más que escribir más código.")