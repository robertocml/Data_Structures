#Implementacion del hash table.
# Esta implementacion usa una funcion hash muy sencilla con el fin de entender el concepto.
# Simplemente usamos el valor ascii de la primera letra del key y a eso le sacamos el modulo 

# Para resolver los problemas de colisiones usamos la tecnica de separate chaning (linked lists en cada bucket de nuestra tabla)

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