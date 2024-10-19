import pygame
import sys
import os
import cv2  # Para cargar el video (esto se isntala en la terminal con pip install opencv-python)
import constantes

pygame.init()

COLOR_TEXTO = (0, 0, 0)

# Cargar las tipografia "assets/fonts/press.ttf"
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
    sonido_video = pygame.mixer.Sound("assets/menu/logo.mp3")  #  sonido de fondo
except pygame.error as e:
    print(f"No se pudieron cargar los sonidos: {e}")
    sys.exit()

# Crear ventana
ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))
pygame.display.set_caption("Pesca-Dos (Menú)")

# Cargar imagen de fondo
try:
    fondo_menu = pygame.image.load("assets/menu/menu.png")
    fondo_menu = pygame.transform.scale(fondo_menu, (constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))  # Escalar la imagen al tamaño de la ventana
except pygame.error as e:
    print(f"No se pudo cargar la imagen de fondo: {e}")
    fondo_menu = None  # Asignar None si no se puede cargar la imagen

# Cargar imágenes para "Jugar"
try:
    imagen_jugar = pygame.image.load("assets/menu/f(2).png")
    imagen_jugar = pygame.transform.scale(imagen_jugar, ((200, 60)))  # Escalar imagen a 200x60

    imagen_hover = pygame.image.load("assets/menu/f-hover(2).png")  # Imagen cuando está seleccionada
    imagen_hover = pygame.transform.scale(imagen_hover, ((200, 60)))
except pygame.error as e:
    print(f"No se pudieron cargar las imágenes para Jugar: {e}")
    imagen_jugar = imagen_hover = None  # Asignar None si no se pueden cargar las imágenes

# Función para reproducir el video dentro de la ventana de Pygame
def reproducir_video_pygame(ruta_video):
    cap = cv2.VideoCapture(ruta_video)
    if not cap.isOpened():
        print(f"No se pudo cargar el video: {ruta_video}")
        return

    # Reproducir sonido del video
    pygame.mixer.Sound.play(sonido_video)

    # Bucle para reproducir el video
    clock = pygame.time.Clock()  # Para controlar la velocidad de reproducción
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break       

        # Convertir el frame de OpenCV (BGR) a formato Pygame (RGB)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_surface = pygame.surfarray.make_surface(frame_rgb.swapaxes(0, 1))  # Convertir en una surface de Pygame

        # Dibujar el frame en la ventana de Pygame
        ventana.blit(pygame.transform.scale(frame_surface, (constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA)), (0, 0))
        pygame.display.update()

        # Controlar la velocidad de reproducción
        clock.tick(30)  # 30 FPS 

        # Manejar eventos de Pygame para evitar que se congele la ventana
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cap.release()
                pygame.quit()
                sys.exit()

    cap.release()

# Reproducir el video antes de mostrar el menú 
reproducir_video_pygame("assets/menu/logo.mp4")

# Opciones del menú
opciones = ["Jugar", "Opciones", "Salir"] #lista pal menú
seleccion = 0  # Opción seleccionada inicialmente
anterior_seleccion = seleccion  # Para detectar cambios de selección

# Función para dibujar el menú
def dibujar_menu():
    # Dibujar fondo
    if fondo_menu:
        ventana.blit(fondo_menu, (0, 0))  # Dibujar la imagen de fondo
    
    # Dibujar título
    titulo_texto = FUENTE_TEXTO.render("Pesca-Dos (¡Beta!)", True, (210, 219, 42))  # Cambiar el color del texto del título
    ventana.blit(titulo_texto, (constantes.ANCHO_VENTANA // 2 - titulo_texto.get_width() // 2, 100))
    
    # Dibujar opciones
    for i, opcion in enumerate(opciones):
        x_opcion = constantes.ANCHO_VENTANA // 2 - 50  # Ajustar según la posición deseada
        y_opcion = 250 + i * 60

        if seleccion == i and imagen_hover:
            ventana.blit(imagen_hover, (x_opcion - 50, y_opcion - 15))
        elif imagen_jugar:
            ventana.blit(imagen_jugar, (x_opcion - 50, y_opcion - 15))

        # Renderizar las opciones
        texto_opcion = FUENTE_OPCIONES.render(opcion, True, (255, 255, 255) if i == seleccion else (150, 77, 3))
        ventana.blit(texto_opcion, (constantes.ANCHO_VENTANA // 2 - texto_opcion.get_width() // 2, y_opcion))

    pygame.display.flip()  # Actualizar pantalla

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:  # Tecla arriba
                seleccion = (seleccion - 1) % len(opciones)
            elif event.key == pygame.K_DOWN:  # Tecla abajo
                seleccion = (seleccion + 1) % len(opciones)
            elif event.key == pygame.K_RETURN:  # Tecla Enter
                pygame.mixer.Sound.play(sonido_seleccion)  # Reproducir sonido de selección
                if seleccion == 0:  # Jugar
                    print("Iniciando juego...")
                    os.system('python assets/menu/jugar.py')  # Ejecutar el archivo de juego
                elif seleccion == 1:  # Opciones
                    print("Abriendo opciones...")
                    os.system('python assets/menu/opciones.py')  # Ejecutar el archivo de opciones
                elif seleccion == 2:  # Salir
                    pygame.quit()
                    sys.exit()

    # Reproducir sonido de hover cuando cambie la selección
    if seleccion != anterior_seleccion:
        pygame.mixer.Sound.play(sonido_hover)
        anterior_seleccion = seleccion

    dibujar_menu()  # Dibujar menú
