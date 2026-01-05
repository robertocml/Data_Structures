
# Se pueden implementar queues usando listas pero es muy ineficiente O(n) ya que se tienen que reacomodadr
# los punteros despues de una operacion de pop

print("------------ Queues con listas ------------")
q = []
q.append('a')
q.append('b')
q.append('c')

print("Queue inicial", q)

print("Elementos sacados de la queue:")
print(q.pop(0))
print(q.pop(0))
print("Queue despues de sacar los elementos", q)



# Es mucho mas eficiente usar deque (deck) ya que tienen una complejidad O(1)
print("\n")
print("------------ Queues con colletions deque ------------")
from collections import deque
q = deque()

q.append('a')
q.append('b')
q.append('c')
print("Queue inicial:", q)

print("Elementos sacados del queue:")
print(q.popleft())
print(q.popleft())

print("Queue despues de sacar los elementos", q)




# Los queues del modulo Queue son utiles cuando se trabaja con threads ya que lo hace de manera segura
print("\n")
print("------------ Queues con modulo Queue ------------")

from queue import Queue
q = Queue(maxsize=3)
print("Tamaño Inicial:", q.qsize())

q.put('a')
q.put('b')
q.put('c')
print("Esta el queue lleno ?:", q.full())

print("Elementos sacados del queue")
print(q.get())
print(q.get())
print(q.get())
print("Esta el queue vacio ?:", q.empty())

q.put(1)
print("Esta vacio ?:", q.empty())
print("Esta lleno ?:", q.full())