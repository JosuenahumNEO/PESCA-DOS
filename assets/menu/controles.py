import pygame
import sys
import os
<<<<<<< HEAD
import subprocess
=======
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1

# Definir constantes
ANCHO_VENTANA = 1200
ALTO_VENTANA = 600
COLOR_TEXTO_NORMAL = (150, 77, 3)  # Color de texto predeterminado
COLOR_TEXTO_HOVER = (255, 255, 255)  # Color del texto en hover

<<<<<<< HEAD
img_controles = pygame.image.load("assets/menu/controles.png")
img_controles = pygame.transform.scale(img_controles, (1150,600))

def ejecutar_script(script):
    subprocess.Popen([sys.executable, script])  # Ejecuta el script en un nuevo proceso
=======
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1
# Función para el menú del juego
def iniciar_juego():
    pygame.init()

    # Cargar fuente
    FUENTE_TEXTO = pygame.font.Font("assets/fonts/press.ttf", 54)
    FUENTE_OPCIONES = pygame.font.Font("assets/fonts/press.ttf", 20)

    # Cargar sonidos
    try:
        sonido_hover = pygame.mixer.Sound("assets/musica/boton.mp3")
        sonido_seleccion = pygame.mixer.Sound("assets/musica/golpe_2.mp3")
    except pygame.error as e:
        print(f"No se pudieron cargar los sonidos: {e}")
        sys.exit()

    # Crear ventana
    ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    pygame.display.set_caption("Pesca-Dos (Controles)")

    # Cargar imagen de fondo
    try:
        fondo_menu = pygame.image.load("assets/menu/f(1).png")
        fondo_menu = pygame.transform.scale(fondo_menu, (ANCHO_VENTANA, ALTO_VENTANA))  # Escalar la imagen al tamaño de la ventana
    except pygame.error as e:
        print(f"No se pudo cargar la imagen de fondo: {e}")
        fondo_menu = None  # Asignar None si no se puede cargar la imagen

    # Tamaño de las imágenes detrás del texto
<<<<<<< HEAD
    imagen_ancho = 270
    imagen_alto = 140

    # Cargar imágenes para las opciones
    try:
        imagen_normal = pygame.image.load("assets/menu/regresar.png")
        imagen_normal = pygame.transform.scale(imagen_normal, (imagen_ancho, imagen_alto))  # Escalar a 270x140

        imagen_hover = pygame.image.load("assets/menu/regresar-hover.png")  # Imagen cuando está seleccionada
=======
    imagen_ancho = 200
    imagen_alto = 60

    # Cargar imágenes para las opciones
    try:
        imagen_normal = pygame.image.load("assets/menu/f(2).png")
        imagen_normal = pygame.transform.scale(imagen_normal, (imagen_ancho, imagen_alto))  # Escalar a 200x90

        imagen_hover = pygame.image.load("assets/menu/f-hover(2).png")  # Imagen cuando está seleccionada
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1
        imagen_hover = pygame.transform.scale(imagen_hover, (imagen_ancho, imagen_alto))
    except pygame.error as e:
        print(f"No se pudieron cargar las imágenes para las opciones: {e}")
        imagen_normal = imagen_hover = None

<<<<<<< HEAD
    # Posición del botón
    x_opcion = 900
    y_opcion = 490

    # Variable para controlar la reproducción del sonido de hover
    sonido_reproducido = False

    # Función para dibujar el menú
    def dibujar_menu():
        nonlocal sonido_reproducido  # Hacer que la variable sonido_reproducido se use correctamente

        # Dibujar fondo
        if fondo_menu:
            ventana.blit(fondo_menu, (0, 0))  # Dibujar la imagen de fondo
        ventana.blit(img_controles,(0,0))

        # Dibujar título
        titulo_texto = FUENTE_TEXTO.render("Controles", True, (54, 28, 6))  # Cambiar el color del texto del título
        ventana.blit(titulo_texto, (ANCHO_VENTANA // 2 - titulo_texto.get_width() // 2, 20))

        # Detectar si el mouse está sobre el botón
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if x_opcion <= mouse_x <= x_opcion + imagen_ancho and y_opcion <= mouse_y <= y_opcion + imagen_alto:
            ventana.blit(imagen_hover, (x_opcion, y_opcion))  # Mostrar imagen hover
            texto_opcion = FUENTE_OPCIONES.render("", True, COLOR_TEXTO_HOVER)

            # Reproducir sonido de hover solo si no se ha reproducido aún
            if not sonido_reproducido:
                pygame.mixer.Sound.play(sonido_hover)
                sonido_reproducido = True
        else:
            ventana.blit(imagen_normal, (x_opcion, y_opcion))  # Mostrar imagen normal
            texto_opcion = FUENTE_OPCIONES.render("", True, COLOR_TEXTO_NORMAL)
            sonido_reproducido = False  # Restablecer el sonido cuando el mouse ya no está sobre el botón

        # Dibujar la opción (en este caso, no hay texto, solo el botón)
        ventana.blit(texto_opcion, (x_opcion + imagen_ancho // 2 - texto_opcion.get_width() // 2, y_opcion + imagen_alto // 2))
=======
    # Opciones del menú
    opciones = ["Regresar"]
    seleccion = 0  # Opción seleccionada inicialmente
    anterior_seleccion = seleccion  # Para detectar cambios de selección

    def dibujar_menu():
        # Dibujar fondo
        if fondo_menu:
            ventana.blit(fondo_menu, (0, 0))  # Dibujar la imagen de fondo
        
        # Dibujar título
        titulo_texto = FUENTE_TEXTO.render("Elegir nivel", True, (255,0,0))  # Cambiar el color del texto del título
        ventana.blit(titulo_texto, (ANCHO_VENTANA // 2 - titulo_texto.get_width() // 2, 100))
        
        # Dibujar opciones
        for i, opcion in enumerate(opciones):
            # Coordenadas de las opciones
            x_opcion = ANCHO_VENTANA // 2 - imagen_ancho // 2
            y_opcion = 250 + i * 100  # Ajustar la separación vertical entre opciones
            
            # Cambiar la imagen y el color del texto dependiendo de si está en hover
            if i == seleccion:
                ventana.blit(imagen_hover, (x_opcion, y_opcion))  # Dibujar la imagen hover
                texto_opcion = FUENTE_OPCIONES.render(opcion, True, COLOR_TEXTO_HOVER)  # Texto blanco en hover
            else:
                ventana.blit(imagen_normal, (x_opcion, y_opcion))  # Dibujar la imagen predeterminada
                texto_opcion = FUENTE_OPCIONES.render(opcion, True, COLOR_TEXTO_NORMAL)  # Texto con color predeterminado

            # Dibujar la opción en la pantalla centrada
            ventana.blit(texto_opcion, (ANCHO_VENTANA // 2 - texto_opcion.get_width() // 2, y_opcion + 15))  # Ajustar texto sobre la imagen
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1

        pygame.display.flip()  # Actualizar pantalla

    # Bucle principal
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
<<<<<<< HEAD
                if event.key == pygame.K_RETURN:  # Tecla Enter
                    pygame.mixer.Sound.play(sonido_seleccion)  # Reproducir sonido de selección
                    
                    
                    print("Botón seleccionado con Enter")
                    pygame.quit()
                    # Acción cuando se selecciona el botón
                    ejecutar_script("assets/menu/opciones.py")

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Clic izquierdo del mouse
                    # Acción cuando se hace clic en el botón
                    pygame.mixer.Sound.play(sonido_seleccion)
                    
                    print("Botón seleccionado con clic")
                    pygame.quit()
                    
                    ejecutar_script("assets/menu/opciones.py")
=======
                if event.key == pygame.K_UP:  # Tecla arriba
                    seleccion = (seleccion - 1) % len(opciones)
                    
                elif event.key == pygame.K_DOWN:  # Tecla abajo
                    seleccion = (seleccion + 1) % len(opciones)
                    
                elif event.key == pygame.K_RETURN:  # Tecla Enter
                    pygame.mixer.Sound.play(sonido_seleccion)  # Reproducir sonido de selección
                    if seleccion == 0:  # Regresar
                        print("Seleccionando Nivel 1...")
                        pygame.quit()
                        os.system('python assets/menu/opciones.py')  # Ejecutar el script de Nivel 1

                elif event.key == pygame.K_ESCAPE or event.key == pygame.K_LEFT:  # Tecla ESC
                    pygame.mixer.Sound.play(sonido_seleccion)
                    print("Regresando a opciones...")
                    os.system('python assets/menu/opciones.py')  # Ejecutar el script de opciones
                    pygame.quit()
                    sys.exit()

        # Reproducir sonido de hover cuando cambie la selección
        if seleccion != anterior_seleccion:
            pygame.mixer.Sound.play(sonido_hover)
            anterior_seleccion = seleccion
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1

        dibujar_menu()  # Dibujar menú

# Iniciar el juego
iniciar_juego()
