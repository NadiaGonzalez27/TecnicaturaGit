# Dada la siguiente Tupla
tupla = (13, 1, 8, 3, 2, 5, 8)
# Crear una lista que solo incluya los numeros menores a 5
# e imprima por consola [1, 2, 3]

lista = []
for listaTupla in tupla:
    if listaTupla < 5:
        lista.append(listaTupla)
print(lista)