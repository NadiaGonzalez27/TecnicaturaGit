# Comenzamos con Funciones
# mi_funcion() # No se puede llamar antes de definir a una función
# Definimos una función
def mi_funcion(): # Para identificar a la funcion utilizamos parantesis
    print('Saludos a todos los alumnos de la Tecnicatura')

mi_funcion() # estamos llamando a la función
mi_funcion() # Se puede llamar a una función N cantidad de veces

# Desempaquetado de listas o list Unpacking
def show(name, lastName):
    print(name+' '+lastName)
person = ['Ariel', 'Betancud']
show(person[0], person[1]) # Pasamos uno por uno los datos de la lista a la funcion
show(*person) # Esto es lo mismo que lo anterior pero le pasamos todo junto
person2 = ('Osvaldo', 'Giordanini') # desempaquetamos a traves de una tupla
show(*person2)
person3 = {"lastName": "Lucero", "name": "Natalia"}
show(**person3)

# Repaso sobre for , else
numbers = [1, 2, 3, 4, 5] # Aun con el la lista vacia se va a ejecutar el else
for n in numbers:
    print(n)
    if n == 3:
        break # Esta es la unica manera para que no se ejecute el else
else:
    print('Esto se termino')

# List comprehension, lista de comprensiob
names = ['Paolo', 'Rodrigo', 'Pepe']
alongP = [p for p in names if p[0] == 'P'] #nEsto trgtrsa una nueva lista
print(alongP)

bottleC = [{"name": "Quilmes", "country": "Arg"},
           {"name": "Corona", "country": "Mx"},
           {"name": "Stella Artois", "country": "Belgium"},
           ]
Arg = [b for b in bottleC if b["country"] == "Arg"]
print(Arg)
print(bottleC)

# Paso de Argumentos (funciones)
def mi_fumcion2(name, lastName):
    print("Saludos a todos los que ven a traves del canal de YouTube")
    print(f'Nombre: {name}, Apellido: {lastName}')
mi_fumcion2('Jorge', 'Lucero')
mi_fumcion2('Ariel', 'Betancud')
mi_fumcion2('Analia', 'Pedrosa')

# La palabra return en funciones
# Creamos una funcion para sumar
def sumar(a, b):
    return a + b
# resultado = sumar(78, 22)
# print(f'El resultado de la suma es: {resultado}')
print(f'El resultado de la suma es: {sumar(55, 45)}')

# Valores por default
def sumar2(a = 0, b = 0): # Le damos un valor por default
    return a + b
resultado = sumar2()
print(f'Resultado de la suma: {resultado}')
print(f'Resultado de la suma: {sumar2(22, 66)}')

# Argumentos, variables en Funciones
def listaNombres(*nombres): # Normalmente se utiliza: *args
    for nombre in nombres: # Se va a convertir en una tupla
        print(nombre)
listaNombres('Lucas', 'José', 'Claudia', 'Rosa', 'Maria')
listaNombres('Marcos', 'Daniel', 'Romina', 'Pepe', 'Marcela', 'Carlos')