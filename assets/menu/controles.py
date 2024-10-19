import pygame
import sys
import os

# Definir constantes
ANCHO_VENTANA = 1200
ALTO_VENTANA = 600
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
        sonido_seleccion = pygame.mixer.Sound("assets/musica/golpe_2.mp3")
    except pygame.error as e:
        print(f"No se pudieron cargar los sonidos: {e}")
        sys.exit()

    # Crear ventana
    ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    pygame.display.set_caption("Pesca-Dos (Principiante)")

    # Cargar imagen de fondo
    try:
        fondo_menu = pygame.image.load("assets/menu/f(1).png")
        fondo_menu = pygame.transform.scale(fondo_menu, (ANCHO_VENTANA, ALTO_VENTANA))  # Escalar la imagen al tamaño de la ventana
    except pygame.error as e:
        print(f"No se pudo cargar la imagen de fondo: {e}")
        fondo_menu = None  # Asignar None si no se puede cargar la imagen

    # Tamaño de las imágenes detrás del texto
    imagen_ancho = 200
    imagen_alto = 60

    # Cargar imágenes para las opciones
    try:
        imagen_normal = pygame.image.load("assets/menu/f(2).png")
        imagen_normal = pygame.transform.scale(imagen_normal, (imagen_ancho, imagen_alto))  # Escalar a 200x90

        imagen_hover = pygame.image.load("assets/menu/f-hover(2).png")  # Imagen cuando está seleccionada
        imagen_hover = pygame.transform.scale(imagen_hover, (imagen_ancho, imagen_alto))
    except pygame.error as e:
        print(f"No se pudieron cargar las imágenes para las opciones: {e}")
        imagen_normal = imagen_hover = None

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
                    if seleccion == 0:  # Regresar
                        print("Seleccionando Nivel 1...")
                        os.system('python assets/menu/opciones.py')  # Ejecutar el script de Nivel 1
                        pygame.quit()  # Cerrar la ventana actual
                        sys.exit()  # Salir del programa

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

        dibujar_menu()  # Dibujar menú

# Iniciar el juego
iniciar_juego()
