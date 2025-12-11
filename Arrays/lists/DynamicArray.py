import ctypes
# Implementacion de un array dinamico en python

class DynamicArray():

    #Inicializacion y sobrecarga de metodos
    def __init__(self):
        self.n = 0 # El contador de elementos
        self.capacity = 1 # Inicializamos la capacidad en 1
        self.A = self.make_array(self.capacity) # Generamos el espacio en memoria con ctpyes

    def __len__(self): # overload para usar el metodo len()
        return self.n
    
    def __getitem__(self, k): # overload para usar el metodo getitem()
        if not 0 <= k <= self.n:
            return IndexError("Element is out of index")
        
        return self.A[k]
    
    #Funcionalidades de mi array dinamico
    
    
    def append(self, element):
        
        if self.n == self.capacity:
            self._resize(self.capacity * 2) # Lo mas comun es ir duplicando la capacidad del array

        self.A[self.n] = element

        self.n += self.n

    #Desplazamos a partir del index todos los valores a la derecha, insertamos el nuevo valor en el index y aumentamos en 1 la cantidadde elementos 
    # si es necesario, hacemos resize
    def insertAt(self, index, element):

        if index > self.n - 1 or index < 0:
            return IndexError("Index out of range")
        
        if self.n == self.capacity:
            self._resize(self.capacity * 2) # Lo mas comun es ir duplicando la capacidad del array
        
        # Desplazamos desde el final de array hasta el index para hacer espacio para el nuevo elemento
        for i in range(self.n-1, index-1, -1):
            self.A[i+1] = self.A[i] 
        
        self.A[index] = element # Insertamos el elemento en la posicion deseada
        self.n += 1  # Actualizamos la capacidads

    

    def make_array(self, capacity):
        return (capacity * ctypes.py_object)() # Aqui generamos el array, al momento de instanciarlo con (), asignamos la memoria
    


    #Funciones privadas de la clase
    
    # Este metodo es importante porque es el que hace la reasignacion en memoria (contigua) de un nuevo array (y pasa los valores existentes
    # del array viejo al nuevo con mayor capacidad)
    def _resize(self, new_capacity): 

        B = self.make_array(new_capacity)

        #Asignamos los valores del array al nuevo espacio contiguo
        for i in range(self.n):
            B[i] = self.A[i]

        self.A = B  # Apuntamos el array al nuevo espacio de memoria (el arrray viejo queda como garbage collection que despues se reusa)
        self.capacity = new_capacity # Actualizamos la capacidad

