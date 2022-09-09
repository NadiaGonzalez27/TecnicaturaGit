import math # Importamos la clase math para hacer uso de la funcion sqrt(Raiz cuadrada)
# Dada la siguiente Tupla
tupla = (13, 1, 8, 3, 2, 5, 8)
# Crear una lista que solo incluya los numeros menores a 5
# e imprima por consola [1, 2, 3]

lista = [] # Definimos la lista
# Filtramos los elementos menores a 5 de la tupla
for listaTupla in tupla:
    if listaTupla < 5:
        lista.append(listaTupla)
print(lista)

# Ejercicio de matematicas
# Para sacar la raiz cuadrada de un numero positivo
numero = int(input('Digite un numero positivo:'))
while numero < 0:
    print('Error -> Deberia ser un numero positivo')
    numero = int(input('Digite un numero positivo:'))
print(f'\nSu raiz cuadrada es: {math.sqrt(numero):.2f}')



