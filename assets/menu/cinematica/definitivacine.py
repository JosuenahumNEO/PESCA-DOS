import pygame
import sys
import subprocess  # Para ejecutar otros scripts

# Inicializar Pygame
pygame.init()

# Inicializar el mixer de Pygame (esto es necesario para cargar y reproducir sonidos)
pygame.mixer.init()

# Tamaño de la ventana
screen_size = (1200, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Cinemática")

# Cargar imágenes
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

# Función para ejecutar "opciones.py"
def run_opciones():
    # Ejecutar el script "opciones.py"
    subprocess.run([sys.executable, "assets/menu/opciones.py"])

# Bucle principal
running = True
index = 0
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Si el usuario cierra la ventana
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:  # Si el usuario hace clic
            mouse_pos = event.pos  # Posición del ratón
            if button_rect.collidepoint(mouse_pos):  # Si se hizo clic en el botón
                sonido_seleccion.play()  # Reproducir el sonido
                run_opciones()  # Ejecutar el script "opciones.py"
                running = False  # Cerrar el bucle principal después de abrir "opciones.py"

    # Limpiar la pantalla con un color de fondo (opcional)
    screen.fill((0, 0, 0))  # Fondo negro

    # Mostrar la imagen actual en la secuencia
    screen.blit(cinematica[index], (0, 0))  # Mostrar imagen en la esquina superior izquierda
    
    # Mostrar el botón "Regresar"
    pygame.draw.rect(screen, button_color, button_rect)  # Dibujar el fondo del botón
    screen.blit(button_text, (button_rect.x + 40, button_rect.y + 10))  # Dibujar el texto del botón
    
    # Detectar si el ratón está sobre el botón para cambiar su color
    if button_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, button_hover_color, button_rect)  # Cambiar a un color más oscuro si está sobre él
        screen.blit(button_text, (button_rect.x + 40, button_rect.y + 10))  # Dibujar el texto encima
    
    # Actualizar la pantalla
    pygame.display.update()

    # Esperar un segundo antes de mostrar la siguiente imagen
    pygame.time.wait(1000)  # Esperar 1000 milisegundos (1 segundo)

    # Avanzar al siguiente índice de la secuencia
    index += 1
    if index >= len(cinematica):  # Si llegamos al final de la secuencia, repetir desde el inicio
        index = 0

    # Limitar la tasa de fotogramas (opcional)
    clock.tick(60)  # 60 FPS

# Salir del juego
pygame.quit()
sys.exit()
