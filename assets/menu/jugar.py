import pygame
import sys
import os
<<<<<<< HEAD
import subprocess
=======
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1

pygame.init()

# Definir constantes
ANCHO_VENTANA = 1200
ALTO_VENTANA = 600
COLOR_TEXTO_NORMAL = (255, 255, 255)  # Blanco, igual que el color de texto normal en el primer código
COLOR_TEXTO_HOVER = (255, 223, 129)  # Dorado Claro o Amarillo, igual que en el primer código

# Cargar la fuente personalizada
try:
    FUENTE_TEXTO = pygame.font.Font("assets/fonts/press.ttf", 40)  # Ajusté el tamaño de la fuente
    FUENTE_OPCIONES = pygame.font.Font("assets/fonts/press.ttf", 22)  # Ajusté el tamaño de la fuente para las opciones
except pygame.error as e:
    print(f"No se pudo cargar la fuente: {e}")
    sys.exit()

# Cargar sonidos
try:
    sonido_hover = pygame.mixer.Sound("assets/musica/boton.mp3")
    sonido_seleccion = pygame.mixer.Sound("assets/musica/golpe_2.mp3")
except pygame.error as e:
    print(f"No se pudieron cargar los sonidos: {e}")
    sys.exit()

<<<<<<< HEAD
def ejecutar_script(script):
    subprocess.Popen([sys.executable, script])  # Ejecuta el script en un nuevo proceso
=======
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1
# Crear ventana
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Pesca-Dos (Jugar)")

# Cargar imagen de fondo
try:
    fondo_menu = pygame.image.load("assets/menu/mar.png")
    fondo_menu = pygame.transform.scale(fondo_menu, (ANCHO_VENTANA, ALTO_VENTANA))
except pygame.error as e:
    print(f"No se pudo cargar la imagen de fondo: {e}")
    fondo_menu = None

# Cargar imágenes para las opciones (de acuerdo con el primer código)
imagenes_boton = {}
for i in range(4):  # Las 4 opciones
    imagen_normal = pygame.image.load("assets/menu/f(2).png")
    imagen_hover = pygame.image.load("assets/menu/f-hover(2).png")

    # Redimensionar las imágenes detrás de los botones
    imagen_normal = pygame.transform.scale(imagen_normal, (350, 100))  # Escalar a 280x100 píxeles
    imagen_hover = pygame.transform.scale(imagen_hover, (350, 98))    # Escalar a 280x98 píxeles

    imagenes_boton[i] = {"normal": imagen_normal, "hover": imagen_hover}

# Opciones del menú
opciones = ["Principiante", "Intermedio", "Avanzado", "Regresar"]
seleccion = 0  # Opción seleccionada inicialmente

# Variable para el desplazamiento de la imagen de fondo
fondo_x = 0
velocidad_fondo = .2  # Velocidad de movimiento del fondo

def dibujar_menu():
    global fondo_x  # Hacer que fondo_x sea accesible

    # Obtener el tamaño actual de la ventana
    ancho, alto = ventana.get_size()

    # Dibujar imagen de fondo desplazada
    if fondo_menu:
        ventana.blit(fondo_menu, (fondo_x, 0))  # Dibujar la imagen de fondo
        ventana.blit(fondo_menu, (fondo_x + ancho, 0))  # Dibujar la imagen de fondo adicional para crear un efecto de bucle

    # Dibujar título
    titulo_texto = FUENTE_TEXTO.render("Dificultad", True, (252, 186, 3))  # Color del texto similar al primer código
    ventana.blit(titulo_texto, (ancho // 2 - titulo_texto.get_width() // 2, 80))

    # Dibujar opciones
    for i, opcion in enumerate(opciones):
        # Coordenadas de las opciones
        x_opcion = ancho // 2 - 175  # Ajusté para que esté centrado con las imágenes
        y_opcion = 200 + i * 90  # Ajusté la separación vertical

        # Cambiar la imagen según si la opción está seleccionada o no (hover)
        if i == seleccion:
            imagen_a_dibujar = imagenes_boton[i]["hover"]
            texto_opcion = FUENTE_OPCIONES.render(opcion, True, COLOR_TEXTO_HOVER)
        else:
            imagen_a_dibujar = imagenes_boton[i]["normal"]
            texto_opcion = FUENTE_OPCIONES.render(opcion, True, COLOR_TEXTO_NORMAL)

        # Mostrar la imagen del botón detrás del texto
        ventana.blit(imagen_a_dibujar, (x_opcion, y_opcion - 20))  # Dibujar la imagen detrás del texto

        # Dibujar el texto sobre la imagen
        ventana.blit(texto_opcion, (ancho // 2 - texto_opcion.get_width() // 2, y_opcion + 15))

    pygame.display.flip()  # Actualizar pantalla

# Bucle principal
while True:
    mouse_pos = pygame.mouse.get_pos()  # Obtener la posición del mouse
    seleccion_anterior = seleccion  # Guardar la selección anterior

    # Detectar hover con el mouse
    for i in range(len(opciones)):
        x_opcion = ANCHO_VENTANA // 2 - 140
        y_opcion = 200 + i * 90

        # Verificar si el mouse está sobre la opción
        if x_opcion <= mouse_pos[0] <= x_opcion + 280 and y_opcion <= mouse_pos[1] <= y_opcion + 100:
            seleccion = i
            break  # Salir del bucle al encontrar la opción

    # Reproducir sonido de hover solo si la selección ha cambiado
    if seleccion != seleccion_anterior:
        pygame.mixer.Sound.play(sonido_hover)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:  # Tecla arriba
                seleccion = (seleccion - 1) % len(opciones)
                pygame.mixer.Sound.play(sonido_hover)
            elif event.key == pygame.K_DOWN:  # Tecla abajo
                seleccion = (seleccion + 1) % len(opciones)
                pygame.mixer.Sound.play(sonido_hover)

            elif event.key == pygame.K_RETURN:  # Tecla Enter
                pygame.mixer.Sound.play(sonido_seleccion)  # Reproducir sonido de selección

                # Espera para que el sonido se reproduzca
                pygame.time.delay(500)  # Espera 500 ms (medio segundo)

                # Luego cerrar la ventana y ejecutar el script seleccionado
                pygame.quit()  # Cerrar la ventana
                if seleccion == 0:  # Principiante
                    print("Seleccionando modo Principiante...")
<<<<<<< HEAD
                    ejecutar_script('assets/menu/principiante.py')  # Ejecutar el script de principiante.py
                elif seleccion == 1:  # Intermedio
                    print("Seleccionando modo Intermedio...")
                    ejecutar_script('assets/menu/intermedio.py')  # Ejecutar el script de intermedio.py
                elif seleccion == 2:  # Avanzado
                    print("Seleccionando modo Avanzado...")
                    ejecutar_script('assets/menu/avanzado.py')  # Ejecutar el script de avanzado.py
                elif seleccion == 3:  # Regresar
                    print("Regresando al menú principalll...")
                    pygame.quit()
                    ejecutar_script('asstes/menu/opciones.py')
=======
                    os.system('python assets/menu/principiante.py')  # Ejecutar el script de principiante.py
                elif seleccion == 1:  # Intermedio
                    print("Seleccionando modo Intermedio...")
                    os.system('python assets/menu/intermedio.py')  # Ejecutar el script de intermedio.py
                elif seleccion == 2:  # Avanzado
                    print("Seleccionando modo Avanzado...")
                    os.system('python assets/menu/avanzado.py')  # Ejecutar el script de avanzado.py
                elif seleccion == 3:  # Regresar
                    print("Regresando al menú principal...")
                    pygame.quit()
                    sys.exit()
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1

            elif event.key == pygame.K_ESCAPE:  # Tecla Escape
                pygame.quit()
                sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:  # Detectar clic del mouse
            if event.button == 1:  # Botón izquierdo
                pygame.mixer.Sound.play(sonido_seleccion)  # Reproducir sonido de selección

                # Espera para que el sonido se reproduzca
                pygame.time.delay(500)  # Espera 500 ms (medio segundo)

                # Luego cerrar la ventana y ejecutar el script seleccionado
                pygame.quit()  # Cerrar la ventana
                if seleccion == 0:  # Principiante
                    print("Seleccionando modo Principiante...")
<<<<<<< HEAD
                    ejecutar_script('assets/menu/principiante.py')
                elif seleccion == 1:  # Intermedio
                    print("Seleccionando modo Intermedio...")
                    ejecutar_script('assets/menu/intermedio.py')
                elif seleccion == 2:  # Avanzado
                    print("Seleccionando modo Avanzado...")
                    ejecutar_script('assets/menu/avanzado.py')
                elif seleccion == 3:  # Regresar
                    print("Regresando al menú principal...")
                    
                    pygame.quit()
                    ejecutar_script("menu.py")
=======
                    os.system('python assets/menu/principiante.py')
                elif seleccion == 1:  # Intermedio
                    print("Seleccionando modo Intermedio...")
                    os.system('python assets/menu/intermedio.py')
                elif seleccion == 2:  # Avanzado
                    print("Seleccionando modo Avanzado...")
                    os.system('python assets/menu/avanzado.py')
                elif seleccion == 3:  # Regresar
                    print("Regresando al menú principal...")
                    pygame.quit()
                    sys.exit()
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1

    # Mover el fondo de derecha a izquierda
    fondo_x -= velocidad_fondo
    if fondo_x <= -ANCHO_VENTANA:  # Reiniciar la posición del fondo
        fondo_x = 0

    dibujar_menu()  # Dibujar menú
