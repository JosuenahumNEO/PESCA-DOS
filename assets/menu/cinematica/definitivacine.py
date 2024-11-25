import pygame
import sys
import subprocess  # Para ejecutar otros scripts

# Inicializar Pygame
pygame.init()

# Inicializar el mixer de Pygame (esto es necesario para cargar y reproducir sonidos)
pygame.mixer.init()

<<<<<<< HEAD
def ejecutar_script(script):
    subprocess.Popen([sys.executable, script])  # Ejecuta el script en un nuevo proceso
=======
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1
# Tamaño de la ventana
screen_size = (1200, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Cinemática")

<<<<<<< HEAD
# Cargar imágenes de las cinemáticas
=======
# Cargar imágenes
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1
imagen1 = pygame.image.load("assets/menu/cinematica/imagenes/imagen1.png")
imagen2 = pygame.image.load("assets/menu/cinematica/imagenes/imagen2.png")
imagen3 = pygame.image.load("assets/menu/cinematica/imagenes/imagen3.png")
imagen4 = pygame.image.load("assets/menu/cinematica/imagenes/imagen4.png")
imagen5 = pygame.image.load("assets/menu/cinematica/imagenes/imagen5.png")
imagen6 = pygame.image.load("assets/menu/cinematica/imagenes/imagen6.png")
imagen7 = pygame.image.load("assets/menu/cinematica/imagenes/imagen7.png")
imagen8 = pygame.image.load("assets/menu/cinematica/imagenes/imagen8.png")
imagen9 = pygame.image.load("assets/menu/cinematica/imagenes/imagen9.png")
imagen10 = pygame.image.load("assets/menu/cinematica/imagenes/imagen10.png")
imagen11 = pygame.image.load("assets/menu/cinematica/imagenes/imagen11.png")
imagen12 = pygame.image.load("assets/menu/cinematica/imagenes/imagen12.png")
imagen13 = pygame.image.load("assets/menu/cinematica/imagenes/imagen13.png")
imagen14 = pygame.image.load("assets/menu/cinematica/imagenes/imagen14.png")
imagen15 = pygame.image.load("assets/menu/cinematica/imagenes/imagen15.png")
imagen16 = pygame.image.load("assets/menu/cinematica/imagenes/imagen16.png")
imagen17 = pygame.image.load("assets/menu/cinematica/imagenes/imagen17.png")
imagen18 = pygame.image.load("assets/menu/cinematica/imagenes/imagen18.png")
imagen19 = pygame.image.load("assets/menu/cinematica/imagenes/imagen19.png")
imagen20 = pygame.image.load("assets/menu/cinematica/imagenes/imagen20.png")
imagen21 = pygame.image.load("assets/menu/cinematica/imagenes/imagen21.png")
imagen22 = pygame.image.load("assets/menu/cinematica/imagenes/imagen22.png")
imagen23 = pygame.image.load("assets/menu/cinematica/imagenes/imagen23.png")
<<<<<<< HEAD
cinematica = [imagen1, imagen2, imagen3, imagen4, imagen5, imagen6, imagen7, imagen8,
    imagen9, imagen10, imagen11, imagen12, imagen13, imagen14, imagen15, imagen16,
    imagen17, imagen18, imagen19, imagen20, imagen21, imagen22, imagen23]  

# Cargar sonido
sonido_seleccion = pygame.mixer.Sound("assets/musica/golpe_2.mp3")

# Cargar imágenes para el botón "Regresar"
imagen_boton_normal = pygame.image.load("assets/menu/regresar.png")
imagen_boton_hover = pygame.image.load("assets/menu/regresar-hover.png")

# Redimensionar las imágenes del botón a 200x300 píxeles
imagen_boton_normal = pygame.transform.scale(imagen_boton_normal, (200, 100))
imagen_boton_hover = pygame.transform.scale(imagen_boton_hover, (200, 100))

# Dimensiones del botón (ya redimensionado)
boton_width = imagen_boton_normal.get_width()
boton_height = imagen_boton_normal.get_height()

# Configuración del botón "Regresar" en la esquina inferior derecha
button_rect = pygame.Rect(screen_size[0] - boton_width - 20, screen_size[1] - boton_height - 20, boton_width, boton_height)
=======
# Añadir las demás imágenes de la secuencia
cinematica = [imagen1, imagen2, imagen3, imagen4, imagen5, imagen6, imagen7, imagen8,
    imagen9, imagen10, imagen11, imagen12, imagen13, imagen14, imagen15, imagen16,
    imagen17, imagen18, imagen19, imagen20, imagen21, imagen22, imagen23]  # Agrega las demás imágenes aquí

# Cargar sonido
sonido_seleccion = pygame.mixer.Sound("assets/musica/select_level.mp3")

# Configuración del botón "Regresar"
button_font = pygame.font.SysFont("Arial", 30)
button_color = (255, 0, 0)  # Rojo
button_hover_color = (200, 0, 0)  # Rojo más oscuro
button_rect = pygame.Rect(650, 500, 140, 50)  # Posición y tamaño del botón
button_text = button_font.render("Regresar", True, (255, 255, 255))  # Texto del botón
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1

# Función para ejecutar "opciones.py"
def run_opciones():
    # Ejecutar el script "opciones.py"
<<<<<<< HEAD
    pygame.quit()
=======
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1
    subprocess.run([sys.executable, "assets/menu/opciones.py"])

# Bucle principal
running = True
<<<<<<< HEAD
index = 0  # Índice de la imagen actual
clock = pygame.time.Clock()

# Estado del botón
boton_hover = False  # El botón no está en estado hover por defecto

=======
index = 0
clock = pygame.time.Clock()

>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Si el usuario cierra la ventana
            running = False

<<<<<<< HEAD
        if event.type == pygame.MOUSEMOTION:  # Si el ratón se mueve
            # Detectar si el ratón está sobre el botón
            if button_rect.collidepoint(event.pos):
                boton_hover = True  # El ratón está sobre el botón
            else:
                boton_hover = False  # El ratón no está sobre el botón

=======
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1
        if event.type == pygame.MOUSEBUTTONDOWN:  # Si el usuario hace clic
            mouse_pos = event.pos  # Posición del ratón
            if button_rect.collidepoint(mouse_pos):  # Si se hizo clic en el botón
                sonido_seleccion.play()  # Reproducir el sonido
                run_opciones()  # Ejecutar el script "opciones.py"
                running = False  # Cerrar el bucle principal después de abrir "opciones.py"
<<<<<<< HEAD
        
        if event.type == pygame.KEYDOWN:  # Detectar presion de teclas
            if event.key == pygame.K_RIGHT:  # Flecha derecha
                index += 1  # Avanzar a la siguiente imagen
                if index >= len(cinematica):  # Si estamos al final, volver al inicio
                    index = 0
            elif event.key == pygame.K_LEFT:  # Flecha izquierda
                index -= 1  # Retroceder a la imagen anterior
                if index < 0:  # Si estamos al principio, volver al final
                    index = len(cinematica) - 1
            elif event.key == pygame.K_RETURN:  # Si se presiona "Enter"
                if button_rect.collidepoint(pygame.mouse.get_pos()):
                    sonido_seleccion.play()  # Reproducir el sonido
                    run_opciones()  # Ejecutar el script "opciones.py"
                    
=======
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1

    # Limpiar la pantalla con un color de fondo (opcional)
    screen.fill((0, 0, 0))  # Fondo negro

    # Mostrar la imagen actual en la secuencia
    screen.blit(cinematica[index], (0, 0))  # Mostrar imagen en la esquina superior izquierda
    
<<<<<<< HEAD
    # Detectar si el ratón está sobre el botón para cambiar su imagen
    if boton_hover:
        # Si el mouse está sobre el botón, mostrar la versión "hover" del botón
        screen.blit(imagen_boton_hover, (button_rect.x, button_rect.y))
    else:
        # Si no está sobre el botón, mostrar la versión normal del botón
        screen.blit(imagen_boton_normal, (button_rect.x, button_rect.y))
=======
    # Mostrar el botón "Regresar"
    pygame.draw.rect(screen, button_color, button_rect)  # Dibujar el fondo del botón
    screen.blit(button_text, (button_rect.x + 40, button_rect.y + 10))  # Dibujar el texto del botón
    
    # Detectar si el ratón está sobre el botón para cambiar su color
    if button_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, button_hover_color, button_rect)  # Cambiar a un color más oscuro si está sobre él
        screen.blit(button_text, (button_rect.x + 40, button_rect.y + 10))  # Dibujar el texto encima
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1
    
    # Actualizar la pantalla
    pygame.display.update()

<<<<<<< HEAD
=======
    # Esperar un segundo antes de mostrar la siguiente imagen
    pygame.time.wait(1000)  # Esperar 1000 milisegundos (1 segundo)

    # Avanzar al siguiente índice de la secuencia
    index += 1
    if index >= len(cinematica):  # Si llegamos al final de la secuencia, repetir desde el inicio
        index = 0

>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1
    # Limitar la tasa de fotogramas (opcional)
    clock.tick(60)  # 60 FPS

# Salir del juego
pygame.quit()
sys.exit()
