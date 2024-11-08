import pygame
import sys
import os

pygame.init()

# Definir constantes
ANCHO_VENTANA = 1200
ALTO_VENTANA = 600
COLOR_TEXTO_NORMAL = (150, 77, 3)  # Color del texto predeterminado
COLOR_TEXTO_HOVER = (255, 255, 255)  # Color del texto cuando está en hover

# Cargar la fuente personalizada
try:
    FUENTE_TEXTO = pygame.font.Font("assets/fonts/press.ttf", 50)
    FUENTE_OPCIONES = pygame.font.Font("assets/fonts/press.ttf", 20)
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

# Crear ventana
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Pesca-Dos (Jugar)")

# Cargar imagen de fondo
try:
    fondo_menu = pygame.image.load("assets/menu/mar.jpeg")
except pygame.error as e:
    print(f"No se pudo cargar la imagen de fondo: {e}")
    fondo_menu = None

# Cargar imágenes para las opciones
try:
    imagen_normal = pygame.image.load("assets/menu/f(2).png")
    imagen_hover = pygame.image.load("assets/menu/f-hover(2).png")  # Imagen cuando está seleccionada
except pygame.error as e:
    print(f"No se pudieron cargar las imágenes para las opciones: {e}")
    imagen_normal = imagen_hover = None

# Opciones del menú
opciones = ["Principiante", "Intermedio", "Avanzado", "Regresar"]
seleccion = 0  # Opción seleccionada inicialmente
anterior_seleccion = seleccion  # Para detectar cambios de selección

# Estado de pantalla completa
pantalla_completa = False

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
    titulo_texto = FUENTE_TEXTO.render("Dificultad", True, (255, 0, 0))  # Cambiar el color del texto del título
    ventana.blit(titulo_texto, (ancho // 2 - titulo_texto.get_width() // 2, 80))

    # Calcular el factor de escala
    factor_escala_x = ancho / ANCHO_VENTANA
    factor_escala_y = alto / ALTO_VENTANA

    # Tamaño escalado de las imágenes detrás del texto
    imagen_ancho = int(270 * factor_escala_x)
    imagen_alto = int(60 * factor_escala_y)

    # Dibujar opciones
    for i, opcion in enumerate(opciones):
        # Coordenadas de las opciones
        x_opcion = ancho // 2 - imagen_ancho // 2
        y_opcion = int(200 * factor_escala_y) + i * int(80 * factor_escala_y)  # Ajustar la separación vertical

        # Cambiar la imagen según si la opción está seleccionada o no (hover)
        if i == seleccion:
            imagen_a_dibujar = pygame.transform.scale(imagen_hover, (imagen_ancho, imagen_alto))  # Escalar imagen hover
            ventana.blit(imagen_a_dibujar, (x_opcion, y_opcion))  # Dibujar la imagen de hover
            texto_opcion = FUENTE_OPCIONES.render(opcion, True, COLOR_TEXTO_HOVER)  # Cambiar el color del texto a blanco en hover
        else:
            imagen_a_dibujar = pygame.transform.scale(imagen_normal, (imagen_ancho, imagen_alto))  # Escalar imagen normal
            ventana.blit(imagen_a_dibujar, (x_opcion, y_opcion))  # Dibujar la imagen predeterminada
            texto_opcion = FUENTE_OPCIONES.render(opcion, True, COLOR_TEXTO_NORMAL)  # Color del texto predeterminado

        # Dibujar la opción en la pantalla centrada
        ventana.blit(texto_opcion, (ancho // 2 - texto_opcion.get_width() // 2, y_opcion + 15))  # Ajustar texto sobre la imagen

    pygame.display.flip()  # Actualizar pantalla

# Bucle principal
while True:
    mouse_pos = pygame.mouse.get_pos()  # Obtener la posición del mouse
    seleccion_anterior = seleccion  # Guardar la selección anterior

    # Detectar hover con el mouse
    for i in range(len(opciones)):
        x_opcion = ANCHO_VENTANA // 2 - (270 * (ANCHO_VENTANA / ANCHO_VENTANA)) // 2
        y_opcion = int(200 * (ALTO_VENTANA / ALTO_VENTANA)) + i * int(80 * (ALTO_VENTANA / ALTO_VENTANA))

        # Verificar si el mouse está sobre la opción
        if x_opcion <= mouse_pos[0] <= x_opcion + 270 and y_opcion <= mouse_pos[1] <= y_opcion + 60:
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
                if seleccion == 0:  # Principiante
                    print("Seleccionando modo Principiante...")
                    pygame.quit()
                    os.system('python assets/menu/principiante.py')  # Ejecutar el script de principiante.py
                elif seleccion == 1:  # Intermedio
                    print("Seleccionando modo Intermedio...")
                    pygame.quit()
                    os.system('python assets/menu/intermedio.py')  # Ejecutar el script de principiante.py
                    
                    # Lógica para el modo Intermedio

                elif seleccion == 2:  # Avanzado
                    print("Seleccionando modo Avanzado...")
                    pygame.quit()
                    os.system('python assets/menu/avanzado.py')  # Ejecutar el script de principiante.py
                    
                    # Lógica para el modo Avanzado

                elif seleccion == 3:  # Regresar
                    print("Regresando al menú principal...")
                    pygame.quit()
                    os.system('python menu.py')  # Ejecutar el script del menú principal

            elif event.key == pygame.K_ESCAPE:  # Tecla Escape
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_F11:  # Tecla F11 para pantalla completa
                pantalla_completa = not pantalla_completa
                if pantalla_completa:
                    ventana = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # Cambiar a pantalla completa
                else:
                    ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))  # Volver a modo ventana

        if event.type == pygame.MOUSEBUTTONDOWN:  # Detectar clic del mouse
            if event.button == 1:  # Botón izquierdo
                pygame.mixer.Sound.play(sonido_seleccion)  # Reproducir sonido de selección
                if seleccion == 0:  # Principiante
                    print("Seleccionando modo Principiante...")
                    pygame.quit()
                    os.system('python assets/menu/principiante.py')
                elif seleccion == 1:  # Intermedio
                    pygame.quit()
                    print("Seleccionando modo Intermedio...")
                    os.system('python assets/menu/intermedio.py')
                    # Lógica para el modo Intermedio
                elif seleccion == 2:  # Avanzado
                    pygame.quit()
                    os.system('python assets/menu/avanzado.py')
                    print("Seleccionando modo Avanzado...")
                    # Lógica para el modo Avanzado
                elif seleccion == 3:  # Regresar
                    print("Regresando al menú principal...")
                    os.system('python menu.py')
                    pygame.quit()
                    sys.exit()

    # Mover el fondo de derecha a izquierda
    fondo_x -= velocidad_fondo
    if fondo_x <= -ANCHO_VENTANA:  # Reiniciar la posición del fondo
        fondo_x = 0

    dibujar_menu()  # Dibujar menú
