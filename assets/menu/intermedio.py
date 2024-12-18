import pygame
import sys
import os
<<<<<<< HEAD
import subprocess

pygame.init()
=======
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1

# Definir constantes
ANCHO_VENTANA = 1200
ALTO_VENTANA = 600
<<<<<<< HEAD
COLOR_TEXTO_NORMAL = (255, 255, 255)  # Blanco, igual que el color de texto normal en el primer código
COLOR_TEXTO_HOVER = (255, 223, 129)  # Dorado Claro o Amarillo, igual que en el primer código

# Cargar la fuente personalizada
try:
    FUENTE_TEXTO = pygame.font.Font("assets/fonts/press.ttf", 40)  # Ajusté el tamaño de la fuente
    FUENTE_OPCIONES = pygame.font.Font("assets/fonts/press.ttf", 22)  # Ajusté el tamaño de la fuente para las opciones
except pygame.error as e:
    print(f"No se pudo cargar la fuente: {e}")
    sys.exit()

# Cargar sonidos
try:
    sonido_hover = pygame.mixer.Sound("assets/musica/boton.mp3")
    sonido_seleccion = pygame.mixer.Sound("assets/musica/golpe_2.mp3")
except pygame.error as e:
    print(f"No se pudieron cargar los sonidos: {e}")
    sys.exit()

def ejecutar_script(script):
    subprocess.Popen([sys.executable, script])  # Ejecuta el script en un nuevo proceso

# Función para el menú del juego
def iniciar_juego():
=======
COLOR_TEXTO_NORMAL = (150, 77, 3)  # Color de texto predeterminado
COLOR_TEXTO_HOVER = (255, 255, 255)  # Color del texto en hover


# Función para el menú del juego
def iniciar_juego():
    pygame.init()

    # Cargar fuente
    FUENTE_TEXTO = pygame.font.Font("assets/fonts/press.ttf", 54)
    FUENTE_OPCIONES = pygame.font.Font("assets/fonts/press.ttf", 20)

    # Cargar sonidos
    try:
        sonido_hover = pygame.mixer.Sound("assets/musica/boton.mp3")
        sonido_seleccion = pygame.mixer.Sound("assets/musica/select_level.mp3")
    except pygame.error as e:
        print(f"No se pudieron cargar los sonidos: {e}")
        sys.exit()

>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1
    # Crear ventana
    ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    pygame.display.set_caption("Pesca-Dos (Intermedio)")

    # Cargar imagen de fondo
    try:
        fondo_menu = pygame.image.load("assets/menu/intermedio.png")
        fondo_menu = pygame.transform.scale(fondo_menu, (ANCHO_VENTANA, ALTO_VENTANA))  # Escalar la imagen al tamaño de la ventana
    except pygame.error as e:
        print(f"No se pudo cargar la imagen de fondo: {e}")
        fondo_menu = None

    # Tamaño de las imágenes detrás del texto
<<<<<<< HEAD
    imagen_ancho = 350  # Ajustamos a 350 como en el primer código
    imagen_alto = 100   # Ajustamos a 100 como en el primer código
=======
    imagen_ancho = 250
    imagen_alto = 90
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1

    # Cargar imágenes para las opciones
    try:
        imagen_normal = pygame.image.load("assets/menu/f(2).png")
<<<<<<< HEAD
        imagen_normal = pygame.transform.scale(imagen_normal, (imagen_ancho, imagen_alto))  # Escalar a 350x100
=======
        imagen_normal = pygame.transform.scale(imagen_normal, (imagen_ancho, imagen_alto))  # Escalar a 200x90
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1

        imagen_hover = pygame.image.load("assets/menu/f-hover(2).png")  # Imagen cuando está seleccionada
        imagen_hover = pygame.transform.scale(imagen_hover, (imagen_ancho, imagen_alto))
    except pygame.error as e:
        print(f"No se pudieron cargar las imágenes para las opciones: {e}")
        imagen_normal = imagen_hover = None

    # Opciones del menú
    opciones = ["Nivel 1", "Nivel 2", "Nivel 3", "Regresar"]
    seleccion = 0  # Opción seleccionada inicialmente
    anterior_seleccion = seleccion  # Para detectar cambios de selección

    # Variables para el movimiento del fondo
    fondo_x = 0  # Posición inicial del fondo
    velocidad_fondo = 1  # Velocidad del movimiento del fondo

    def dibujar_menu():
        # Dibujar fondo
        if fondo_menu:
            ventana.blit(fondo_menu, (fondo_x, 0))  # Dibujar la imagen de fondo
            ventana.blit(fondo_menu, (fondo_x + ANCHO_VENTANA, 0))  # Dibujar el fondo nuevamente para el efecto de bucle
        
        # Dibujar título
        titulo_texto = FUENTE_TEXTO.render("Elegir nivel", True, (255, 0, 0))  # Cambiar el color del texto del título
        ventana.blit(titulo_texto, (ANCHO_VENTANA // 2 - titulo_texto.get_width() // 2, 100))
        
        titulo_texto = FUENTE_TEXTO.render("(Intermedio)", True, (255, 0, 0))  # Cambiar el color del texto del título
        ventana.blit(titulo_texto, (ANCHO_VENTANA // 2 - titulo_texto.get_width() // 2, 180))
        
        # Dibujar opciones
        for i, opcion in enumerate(opciones):
            # Coordenadas de las opciones
<<<<<<< HEAD
            x_opcion = ANCHO_VENTANA // 2 - imagen_ancho // 2 
            y_opcion = 250 + i * 80 # Ajustar la separación vertical entre opciones
=======
            x_opcion = ANCHO_VENTANA // 2 - imagen_ancho // 2
            y_opcion = 250 + i * 90  # Ajustar la separación vertical entre opciones
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1
            
            # Cambiar la imagen y el color del texto dependiendo de si está en hover
            if i == seleccion:
                ventana.blit(imagen_hover, (x_opcion, y_opcion))  # Dibujar la imagen hover
                texto_opcion = FUENTE_OPCIONES.render(opcion, True, COLOR_TEXTO_HOVER)  # Texto blanco en hover
            else:
                ventana.blit(imagen_normal, (x_opcion, y_opcion))  # Dibujar la imagen predeterminada
                texto_opcion = FUENTE_OPCIONES.render(opcion, True, COLOR_TEXTO_NORMAL)  # Texto con color predeterminado

            # Dibujar la opción en la pantalla centrada
<<<<<<< HEAD
            ventana.blit(texto_opcion, (ANCHO_VENTANA // 2 - texto_opcion.get_width() // 2, y_opcion + 35))  # Ajustar texto sobre la imagen
=======
            ventana.blit(texto_opcion, (ANCHO_VENTANA // 2 - texto_opcion.get_width() // 2, y_opcion + 15))  # Ajustar texto sobre la imagen
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1

        pygame.display.flip()  # Actualizar pantalla

    # Bucle principal
    while True:
        # Actualizar la posición del fondo
        fondo_x -= velocidad_fondo  # Mover el fondo a la izquierda
        if fondo_x <= -ANCHO_VENTANA:  # Si el fondo se ha movido completamente
            fondo_x = 0  # Reiniciar la posición

        mouse_pos = pygame.mouse.get_pos()  # Obtener posición del mouse
        seleccion_anterior = seleccion  # Guardar la selección anterior

        # Detectar hover con el mouse
        for i in range(len(opciones)):
            x_opcion = ANCHO_VENTANA // 2 - imagen_ancho // 2
<<<<<<< HEAD
            y_opcion = 250 + i * 80
=======
            y_opcion = 250 + i * 100
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1

            # Verificar si el mouse está sobre la opción
            if x_opcion <= mouse_pos[0] <= x_opcion + imagen_ancho and y_opcion <= mouse_pos[1] <= y_opcion + imagen_alto:
                seleccion = i
                break  # Salir del bucle al encontrar la opción

        # Reproducir sonido de hover solo si la selección ha cambiado
        if seleccion != seleccion_anterior:
            pygame.mixer.Sound.play(sonido_hover)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:  # Tecla arriba
                    seleccion = (seleccion - 1) % len(opciones)
                    pygame.mixer.Sound.play(sonido_hover)
                elif event.key == pygame.K_DOWN:  # Tecla abajo
                    seleccion = (seleccion + 1) % len(opciones)
                    pygame.mixer.Sound.play(sonido_hover)
                elif event.key == pygame.K_RETURN:  # Tecla Enter
                    pygame.mixer.Sound.play(sonido_seleccion)  # Reproducir sonido de selección
                    if seleccion == 0:  # Nivel 1
                        print("Seleccionando Nivel 1...")
<<<<<<< HEAD
                        ejecutar_script('assets/niveles/intermedio/nivel1/nivel1.py')  # Ejecutar el script de Nivel 1
=======
                        os.system('python assets/niveles/principiante/nivel1/nivel1.py')  # Ejecutar el script de Nivel 1
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1
                        pygame.quit()  # Cerrar la ventana actual
                        sys.exit()  # Salir del programa
                    elif seleccion == 1:  # Nivel 2
                        print("Seleccionando Nivel 2...")
<<<<<<< HEAD
                        ejecutar_script('assets/niveles/intermedio/nivel2/nivel2.py')  # Ejecutar el script de Nivel 2
=======
                        os.system('python assets/niveles/principiante/nivel2/nivel2.py')  # Ejecutar el script de Nivel 2
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1
                        pygame.quit()  # Cerrar la ventana actual
                        sys.exit()  # Salir del programa
                    elif seleccion == 2:  # Nivel 3
                        print("Seleccionando Nivel 3...")
<<<<<<< HEAD
                        ejecutar_script('assets/niveles/intermedio/nivel3/nivel3.py')  # Ejecutar el script de Nivel 3
                        pygame.quit()  # Cerrar la ventana actual
                        sys.exit()  # Salir del programa
                    elif seleccion == 3:  # Regresar
                        
                        pygame.quit()  # Cerrar la ventana actual
                        print("Regresando al menú principal...")
                        ejecutar_script("assets/menu/jugar.py")
                        
                        sys.exit()  # Salir del programa

        # Dibujar el menú
        dibujar_menu()
        pygame.time.Clock().tick(60)  # Limitar a 60 FPS

# Ejecutar la función principal
=======
                        os.system('python assets/niveles/principiante/nivel3/nivel3.py')  # Ejecutar el script de Nivel 3
                        pygame.quit()  # Cerrar la ventana actual
                        sys.exit()  # Salir del programa
                    elif seleccion == 3:  # Regresar
                        print("Regresando al menú principal...")
                        pygame.quit()
                        os.system('python assets/menu/jugar.py')  # Ejecutar el script del menú principal

            if event.type == pygame.MOUSEBUTTONDOWN:  # Detectar clic del mouse
                if event.button == 1:  # Botón izquierdo
                    pygame.mixer.Sound.play(sonido_seleccion)  # Reproducir sonido de selección
                    if seleccion == 0:  # Nivel 1
                        print("Seleccionando Nivel 1...")
                        os.system('python assets/niveles/principiante/nivel1/nivel1.py')
                        pygame.quit()
                        sys.exit()
                    elif seleccion == 1:  # Nivel 2
                        print("Seleccionando Nivel 2...")
                        os.system('python assets/niveles/principiante/nivel2/nivel2.py')
                        pygame.quit()
                        sys.exit()
                    elif seleccion == 2:  # Nivel 3
                        print("Seleccionando Nivel 3...")
                        os.system('python assets/niveles/principiante/nivel3/nivel3.py')
                        pygame.quit()
                        sys.exit()
                    elif seleccion == 3:  # Regresar
                        print("Regresando al menú principal...")
                        pygame.quit()
                        os.system('python assets/menu/jugar.py')

        dibujar_menu()  # Dibujar menú

# Iniciar el juego
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1
iniciar_juego()
