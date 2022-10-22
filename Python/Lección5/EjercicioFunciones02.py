# Ejercicio 2: Funcion con * args para multiplicar
# Crear una funcion para multiplicar los valores recibidos
# de tipo numérico, utilizando argumentos variables *args
# como prametro de la funcion y regresar como resultado
# la multiplicacion de todos los valores pasados como argumentos

# Definimos la funcion para multiplicar
def multiplicar_valores(*numeros): # El mas utilizado es *args
    resultado = 1 # porque con cero no se puede multiplicar nada
    for numero in numeros:
        resultado *= numero
    return resultado

# Llamamos la funcion
print(multiplicar_valores(3, 5, 15, 3)) # Le pasamos los argumentos