# Sistema de calificaciones
calificaciones = int(input("Ingrese un valor del (0 - 10): "))
if calificaciones == 9 or calificaciones == 10:
    print('A')
elif 8 <= calificaciones < 9:
    print('B')
elif 7 <= calificaciones < 8:
    print('C')
elif 6 <= calificaciones < 7:
    print('D')
elif 0 <= calificaciones < 6:
    print('F')
else:
    print('Valor incorrecto...')