#Implementacion del hash table.
# Esta implementacion usa una funcion hash muy sencilla con el fin de entender el concepto.
# Simplemente usamos el valor ascii de la primera letra del key y a eso le sacamos el modulo 

# Para resolver los problemas de colisiones usamos la tecnica de separate chainning (linked lists en cada bucket de nuestra tabla)

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return ord(key[0]) % self.size

    def set(self, key, value):
        hash_index = self._hash(key)
        for kvp in self.table[hash_index]:
            if kvp[0] == key:
                kvp[1] = value
                return

        self.table[hash_index].append([key, value])

    def get(self, key):
        hash_index = self._hash(key)
        for kvp in self.table[hash_index]:
            if kvp[0] == key:
                return kvp[1]

        raise KeyError(f'Key {key} not found')

    def remove(self, key):
        hash_index = self._hash(key)
        for i, kvp in enumerate(self.table[hash_index]):
            if kvp[0] == key:
                self.table[hash_index].pop(i)
                return

        raise KeyError(f'Key {key} not found')
    




#### Ejemplo:
tabla = HashTable(size=10)

tabla.set("Roberto", 28)  # 'R' → ASCII 82 → 82 % 10 = 2
tabla.set("Hugo", 35)     # 'H' → ASCII 72 → 72 % 10 = 2  ← colisión con "Roberto"
tabla.set("Ana", 22)      # 'A' → ASCII 65 → 65 % 10 = 5
tabla.set("Carlos", 40)   # 'C' → ASCII 67 → 67 % 10 = 7
tabla.set("Luis", 31)    # 'L' → ASCII 76 → 76 % 10 = 6

print(tabla.get("Roberto")) 
print(tabla.get("Hugo"))


## Asi queda la tabla:
# Índice 0 → []
# Índice 1 → []
# Índice 2 → [["Roberto", 28], ["Hugo", 35]  ← única colisión (mismo index de resultado de nuestra funcion _hash para ambos)
# Índice 3 → []
# Índice 4 → []
# Índice 5 → [["Ana", 22]]
# Índice 6 → [["Luis", 31]]
# Índice 7 → [["Carlos", 40]]
# Índice 8 → []
# Índice 9 → []

 