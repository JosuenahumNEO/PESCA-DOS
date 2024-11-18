import pygame
import sys
import os
import json  # Importar el módulo para leer JSON

# Configuración del sistema
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))  # Para saltar 3 carpetas hacia arriba

# Inicializar Pygame
pygame.init()
pygame.mixer.init()

# Definir constantes
ANCHO_VENTANA = 1200
ALTO_VENTANA = 600
COLOR_TEXTO_NORMAL = (150, 77, 3)  # Color del texto predeterminado
COLOR_TEXTO_HOVER = (255, 255, 255)  # Color del texto cuando está en hover

# Cargar la fuente personalizada
try:
    FUENTE_TEXTO = pygame.font.Font("assets/fonts/press.ttf", 50)
    FUENTE_OPCIONES = pygame.font.Font("assets/fonts/press.ttf", 20)
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

# Cargar el archivo JSON de idiomas
def cargar_idioma(idioma):
    try:
        with open("idioma.json", "r", encoding="utf-8") as file:
            idiomas = json.load(file)
        return idiomas.get(idioma, idiomas["es"])  # Si no encuentra el idioma, carga el español
    except json.JSONDecodeError as e:
        print(f"Error en el formato del JSON: {e}")
    except FileNotFoundError as e:
        print(f"No se pudo encontrar el archivo de idiomas: {e}")
    except Exception as e:
        print(f"Error al cargar el archivo de idiomas: {e}")
    return {}

# Cargar textos en español por defecto
textos = cargar_idioma("es")  # Inicialmente se carga el idioma español

# Opciones del menú
opciones = [textos["español"], textos["ingles"], textos["regresar"]]
seleccion = 0  # Opción seleccionada inicialmente
anterior_seleccion = seleccion  # Para detectar cambios de selección

# Configuración de la ventana
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Pesca-Dos (Idioma)")

# Cargar imagen de fondo
try:
    fondo_menu = pygame.image.load("assets/menu/mar.jpeg")
    fondo_menu = pygame.transform.scale(fondo_menu, (ANCHO_VENTANA, ALTO_VENTANA))  # Escalar la imagen al tamaño de la ventana
except pygame.error as e:
    print(f"No se pudo cargar la imagen de fondo: {e}")
    fondo_menu = None  # Asignar None si no se puede cargar la imagen

# Tamaño de las imágenes detrás del texto
imagen_ancho = 270
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

def dibujar_menu():
    # Dibujar fondo
    if fondo_menu:
        ventana.blit(fondo_menu, (0, 0))  # Dibujar la imagen de fondo
    
    # Dibujar título
    titulo_texto = FUENTE_TEXTO.render(textos["idioma"], True, (255,0,0))  # Cambiar el color del texto del título
    ventana.blit(titulo_texto, (ANCHO_VENTANA // 2 - titulo_texto.get_width() // 2, 80))
    
    # Dibujar opciones
    for i, opcion in enumerate(opciones):
        # Coordenadas de las opciones
        x_opcion = ANCHO_VENTANA // 2 - imagen_ancho // 2
        y_opcion = 200 + i * 80  # Ajustar la separación vertical para acercarlo más al título
        
        # Cambiar la imagen según si la opción está seleccionada o no (hover)
        if i == seleccion:
            ventana.blit(imagen_hover, (x_opcion, y_opcion))  # Dibujar la imagen de hover
            texto_opcion = FUENTE_OPCIONES.render(opcion, True, COLOR_TEXTO_HOVER)  # Cambiar el color del texto a blanco en hover
        else:
            ventana.blit(imagen_normal, (x_opcion, y_opcion))  # Dibujar la imagen predeterminada
            texto_opcion = FUENTE_OPCIONES.render(opcion, True, COLOR_TEXTO_NORMAL)  # Color del texto predeterminado
        
        # Dibujar la opción en la pantalla centrada
        ventana.blit(texto_opcion, (ANCHO_VENTANA // 2 - texto_opcion.get_width() // 2, y_opcion + 15))  # Ajustar texto sobre la imagen

    pygame.display.flip()  # Actualizar pantalla

# Función para detectar si el mouse está sobre una opción
def obtener_opcion_con_mouse(mouse_pos):
    for i, opcion in enumerate(opciones):
        x_opcion = ANCHO_VENTANA // 2 - imagen_ancho // 2
        y_opcion = 200 + i * 80
        rect_opcion = pygame.Rect(x_opcion, y_opcion, imagen_ancho, imagen_alto)
        
        # Comprobar si el mouse está dentro del área del botón
        if rect_opcion.collidepoint(mouse_pos):
            return i
    return None

# Bucle principal con detección de mouse
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEMOTION:  # Movimiento del mouse
            mouse_pos = event.pos
            seleccion = obtener_opcion_con_mouse(mouse_pos)  # Cambiar la opción seleccionada según la posición del mouse

        if event.type == pygame.MOUSEBUTTONDOWN:  # Click del mouse
            if seleccion is not None:
                pygame.mixer.Sound.play(sonido_seleccion)  # Reproducir sonido de selección
                if seleccion == 0:  # Español
                    print("Cambiando a español")
                    textos = cargar_idioma("es")
                    opciones = [textos["español"], textos["ingles"], textos["regresar"]]
                elif seleccion == 1:  # Inglés
                    print("Cambiando a inglés")
                    textos = cargar_idioma("en")
                    opciones = [textos["español"], textos["ingles"], textos["regresar"]]
                elif seleccion == 2:  # Regresar
                    print("Regresando al menú de Opciones")
                    pygame.quit()
                    os.system('python assets/menu/opciones.py')

    # Reproducir sonido de hover cuando cambie la selección
    if seleccion != anterior_seleccion:
        pygame.mixer.Sound.play(sonido_hover)
        anterior_seleccion = seleccion

    dibujar_menu()  # Dibujar menú
