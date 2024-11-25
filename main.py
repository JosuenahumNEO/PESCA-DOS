import pygame
import sys
import os
<<<<<<< HEAD
import subprocess
import constantes
import cv2
=======
import cv2
import constantes
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1

pygame.init()

COLOR_TEXTO = (0, 0, 0)

# Inicializar variables
mostrar_video_inicio = True  # Variable para controlar si se muestra el video

# Cargar tipografías y sonidos
try:
    FUENTE_TEXTO = pygame.font.Font("assets/fonts/press.ttf", 34)
    FUENTE_OPCIONES = pygame.font.Font("assets/fonts/press.ttf", 22)
except pygame.error as e:
    print(f"No se pudo cargar la fuente: {e}")
    sys.exit()

try:
    sonido_hover = pygame.mixer.Sound("assets/musica/boton.mp3")
    sonido_seleccion = pygame.mixer.Sound("assets/musica/golpe_2.mp3")
    sonido_video = pygame.mixer.Sound("assets/menu/logo.mp3")  # Sonido del logo
except pygame.error as e:
    print(f"No se pudieron cargar los sonidos: {e}")
    sys.exit()

# Crear ventana
ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))
pygame.display.set_caption("Pesca-Dos (Menú)")

# Cargar imagen de fondo
try:
    fondo_menu = pygame.image.load("assets/menu/menu.png")
    fondo_menu = pygame.transform.scale(fondo_menu, (constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))
except pygame.error as e:
    print(f"No se pudo cargar la imagen de fondo: {e}")
    fondo_menu = None

# Cargar imágenes para "Jugar"
try:
    imagen_jugar = pygame.image.load("assets/menu/f(inicio).png")
    imagen_hover = pygame.image.load("assets/menu/f-hover(inicio).png")
except pygame.error as e:
    print(f"No se pudieron cargar las imágenes para Jugar: {e}")
    imagen_jugar = imagen_hover = None

# Opciones del menú
opciones = ["Jugar", "Opciones", "Salir"]
seleccion = 0  # Opción seleccionada inicialmente
anterior_seleccion = seleccion  # Para detectar cambios de selección

<<<<<<< HEAD
# Función para ejecutar los scripts usando subprocess
def ejecutar_script(script):
    subprocess.Popen([sys.executable, script])  # Ejecuta el script en un nuevo proceso
    # No llamamos a sys.exit() aquí, porque no queremos cerrar el menú principal
=======
# Función para ejecutar los scripts usando os.system()
def ejecutar_script(script):
    os.system(f'python {script}')  # Ejecutamos el script en un nuevo proceso
    sys.exit()  # Terminamos el proceso actual de Pygame
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1

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

# Función para dibujar el menú
def dibujar_menu():
    # Escalar la imagen de fondo
    if fondo_menu:
        fondo_menu_escalado = pygame.transform.scale(fondo_menu, ventana.get_size())
        ventana.blit(fondo_menu_escalado, (0, 0))

    # Calcular posición y tamaño de las opciones
    for i, opcion in enumerate(opciones):
        factor_escala = ventana.get_height() / constantes.ALTO_VENTANA  # Escalar según la altura
<<<<<<< HEAD
        x_opcion = ventana.get_width() // 8 - (200 * factor_escala) // 2 - 80  #80 píxeles hacia la izquierda
=======
        x_opcion = ventana.get_width() // 8 - (200 * factor_escala) // 2 - 80  # Ajuste de 80 píxeles hacia la izquierda
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1
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
<<<<<<< HEAD
        y_texto = y_opcion + (200 * factor_escala) // 2 - texto_opcion.get_height() // 2 - 70  # Centrado verticalmente en el botón
=======
        y_texto = y_opcion + (150 * factor_escala) // 2 - texto_opcion.get_height() // 2 -40  # Centrado verticalmente en el botón
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1

        # Dibujar el texto sobre el botón
        ventana.blit(texto_opcion, (x_texto, y_texto))

    pygame.display.flip()

# Estado de pantalla completa
pantalla_completa = False

# Reproducir el video de inicio al cargar el juego
reproducir_video_pygame("assets/menu/logo.mp4")

# Reproducir la música de fondo
pygame.mixer.music.load("assets/musica/loopmenu.mp3")
pygame.mixer.music.play(-1)  # Reproducir música en bucle

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
                    sys.exit()
            elif event.key == pygame.K_ESCAPE:  # Tecla Escape
                pygame.quit()
                sys.exit()
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
                        ejecutar_script('assets/menu/jugar.py')
                    elif seleccion == 1:
                        ejecutar_script('assets/menu/opciones.py')
                    elif seleccion == 2:
                        sys.exit()

    # Detección de hover (fuera del bucle de eventos, pero dentro del bucle principal)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for i in range(len(opciones)):
        x_opcion = ventana.get_width() // 2 - 100  # Ajustar según el tamaño escalado
<<<<<<< HEAD
        y_opcion = 250 + i * 60
=======
        y_opcion = 50 + i * 60
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1
        if x_opcion < mouse_x < x_opcion + 200 and y_opcion < mouse_y < y_opcion + 60:
            if seleccion != i:
                seleccion = i
                pygame.mixer.Sound.play(sonido_hover)

    # Dibujar el menú
    dibujar_menu()
