# Ejercicio 2: Operaciones de conjuntos con listas
# Escriba un programa que tenga 2 listas y que a continuacion
# cree las siguientes listas (en las que no debe haber repeticion)
# 1 Lista de palabras que aparezcan en las listas
# 2 Lista de palabras que aparezcan en la primera lista, pero no en la segunda
# 3 lista de palabras que aparezcan en la segunda lista, pero no en la primera
# 4 Lista de palabras que aparezcan en ambas listas

lista1 = [1, 2, 3, 4, 3, 5, 3, 4, 2, 1, 5]
lista2 = [4, 4, 5, 6, 1, 2, 3, 8, 7, 9, 9]

#
conjunto1 = set(lista1)
conjunto2 = set(lista2)

union = list(conjunto1 | conjunto2) # Unimos los dos conjuntos
solo1 = list(conjunto1 - conjunto2) # Solo muestra el conjunto1
solo2 = list(conjunto2 - conjunto1) # Solo muestra el conjunto2
interseccion = list(conjunto1 & conjunto2) # Mostramos aambas listas

print(f'Lista de palabras que aparezcan en las listas: {union}')
print(f'Lista de palabras que aparezcan en la primera lista, pero no en la segunda: {solo1}')
print(f'Lista de palabras que aparezcan en la segunda lista, pero no en la primera: {solo2}')
print(f'Lista de palabras que aparezcan en ambas listas: {interseccion}')