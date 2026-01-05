# ==========================================
# STACKS EN PYTHON (LIFO)
# ==========================================

print("\n=== ¿QUÉ ES UN STACK? ===")
print("Stack = Last In, First Out (LIFO)")
print("El último elemento en entrar es el primero en salir.")


print("\n=== IMPLEMENTACIÓN BÁSICA CON LIST ===")

stack = []

# Push (agregar al stack)
stack.append("A")
stack.append("B")
stack.append("C")
print("Stack después de push:", stack)

# Peek (ver el tope sin quitarlo)
top = stack[-1]
print("Elemento en el tope:", top)

# Pop (sacar del stack)
removed = stack.pop()
print("Elemento removido:", removed)
print("Stack después de pop:", stack)


print("\n=== STACK VACÍO (CASO IMPORTANTE) ===")

stack.clear()
print("Stack vacío:", stack)

if not stack:
    print("No se puede hacer pop: stack vacío")


print("\n=== CASO REAL 1: DESHACER (UNDO) ===")

undo_stack = []

undo_stack.append("escribir 'Hola'")
undo_stack.append("borrar 'o'")
undo_stack.append("escribir '!'")
print("Acciones:", undo_stack)

last_action = undo_stack.pop()
print("Undo ->", last_action)
print("Acciones restantes:", undo_stack)


print("\n=== CASO REAL 2: HISTORIAL DE NAVEGACIÓN ===")

history = []

history.append("google.com")
history.append("youtube.com")
history.append("github.com")
print("Historial:", history)

current = history.pop()
print("Volver a:", current)
print("Historial actual:", history)


print("\n=== CONCLUSIÓN ===")
print("Un stack no es una estructura nueva en Python.")
print("Es un patrón que se implementa con list.")
print("Úsalo cuando necesites reversión o retroceso.")