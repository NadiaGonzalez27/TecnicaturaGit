# Etapas de vida
edad = int(input("Digite su edad: "))
mensaje = None
if 0 <= edad < 10:
    mensaje = 'La infancia es increible y bella'
elif 10 <= edad < 19:
    mensaje = 'Tienes muchos cambios, tienes que estudiar'
elif 19 <= edad < 29:
    mensaje = 'Amor y confianza en el trabajo'
elif 29 <= edad < 39:
    mensaje = 'La vida es dura, pero adelante'
elif 39 <= edad < 49:
    mensaje = 'Disfruta de cada momento'
elif 49 <= edad < 59:
    mensaje = 'El camino sigue, a no decaer'
elif 59 <= edad < 69:
    mensaje = 'Los nietos, alegria al corazon'
elif 69 <= edad < 79:
    mensaje = 'A cuidarse mucho'
elif 79 <= edad < 89:
    mensaje = 'La vida es un regalo'
elif 89 <= edad < 99:
    mensaje = 'Agradecer cada dia por la vida'
else:
    mensaje = 'Error, etapa no reconocida'
print(f'Tu edad es {edad}, {mensaje}')