import pygame
import sys
<<<<<<< HEAD
import os
import cv2
=======
import os  # Cambiar de subprocess a os
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1
import constantes

pygame.init()

COLOR_TEXTO = (0, 0, 0)

<<<<<<< HEAD
# Inicializar variables
mostrar_video_inicio = True  # Variable para controlar si se muestra el video

# Cargar tipografías y sonidos
=======
# Cargar las tipografías
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1
try:
    FUENTE_TEXTO = pygame.font.Font("assets/fonts/press.ttf", 34)
    FUENTE_OPCIONES = pygame.font.Font("assets/fonts/press.ttf", 22)
except pygame.error as e:
    print(f"No se pudo cargar la fuente: {e}")
    sys.exit()

<<<<<<< HEAD
try:
    sonido_hover = pygame.mixer.Sound("assets/musica/boton.mp3")
    sonido_seleccion = pygame.mixer.Sound("assets/musica/golpe_2.mp3")
    sonido_video = pygame.mixer.Sound("assets/menu/logo.mp3")  # Sonido del logo
=======
# Cargar sonidos 
try:
    sonido_hover = pygame.mixer.Sound("assets/musica/boton.mp3")
    sonido_seleccion = pygame.mixer.Sound("assets/musica/golpe_2.mp3")
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1
except pygame.error as e:
    print(f"No se pudieron cargar los sonidos: {e}")
    sys.exit()

# Crear ventana
ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))
pygame.display.set_caption("Pesca-Dos (Menú)")

# Cargar imagen de fondo
try:
<<<<<<< HEAD
    fondo_menu = pygame.image.load("assets/menu/menu.png")
=======
    fondo_menu = pygame.image.load("assets/menu/menu.jpeg")
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1
    fondo_menu = pygame.transform.scale(fondo_menu, (constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))
except pygame.error as e:
    print(f"No se pudo cargar la imagen de fondo: {e}")
    fondo_menu = None

# Cargar imágenes para "Jugar"
try:
<<<<<<< HEAD
    imagen_jugar = pygame.image.load("assets/menu/f(inicio).png")
    imagen_hover = pygame.image.load("assets/menu/f-hover(inicio).png")
=======
    imagen_jugar = pygame.image.load("assets/menu/f(2).png")
    imagen_hover = pygame.image.load("assets/menu/f-hover(2).png")
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1
except pygame.error as e:
    print(f"No se pudieron cargar las imágenes para Jugar: {e}")
    imagen_jugar = imagen_hover = None

# Opciones del menú
opciones = ["Jugar", "Opciones", "Salir"]
seleccion = 0  # Opción seleccionada inicialmente
anterior_seleccion = seleccion  # Para detectar cambios de selección

# Función para ejecutar los scripts usando os.system()
def ejecutar_script(script):
<<<<<<< HEAD
    os.system(f'python {script}')  # Ejecutamos el script en un nuevo proceso
    sys.exit()  # Terminamos el proceso actual de Pygame

# Función para cargar y reproducir el video de inicio
def reproducir_video_pygame(ruta_video):
    cap = cv2.VideoCapture(ruta_video)
    if not cap.isOpened():
        print(f"No se pudo cargar el video: {ruta_video}")
        return
    
    clock = pygame.time.Clock()  # Usar pygame.Clock() para controlar la velocidad del video

    # Reproducir el sonido del logo
    sonido_video.play()

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            # Convertir el frame de BGR (OpenCV) a RGB (pygame)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # Convertir a superficie de Pygame
            frame_surface = pygame.surfarray.make_surface(frame_rgb.swapaxes(0, 1))
            
            # Mostrar el video en la ventana de Pygame
            ventana.blit(frame_surface, (0, 0))  # Dibuja el video en la parte superior izquierda
            pygame.display.flip()

            # Controlar la velocidad de los fotogramas del video (FPS)
            clock.tick(30)  # Limitar a 30 fotogramas por segundo, ajusta según lo necesario

            # Salir si se presiona una tecla o si se cierra la ventana
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                    cap.release()
                    pygame.quit()
                    sys.exit()
        else:
            break  # Si no hay más frames, se detiene el video
    
    cap.release()  # Liberar el recurso del video al finalizar

=======
    pygame.quit()  # Cerramos la ventana actual de Pygame
    os.system(f'python {script}')  # Ejecutamos el script en un nuevo proceso
    sys.exit()  # Terminamos el proceso actual de Pygame

>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1
# Función para dibujar el menú
def dibujar_menu():
    # Escalar la imagen de fondo
    if fondo_menu:
        fondo_menu_escalado = pygame.transform.scale(fondo_menu, ventana.get_size())
        ventana.blit(fondo_menu_escalado, (0, 0))

<<<<<<< HEAD
    # Calcular posición y tamaño de las opciones
    for i, opcion in enumerate(opciones):
        factor_escala = ventana.get_height() / constantes.ALTO_VENTANA  # Escalar según la altura
        x_opcion = ventana.get_width() // 8 - (200 * factor_escala) // 2 - 80  # Ajuste de 80 píxeles hacia la izquierda
        y_opcion = 250 * factor_escala + i * (100 * factor_escala)  # Aumento de la separación entre botones

        # Escalar las imágenes de los botones
        if seleccion == i and imagen_hover:
            ventana.blit(pygame.transform.scale(imagen_hover, (400 * factor_escala, 150 * factor_escala)), (x_opcion, y_opcion - 35))
        else:
            ventana.blit(pygame.transform.scale(imagen_jugar, (400 * factor_escala, 150 * factor_escala)), (x_opcion, y_opcion - 35))

        # Calcular el tamaño del texto
        texto_opcion = FUENTE_OPCIONES.render(opcion, True, (255, 255, 255) if i == seleccion else (252, 186, 3))

        # Calcular la posición del texto para centrarlo en el botón
        x_texto = x_opcion + (400 * factor_escala) // 2 - texto_opcion.get_width() // 2 
        y_texto = y_opcion + (150 * factor_escala) // 2 - texto_opcion.get_height() // 2 - 40  # Centrado verticalmente en el botón

        # Dibujar el texto sobre el botón
        ventana.blit(texto_opcion, (x_texto, y_texto))
=======
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
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1

    pygame.display.flip()

# Estado de pantalla completa
pantalla_completa = False

<<<<<<< HEAD
# Reproducir el video de inicio al cargar el juego
#reproducir_video_pygame("assets/menu/logo.mp4")

# Reproducir la música de fondo
pygame.mixer.music.load("assets/musica/loopmenu.mp3")
pygame.mixer.music.play(-1)  # Reproducir música en bucle

=======
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1
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
<<<<<<< HEAD
=======
                    pygame.quit()
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1
                    sys.exit()
            elif event.key == pygame.K_ESCAPE:  # Tecla Escape
                pygame.quit()
                sys.exit()
<<<<<<< HEAD
=======
            elif event.key == pygame.K_F11:  # Tecla F11
                pantalla_completa = not pantalla_completa
                if pantalla_completa:
                    ventana = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # Cambiar a pantalla completa
                else:
                    ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))  # Volver a modo ventana

>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1
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
<<<<<<< HEAD
                        ejecutar_script('assets/menu/jugar.py')
                    elif seleccion == 1:
                        ejecutar_script('assets/menu/opciones.py')
                    elif seleccion == 2:
                        pygame.quit()

    # Detección de hover (fuera del bucle de eventos, pero dentro del bucle principal)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for i in range(len(opciones)):
        x_opcion = ventana.get_width() // 2 - 500  # Ajustar según el tamaño escalado
        y_opcion = 50 + i * 60
=======
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
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1
        if x_opcion < mouse_x < x_opcion + 200 and y_opcion < mouse_y < y_opcion + 60:
            if seleccion != i:
                seleccion = i
                pygame.mixer.Sound.play(sonido_hover)
<<<<<<< HEAD

    # Dibujar el menú
    dibujar_menu()
=======
            break

    dibujar_menu()  # Dibujar menú
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1
