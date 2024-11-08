import pygame
import sys
import os
import random

# Configuración del sistema
pygame.init()
pygame.mixer.init()

# Leer argumento para el estado de mostrar_video_inicio
mostrar_video_inicio = True
if len(sys.argv) > 1:
    mostrar_video_inicio = bool(int(sys.argv[1]))

# Definir constantes para el menú
ANCHO_VENTANA = 1200
ALTO_VENTANA = 600
COLOR_TEXTO_NORMAL = (255, 0, 0)
COLOR_TEXTO_HOVER = (255, 255, 255)
FUENTE_TEXTO = pygame.font.Font("assets/fonts/press.ttf", 40)
FUENTE_OPCIONES = pygame.font.Font("assets/fonts/press.ttf", 22)

# Cargar sonidos
try:
    sonido_hover = pygame.mixer.Sound("assets/musica/boton.mp3")
    sonido_seleccion = pygame.mixer.Sound("assets/musica/golpe_2.mp3")
except pygame.error as e:
    print(f"No se pudieron cargar los sonidos: {e}")
    sys.exit()

# Crear ventana
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Pesca-Dos (Opciones)")

# Cargar imagen de fondo
try:
    fondo_opciones = pygame.image.load("assets/menu/mar_muelle_nuevo2.png")
    fondo_opciones = pygame.transform.scale(fondo_opciones, (ANCHO_VENTANA, ALTO_VENTANA))
except pygame.error as e:
    print(f"No se pudo cargar la imagen de fondo: {e}")
    fondo_opciones = None

# Cargar animaciones del gato
animaciones = []
for i in range(2):
    try:
        img = pygame.image.load(f"assets/personajes/naranjo/cat_{i}.png")
        img = pygame.transform.scale(img, (160, 160))  # Escalar a 150x150
        animaciones.append(img)
    except pygame.error as e:
        print(f"No se pudo cargar la imagen: {e}")

# Opciones del menú
opciones = ["Idioma", "Historia", "Controles", "Regresar"]
seleccion = 0
anterior_seleccion = seleccion

# Variables para el movimiento del fondo y el gato
posicion_fondo_x = -20
velocidad_fondo = 0.2
posicion_gato_x = 500  # Posición inicial del gato
frame_gato = 0  # Para controlar el frame de la animación
direccion_gato = -1  # -1 para izquierda, 1 para derecha

def dibujar_menu():
    # Dibujar fondo
    if fondo_opciones:
        ventana.blit(fondo_opciones, (posicion_fondo_x, 0))
        ventana.blit(fondo_opciones, (posicion_fondo_x + ANCHO_VENTANA, 0))

    # Dibujar título
    titulo_texto = FUENTE_TEXTO.render("Opciones", True, (255, 0, 0))
    ventana.blit(titulo_texto, (ANCHO_VENTANA // 2 - titulo_texto.get_width() // 2, 100))
    
    # Dibujar opciones
    for i, opcion in enumerate(opciones):
        x_opcion = ANCHO_VENTANA // 2 - 100
        y_opcion = 250 + i * 80
        
        if i == seleccion:
            texto_opcion = FUENTE_OPCIONES.render(opcion, True, COLOR_TEXTO_HOVER)
        else:
            texto_opcion = FUENTE_OPCIONES.render(opcion, True, COLOR_TEXTO_NORMAL)

        ventana.blit(texto_opcion, (ANCHO_VENTANA // 2 - texto_opcion.get_width() // 2, y_opcion + 15))

    # Dibujar gato
    gato_actual = animaciones[frame_gato]
    if direccion_gato == 1:  # Si va hacia la derecha, invertir imagen
        gato_actual = pygame.transform.flip(gato_actual, True, False)
        
    ventana.blit(gato_actual, (posicion_gato_x, 460))

    pygame.display.flip()  # Actualizar pantalla

# Bucle principal del menú
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
                # Manejo de opciones
                if seleccion == 0:
                    print("Abriendo menú de idioma")
                    
                    pygame.quit()
                    os.system('python assets/menu/idioma.py')
                    
                elif seleccion == 1:
                    print("Abriendo historia...")
                    
                    pygame.quit()
                    os.system('python assets/menu/cinematica/definitivacine.py')
                elif seleccion == 2:
                    print("Abriendo menú")
                    
                    pygame.quit()
                    os.system('python assets/menu/controles.py')
                elif seleccion == 3:  # Regresar
                    print("Regresando al menú principal...")
                    
                    pygame.quit()
                    os.system(f'python menu.py')

        # Detectar clic del mouse
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Botón izquierdo del mouse
            mouse_x, mouse_y = event.pos
            for i, opcion in enumerate(opciones):
                x_opcion = ANCHO_VENTANA // 2 - 100
                y_opcion = 250 + i * 80
                if x_opcion <= mouse_x <= x_opcion + 200 and y_opcion + 15 <= mouse_y <= y_opcion + 55:
                    seleccion = i
                    pygame.mixer.Sound.play(sonido_seleccion)
                    # Manejo de opciones
                    if seleccion == 0:
                        print("Abriendo menú de idioma")
                        os.system('python assets/menu/idioma1.py')
                    elif seleccion == 1:
                        print("Abriendo historia...")
                        os.system('python assets/menu/cinematica/definitivacine.py')
                    elif seleccion == 2:
                        print("Abriendo menú")
                        os.system('python assets/menu/controles.py')
                    elif seleccion == 3:  # Regresar
                        print("Regresando al menú principal...")
                        os.system('python menu.py')
                    

                        pygame.quit()
                        sys.exit()

    # Detectar hover del mouse
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for i in range(len(opciones)):
        x_opcion = ANCHO_VENTANA // 2 - 100
        y_opcion = 250 + i * 80
        if x_opcion <= mouse_x <= x_opcion + 200 and y_opcion + 15 <= mouse_y <= y_opcion + 55:
            if seleccion != i:
                seleccion = i
                pygame.mixer.Sound.play(sonido_hover)
            break

    # Actualizar posición del fondo
    posicion_fondo_x -= velocidad_fondo
    if posicion_fondo_x <= -ANCHO_VENTANA - 20:
        posicion_fondo_x = -20

    # Actualizar animación del gato
    frame_gato = (frame_gato + 1) % len(animaciones)

    # Controlar la posición del gato
    posicion_gato_x += direccion_gato * 3  # Mover el gato en la dirección actual
    if posicion_gato_x < -800:  # Cambiar dirección al llegar a -800
        direccion_gato = 1  # Cambiar a ir a la derecha
    elif posicion_gato_x > ANCHO_VENTANA:  # Reiniciar posición si se sale por la derecha
        posicion_gato_x = -160  # Reiniciar posición fuera de la pantalla a la izquierda
        direccion_gato = -1  # Cambiar a ir a la izquierda

    dibujar_menu()  # Dibujar el menú

pygame.quit()
