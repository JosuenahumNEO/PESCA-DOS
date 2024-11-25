import pygame
import sys
import os
import subprocess
import constantes
import cv2
from moviepy.editor import VideoFileClip

# Inicialización de Pygame
pygame.init()

# Configuración de la pantalla con dimensiones 1200x600
SCREEN = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("AnimalBots Rescue")

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

# Cargar imagen de fondo
try:
    fondo_menu = pygame.image.load("assets/menu/menu.png")
    fondo_menu = pygame.transform.scale(fondo_menu, (1200, 600))
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

# Función para ejecutar los scripts usando subprocess
def ejecutar_script(script):
    subprocess.Popen([sys.executable, script])  # Ejecuta el script en un nuevo proceso

# Función para reproducir el video de introducción indefinidamente
def play_intro_video(video_path):
    # Usar moviepy para extraer información del video
    video_clip = VideoFileClip(video_path)
    audio = video_clip.audio
    audio.write_audiofile("temp_audio.mp3")  # Extraer audio temporalmente

    fps = video_clip.fps  # Obtener FPS del video para sincronización

    # Iniciar el audio con Pygame
    pygame.mixer.init()
    pygame.mixer.music.load("temp_audio.mp3")
    pygame.mixer.music.play(loops=-1)  # Reproducir el audio indefinidamente (loops=-1)

    # Reproducción de video usando OpenCV
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: No se pudo cargar el video.")
        return

    clock = pygame.time.Clock()

    while True:
        ret, frame = cap.read()
        if not ret:  # Si el video ha terminado, volver al principio
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Reiniciar el video
            continue  # Continuar el bucle para seguir reproduciendo el video

        # Procesar el frame (invertir, convertir color y redimensionar)
        frame = cv2.flip(frame, 1)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (1200, 600))  # Ajustar el tamaño de la imagen a la pantalla
        frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)

        # Convertir el frame a una superficie de Pygame
        frame_surface = pygame.surfarray.make_surface(frame)

        # Dibuja el frame en la pantalla
        SCREEN.blit(frame_surface, (0, 0))

        # Manejo de eventos de Pygame (para cerrar el video si se cierra la ventana)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cap.release()
                pygame.mixer.music.stop()
                pygame.quit()
                sys.exit()

        # Actualiza la pantalla
        pygame.display.update()

        # Sincronización exacta con los FPS del video
        clock.tick(fps)

    cap.release()
    pygame.mixer.music.stop()  # Detener el audio al final

# Función para dibujar el menú
def dibujar_menu():
    # Escalar la imagen de fondo
    if fondo_menu:
        fondo_menu_escalado = pygame.transform.scale(fondo_menu, SCREEN.get_size())
        SCREEN.blit(fondo_menu_escalado, (0, 0))

    # Calcular posición y tamaño de las opciones
    for i, opcion in enumerate(opciones):
        factor_escala = SCREEN.get_height() / 600  # Escalar según la altura
        x_opcion = SCREEN.get_width() // 8 - (200 * factor_escala) // 2 - 80  # 80 píxeles hacia la izquierda
        y_opcion = 250 * factor_escala + i * (100 * factor_escala)  # Aumento de la separación entre botones

        # Escalar las imágenes de los botones
        if seleccion == i and imagen_hover:
            SCREEN.blit(pygame.transform.scale(imagen_hover, (400 * factor_escala, 150 * factor_escala)), (x_opcion, y_opcion - 35))
        else:
            SCREEN.blit(pygame.transform.scale(imagen_jugar, (400 * factor_escala, 150 * factor_escala)), (x_opcion, y_opcion - 35))

        # Calcular el tamaño del texto
        texto_opcion = FUENTE_OPCIONES.render(opcion, True, (255, 255, 255) if i == seleccion else (252, 186, 3))

        # Calcular la posición del texto para centrarlo en el botón
        x_texto = x_opcion + (400 * factor_escala) // 2 - texto_opcion.get_width() // 2
        y_texto = y_opcion + (200 * factor_escala) // 2 - texto_opcion.get_height() // 2 - 70  # Centrado verticalmente en el botón

        # Dibujar el texto sobre el botón
        SCREEN.blit(texto_opcion, (x_texto, y_texto))

    pygame.display.flip()

# Función para manejar los eventos del menú y navegación
def manejar_eventos_menu():
    global seleccion
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
                x_opcion = SCREEN.get_width() // 2 - 100  # Ajustar según el tamaño escalado
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

    # Detección de hover
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for i in range(len(opciones)):
        x_opcion = SCREEN.get_width() // 2 - 100  # Ajustar según el tamaño escalado
        y_opcion = 250 + i * 60
        if x_opcion < mouse_x < x_opcion + 200 and y_opcion < mouse_y < y_opcion + 60:
            if seleccion != i:
                seleccion = i
                pygame.mixer.Sound.play(sonido_hover)

    # Dibujar el menú
    dibujar_menu()

# Reproducir el video de inicio al cargar el juego
play_intro_video("assets/menu/logo.mp4")

# Reproducir la música de fondo
pygame.mixer.music.load("assets/musica/loopmenu.mp3")
pygame.mixer.music.play()  # Reproducir música en bucle

# Bucle principal
while True:
    manejar_eventos_menu()
