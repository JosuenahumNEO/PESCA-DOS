import pygame
import sys
import os
import cv2
import constantes

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
    sonido_video = pygame.mixer.Sound("assets/menu/logo.mp3")
    
except pygame.error as e:
    print(f"No se pudieron cargar los sonidos: {e}")
    sys.exit()

ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))
pygame.display.set_caption("Pesca-Dos (Menú)")

# Cargar imagen de fondo
try:
    fondo_menu = pygame.image.load("assets/menu/menu.jpeg")
    fondo_menu = pygame.transform.scale(fondo_menu, (constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))
except pygame.error as e:
    print(f"No se pudo cargar la imagen de fondo: {e}")
    fondo_menu = None

try:
    imagen_jugar = pygame.image.load("assets/menu/f(2).png")
    imagen_jugar = pygame.transform.scale(imagen_jugar, (200, 60))

    imagen_hover = pygame.image.load("assets/menu/f-hover(2).png")
    imagen_hover = pygame.transform.scale(imagen_hover, (200, 60))
except pygame.error as e:
    print(f"No se pudieron cargar las imágenes para Jugar: {e}")
    imagen_jugar = imagen_hover = None

# Reproduce el video solo si se debe mostrar
def reproducir_video_pygame(ruta_video):
    cap = cv2.VideoCapture(ruta_video)
    if not cap.isOpened():
        print(f"No se pudo cargar el video: {ruta_video}")
        return

    pygame.mixer.Sound.play(sonido_video)

    clock = pygame.time.Clock()
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_surface = pygame.surfarray.make_surface(frame_rgb.swapaxes(0, 1))

        ventana.blit(pygame.transform.scale(frame_surface, (constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA)), (0, 0))
        pygame.display.update()

        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cap.release()
                pygame.quit()
                sys.exit()

    cap.release()

# Inicializar el tiempo para el retraso
tiempo_inicio = pygame.time.get_ticks()



opciones = ["Jugar", "Opciones", "Salir"]
seleccion = 0
anterior_seleccion = seleccion

def dibujar_menu():
    if fondo_menu:
        ventana.blit(fondo_menu, (0, 0))
    
    #titulo_texto = FUENTE_TEXTO.render("Pesca-Dos (¡Beta!)", True, (210, 219, 42))
    #ventana.blit(titulo_texto, (constantes.ANCHO_VENTANA // 2 - titulo_texto.get_width() // 2, 100))
    
    for i, opcion in enumerate(opciones):
        x_opcion = constantes.ANCHO_VENTANA // 2 - 50
        y_opcion = 250 + i * 60

        if seleccion == i and imagen_hover:
            ventana.blit(imagen_hover, (x_opcion - 50, y_opcion - 15))
        elif imagen_jugar:
            ventana.blit(imagen_jugar, (x_opcion - 50, y_opcion - 15))

        texto_opcion = FUENTE_OPCIONES.render(opcion, True, (255, 255, 255) if i == seleccion else (150, 77, 3))
        ventana.blit(texto_opcion, (constantes.ANCHO_VENTANA // 2 - texto_opcion.get_width() // 2, y_opcion))

    pygame.display.flip()

# Reproducir el video de inicio si se necesita
if mostrar_video_inicio:
    reproducir_video_pygame("assets/menu/logo.mp4")

while True:
    mouse_pos = pygame.mouse.get_pos()  # Obtener la posición actual del mouse

    # Verificar si han pasado los 3 segundos desde que se inició el juego
    if pygame.time.get_ticks() - tiempo_inicio >= 3000:  # 3000 ms = 3 segundos
        if not pygame.mixer.music.get_busy():  # Si la música no está sonando
            
            
            # Detener cualquier música que esté sonando antes de cargar el nivel
            pygame.mixer.stop()  # Detiene todos los sonidos y música en curso


            
            pygame.mixer.music.load("assets/musica/loopmenu.mp3")  # Cargar música
            pygame.mixer.music.play(-1)  # Reproducir en bucle

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                seleccion = (seleccion - 1) % len(opciones)
            elif event.key == pygame.K_DOWN:
                seleccion = (seleccion + 1) % len(opciones)
            elif event.key == pygame.K_RETURN:
                pygame.mixer.Sound.play(sonido_seleccion)
                if seleccion == 0:  # Jugar
                    print("Iniciando juego...")
                    os.system('python assets/menu/jugar.py')
                elif seleccion == 1:  # Opciones
                    print("Abriendo opciones...")
                    mostrar_video_inicio = False  # Cambiar la variable aquí
                    os.system(f'python assets/menu/opciones.py {int(mostrar_video_inicio)}')
                elif seleccion == 2:  # Salir
                    pygame.quit()
                    sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for i in range(len(opciones)):
                x_opcion = constantes.ANCHO_VENTANA // 2 - 50
                y_opcion = 250 + i * 60
                if x_opcion - 50 < mouse_pos[0] < x_opcion + 150 and y_opcion - 15 < mouse_pos[1] < y_opcion + 45:
                    seleccion = i
                    pygame.mixer.Sound.play(sonido_seleccion)
                    if seleccion == 0:  # Jugar
                        print("Iniciando juego...")
                        os.system('python assets/menu/jugar.py')
                    elif seleccion == 1:  # Opciones
                        print("Abriendo opciones...")
                        mostrar_video_inicio = False  # Cambiar la variable aquí
                        os.system(f'python assets/menu/opciones.py {int(mostrar_video_inicio)}')
                    elif seleccion == 2:  # Salir
                        pygame.quit()
                        sys.exit()

    # Cambiar la selección si el mouse está sobre una opción
    for i in range(len(opciones)):
        x_opcion = constantes.ANCHO_VENTANA // 2 - 50
        y_opcion = 250 + i * 60
        if x_opcion - 50 < mouse_pos[0] < x_opcion + 150 and y_opcion - 15 < mouse_pos[1] < y_opcion + 45:
            seleccion = i
            break  # Salir del bucle si se encontró un hover

    if seleccion != anterior_seleccion:
        pygame.mixer.Sound.play(sonido_hover)
        anterior_seleccion = seleccion

    dibujar_menu()  # Dibujar menú
