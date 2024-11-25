import pygame
import sys
import os
import cv2
import subprocess  # Para ejecutar "menu.py"

# Inicializar Pygame
pygame.init()

# Tamaño de la ventana
screen_size = (1200, 800)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("¡Gracias por jugar!")

# Cargar imágenes del botón
imagen_boton_normal = pygame.image.load("assets/menu/regresar.png")
imagen_boton_hover = pygame.image.load("assets/menu/regresar-hover.png")

# Redimensionar las imágenes del botón
imagen_boton_normal = pygame.transform.scale(imagen_boton_normal, (250, 150))
imagen_boton_hover = pygame.transform.scale(imagen_boton_hover, (250, 150))

# Dimensiones del botón
boton_width = imagen_boton_normal.get_width()
boton_height = imagen_boton_normal.get_height()

# Configuración del botón "Regresar"
button_rect = pygame.Rect(screen_size[0] - boton_width - 20, screen_size[1] - boton_height - 20, boton_width, boton_height)

# Cargar video (gracias_por_jugar.mp4) con OpenCV
video_path = "assets/menu/gracias_por_jugar.mp4"
cap = cv2.VideoCapture(video_path)

# Verificar si el video se ha abierto correctamente
if not cap.isOpened():
    print("Error al abrir el video")
    sys.exit()

# Función para ejecutar "menu.py"
def run_menu():
    pygame.quit()
    subprocess.run([sys.executable, "menu.py"])

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Si el usuario cierra la ventana
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:  # Si el usuario hace clic
            mouse_pos = event.pos  # Posición del ratón
            if button_rect.collidepoint(mouse_pos):  # Si se hizo clic en el botón
                run_menu()  # Ejecutar "menu.py"
                running = False  # Cerrar el bucle principal después de abrir "menu.py"

    # Limpiar la pantalla
    screen.fill((0, 0, 0))  # Fondo negro

    # Reproducir video
    ret, frame = cap.read()
    if ret:
        # Convertir la imagen del video (BGR -> RGB)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Obtener las dimensiones del frame
        frame_height, frame_width, _ = frame.shape

        # Crear la matriz de rotación para 330 grados
        center = (frame_width // 2, frame_height // 2)  # Centro de rotación
        rotation_matrix = cv2.getRotationMatrix2D(center, 90, 1)  # 330 grados de rotación

        # Aplicar la rotación al frame
        rotated_frame = cv2.warpAffine(frame, rotation_matrix, (frame_width, frame_height))

        # Redimensionar el frame rotado para que encaje dentro de la ventana
        video_ratio = frame_width / frame_height
        screen_ratio = screen_size[0] / screen_size[1]

        if video_ratio > screen_ratio:
            new_width = screen_size[0]
            new_height = int(new_width / video_ratio)
        else:
            new_height = screen_size[1]
            new_width = int(new_height * video_ratio)

        # Redimensionar el frame rotado
        frame_resized = cv2.resize(rotated_frame, (new_width, new_height))

        # Convertir a superficie de Pygame
        frame_surface = pygame.surfarray.make_surface(frame_resized)

        # Dibujar el frame redimensionado
        screen.blit(frame_surface, ((screen_size[0] - new_width) // 2, (screen_size[1] - new_height) // 2))
    else:
        # Si el video termina, salir del bucle y ejecutar "menu.py"
        run_menu()

    # Detectar si el ratón está sobre el botón para cambiar su imagen
    if button_rect.collidepoint(pygame.mouse.get_pos()):
        # Si el mouse está sobre el botón, mostrar la versión "hover" del botón
        screen.blit(imagen_boton_hover, (button_rect.x, button_rect.y))
    else:
        # Si no está sobre el botón, mostrar la versión normal del botón
        screen.blit(imagen_boton_normal, (button_rect.x, button_rect.y))

    # Actualizar la pantalla
    pygame.display.update()

# Salir del juego
pygame.quit()
sys.exit()
