import pygame
import sys
import os  # Cambiar de subprocess a os
import constantes

pygame.init()

COLOR_TEXTO = (0, 0, 0)

# Cargar las tipografías
try:
    FUENTE_TEXTO = pygame.font.Font("assets/fonts/press.ttf", 34)
    FUENTE_OPCIONES = pygame.font.Font("assets/fonts/press.ttf", 22)
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
ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))
pygame.display.set_caption("Pesca-Dos (Menú)")

# Cargar imagen de fondo
try:
    fondo_menu = pygame.image.load("assets/menu/menu.jpeg")
    fondo_menu = pygame.transform.scale(fondo_menu, (constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))
except pygame.error as e:
    print(f"No se pudo cargar la imagen de fondo: {e}")
    fondo_menu = None

# Cargar imágenes para "Jugar"
try:
    imagen_jugar = pygame.image.load("assets/menu/f(2).png")
    imagen_hover = pygame.image.load("assets/menu/f-hover(2).png")
except pygame.error as e:
    print(f"No se pudieron cargar las imágenes para Jugar: {e}")
    imagen_jugar = imagen_hover = None

# Opciones del menú
opciones = ["Jugar", "Opciones", "Salir"]
seleccion = 0  # Opción seleccionada inicialmente
anterior_seleccion = seleccion  # Para detectar cambios de selección

# Función para ejecutar los scripts usando os.system()
def ejecutar_script(script):
    pygame.quit()  # Cerramos la ventana actual de Pygame
    os.system(f'python {script}')  # Ejecutamos el script en un nuevo proceso
    sys.exit()  # Terminamos el proceso actual de Pygame

# Función para dibujar el menú
def dibujar_menu():
    # Escalar la imagen de fondo
    if fondo_menu:
        fondo_menu_escalado = pygame.transform.scale(fondo_menu, ventana.get_size())
        ventana.blit(fondo_menu_escalado, (0, 0))

    #titulo_texto = FUENTE_TEXTO.render("Pesca-Dos (¡Beta!)", True, (210, 219, 42))
    #ventana.blit(titulo_texto, (ventana.get_width() // 2 - titulo_texto.get_width() // 2, 100))
    
    # Calcular posición y tamaño de opciones
    for i, opcion in enumerate(opciones):
        factor_escala = ventana.get_height() / constantes.ALTO_VENTANA  # Escalar según la altura
        x_opcion = ventana.get_width() // 2 - (200 * factor_escala) // 2
        y_opcion = 250 * factor_escala + i * (60 * factor_escala)

        # Escalar las imágenes de los botones
        if seleccion == i and imagen_hover:
            ventana.blit(pygame.transform.scale(imagen_hover, (200 * factor_escala, 60 * factor_escala)), (x_opcion, y_opcion - 15))
        else:
            ventana.blit(pygame.transform.scale(imagen_jugar, (200 * factor_escala, 60 * factor_escala)), (x_opcion, y_opcion - 15))

        # Renderizar las opciones
        texto_opcion = FUENTE_OPCIONES.render(opcion, True, (255, 255, 255) if i == seleccion else (150, 77, 3))
        ventana.blit(texto_opcion, (ventana.get_width() // 2 - texto_opcion.get_width() // 2, y_opcion))

    pygame.display.flip()

# Estado de pantalla completa
pantalla_completa = False

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                seleccion = (seleccion - 1) % len(opciones)
                pygame.mixer.Sound.play(sonido_hover)
            elif event.key == pygame.K_DOWN:
                seleccion = (seleccion + 1) % len(opciones)
                pygame.mixer.Sound.play(sonido_hover)
            elif event.key == pygame.K_RETURN:
                pygame.mixer.Sound.play(sonido_seleccion)
                if seleccion == 0:  # Jugar
                    ejecutar_script('assets/menu/jugar.py')
                elif seleccion == 1:  # Opciones
                    ejecutar_script('assets/menu/opciones.py')
                elif seleccion == 2:  # Salir
                    pygame.quit()
                    sys.exit()
            elif event.key == pygame.K_ESCAPE:  # Tecla Escape
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_F11:  # Tecla F11
                pantalla_completa = not pantalla_completa
                if pantalla_completa:
                    ventana = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # Cambiar a pantalla completa
                else:
                    ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))  # Volver a modo ventana

        # Soporte para mouse
        if event.type == pygame.MOUSEBUTTONDOWN:  # Detección de clic
            mouse_x, mouse_y = event.pos
            for i in range(len(opciones)):
                x_opcion = ventana.get_width() // 2 - 100  # Ajustar según el tamaño escalado
                y_opcion = 250 + i * 60
                if x_opcion < mouse_x < x_opcion + 200 and y_opcion < mouse_y < y_opcion + 60:
                    seleccion = i
                    pygame.mixer.Sound.play(sonido_seleccion)
                    if seleccion == 0:
                        pygame.quit()
                        ejecutar_script('assets/menu/jugar.py')
                    elif seleccion == 1:
                        pygame.quit()   
                        ejecutar_script('assets/menu/opciones.py')
                    elif seleccion == 2:
                        pygame.quit()
                        sys.exit()

    # Detección de hover
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for i in range(len(opciones)):
        x_opcion = ventana.get_width() // 2 - 100  # Ajustar según el tamaño escalado
        y_opcion = 250 + i * 60
        if x_opcion < mouse_x < x_opcion + 200 and y_opcion < mouse_y < y_opcion + 60:
            if seleccion != i:
                seleccion = i
                pygame.mixer.Sound.play(sonido_hover)
            break

    dibujar_menu()  # Dibujar menú
