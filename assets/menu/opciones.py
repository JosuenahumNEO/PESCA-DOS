import pygame
import sys
import os

pygame.init()

# Definir constantes para el menú
ANCHO_VENTANA = 1200
ALTO_VENTANA = 600
COLOR_TEXTO_NORMAL = (150, 77, 3)  # Color de texto predeterminado
COLOR_TEXTO_HOVER = (255, 255, 255)  # Color del texto en hover
FUENTE_TEXTO = pygame.font.Font("assets/fonts/press.ttf", 40)  # Fuente personalizada
FUENTE_OPCIONES = pygame.font.Font("assets/fonts/press.ttf", 22)  # Fuente para opciones

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
    fondo_opciones = pygame.image.load("assets/menu/mar_muelle.jpeg")
    fondo_opciones = pygame.transform.scale(fondo_opciones, (ANCHO_VENTANA, ALTO_VENTANA))  # Escalar la imagen al tamaño de la ventana
except pygame.error as e:
    print(f"No se pudo cargar la imagen de fondo: {e}")
    fondo_opciones = None  # Asignar None si no se puede cargar la imagen

# Tamaño de las imágenes detrás del texto
imagen_ancho = 200
imagen_alto = 60  # Cambiado a 60 para que coincida con el primer código

# Cargar imágenes para las opciones
try:
    imagen_normal = pygame.image.load("assets/menu/f(2).png")
    imagen_normal = pygame.transform.scale(imagen_normal, (imagen_ancho, imagen_alto))  # Escalar a 200x60

    imagen_hover = pygame.image.load("assets/menu/f-hover(2).png")  # Imagen cuando está seleccionada
    imagen_hover = pygame.transform.scale(imagen_hover, (imagen_ancho, imagen_alto))
except pygame.error as e:
    print(f"No se pudieron cargar las imágenes para las opciones: {e}")
    imagen_normal = imagen_hover = None

# Opciones del menú
opciones = ["Idioma", "Historia", "Controles", "Regresar"]
seleccion = 0  # Opción seleccionada inicialmente
anterior_seleccion = seleccion  # Para detectar cambios de selección

def dibujar_menu():
    # Dibujar fondo
    if fondo_opciones:
        ventana.blit(fondo_opciones, (0, 0))  # Dibujar la imagen de fondo
    
    # Dibujar título del menú de opciones en color rojo
    titulo_texto = FUENTE_TEXTO.render("Opciones", True, (255, 0, 0))  # Color rojo
    ventana.blit(titulo_texto, (ANCHO_VENTANA // 2 - titulo_texto.get_width() // 2, 100))
    
    # Dibujar las opciones del menú
    for i, opcion in enumerate(opciones):
        # Coordenadas de las opciones
        x_opcion = ANCHO_VENTANA // 2 - imagen_ancho // 2
        y_opcion = 250 + i * 80  # Ajustar la separación vertical entre opciones (reducido a 80)
        
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

# Bucle principal del menú
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:  # Tecla arriba
                seleccion = (seleccion - 1) % len(opciones)
                pygame.mixer.Sound.play(sonido_hover)  # Reproducir sonido de hover
            elif event.key == pygame.K_DOWN:  # Tecla abajo
                seleccion = (seleccion + 1) % len(opciones)
                pygame.mixer.Sound.play(sonido_hover)  # Reproducir sonido de hover
            elif event.key == pygame.K_RETURN:  # Tecla Enter
                pygame.mixer.Sound.play(sonido_seleccion)  # Reproducir sonido de selección
                if seleccion == 0:  # Opción Idioma
                    print("Abriendo menú de idioma")
                    os.system('python assets/menu/idioma.py')
                elif seleccion == 1:  # Opción Historia
                    print("Abriendo historia...")
                    os.system('python assets/menu/cinematica/definitivacine.py')  # Cambia 'python' por 'python3' si es necesario
                elif seleccion == 2:  # Opción Controles
                    print("Abriendo menú")
                    os.system('python assets/menu/controles.py')
                elif seleccion == 3:  # Opción Regresar
                    print("Regresando al menú principal...")
                    os.system('python menu.py')  # Cambia 'python' por 'python3' si es necesario
                    pygame.quit()
                    sys.exit()

    # Reproducir sonido de hover cuando cambie la selección
    if seleccion != anterior_seleccion:
        pygame.mixer.Sound.play(sonido_hover)
        anterior_seleccion = seleccion

    dibujar_menu()  # Dibujar el menú
