import pygame
import sys
import os
import json  # Importar el módulo para leer JSON
<<<<<<< HEAD
import subprocess
=======
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1

# Configuración del sistema
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))  # Para saltar 3 carpetas hacia arriba

# Inicializar Pygame
pygame.init()
pygame.mixer.init()

# Definir constantes
ANCHO_VENTANA = 1200
ALTO_VENTANA = 600
<<<<<<< HEAD
COLOR_TEXTO_NORMAL = (54, 28, 6)  # Color del texto predeterminado
COLOR_TEXTO_HOVER = (255, 255, 255)  # Color del texto cuando está en hover

def ejecutar_script(script):
    subprocess.Popen([sys.executable, script])  # Ejecuta el script en un nuevo proceso
# Cargar la fuente personalizada
def cargar_fuentes():
    try:
        fuente_texto = pygame.font.Font("assets/fonts/press.ttf", 50)
        fuente_opciones = pygame.font.Font("assets/fonts/press.ttf", 20)
        return fuente_texto, fuente_opciones
    except pygame.error as e:
        print(f"No se pudo cargar la fuente: {e}")
        sys.exit()

# Cargar sonidos
def cargar_sonidos():
    try:
        sonido_hover = pygame.mixer.Sound("assets/musica/boton.mp3")
        sonido_seleccion = pygame.mixer.Sound("assets/musica/golpe_2.mp3")
        return sonido_hover, sonido_seleccion
    except pygame.error as e:
        print(f"No se pudieron cargar los sonidos: {e}")
        sys.exit()
=======
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
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1

# Cargar el archivo JSON de idiomas
def cargar_idioma(idioma):
    try:
        with open("idioma.json", "r", encoding="utf-8") as file:
            idiomas = json.load(file)
<<<<<<< HEAD
        return idiomas.get(idioma, idiomas.get("es", {}))  # Si no encuentra el idioma, carga el español
=======
        return idiomas.get(idioma, idiomas["es"])  # Si no encuentra el idioma, carga el español
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1
    except json.JSONDecodeError as e:
        print(f"Error en el formato del JSON: {e}")
    except FileNotFoundError as e:
        print(f"No se pudo encontrar el archivo de idiomas: {e}")
    except Exception as e:
        print(f"Error al cargar el archivo de idiomas: {e}")
    return {}

<<<<<<< HEAD
# Cargar imágenes de fondo y opciones
def cargar_imagenes():
    try:
        fondo_menu = pygame.image.load("assets/menu/mar.png")
        fondo_menu = pygame.transform.scale(fondo_menu, (ANCHO_VENTANA, ALTO_VENTANA))  # Escalar la imagen al tamaño de la ventana
        imagen_normal = pygame.image.load("assets/menu/f(2).png")
        imagen_normal = pygame.transform.scale(imagen_normal, (270, 100))  # Escalar a 270x60
        imagen_hover = pygame.image.load("assets/menu/f-hover(2).png")  # Imagen cuando está seleccionada
        imagen_hover = pygame.transform.scale(imagen_hover, (270, 100))
        return fondo_menu, imagen_normal, imagen_hover
    except pygame.error as e:
        print(f"No se pudieron cargar las imágenes: {e}")
        return None, None, None

# Cargar recursos
fuente_texto, fuente_opciones = cargar_fuentes()
sonido_hover, sonido_seleccion = cargar_sonidos()
fondo_menu, imagen_normal, imagen_hover = cargar_imagenes()

=======
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1
# Cargar textos en español por defecto
textos = cargar_idioma("es")  # Inicialmente se carga el idioma español

# Opciones del menú
<<<<<<< HEAD
opciones = [textos.get("español", "Español"), textos.get("ingles", "Inglés"), textos.get("regresar", "Regresar")]
seleccion = 0  # Opción seleccionada inicialmente (por defecto, la opción 0: "Español")
=======
opciones = [textos["español"], textos["ingles"], textos["regresar"]]
seleccion = 0  # Opción seleccionada inicialmente
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1
anterior_seleccion = seleccion  # Para detectar cambios de selección

# Configuración de la ventana
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Pesca-Dos (Idioma)")

<<<<<<< HEAD
# Variables para mover el fondo
fondo_x = 0  # Coordenada X de la posición inicial del fondo
velocidad_fondo = 2  # Velocidad de movimiento del fondo

# Función para dibujar el menú
def dibujar_menu():
    global fondo_x
    
    # Mover el fondo
    fondo_x -= velocidad_fondo
    
    # Si el fondo ha pasado completamente por la ventana, lo colocamos de nuevo
    if fondo_x <= -ANCHO_VENTANA:
        fondo_x = 0
    
    # Dibujar fondo
    if fondo_menu:
        ventana.blit(fondo_menu, (fondo_x, 0))  # Dibujar la imagen de fondo en la posición X
        ventana.blit(fondo_menu, (fondo_x + ANCHO_VENTANA, 0))  # Dibujar el fondo desplazado, para continuar la animación

    # Dibujar título
    titulo_texto = fuente_texto.render(textos.get("idioma", "Idioma"), True, (252, 186, 3))  # Cambiar el color del texto del título
    ventana.blit(titulo_texto, (ANCHO_VENTANA // 2 - titulo_texto.get_width() // 2, 80)) 
=======
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
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1
    
    # Dibujar opciones
    for i, opcion in enumerate(opciones):
        # Coordenadas de las opciones
<<<<<<< HEAD
        x_opcion = ANCHO_VENTANA // 2 - 270 // 2 
        y_opcion = 150 + i * 100  # Ajustar la separación vertical para acercarlo más al título (50px más arriba)

        # Cambiar la imagen según si la opción está seleccionada o no (hover)
        if i == seleccion:
            ventana.blit(imagen_hover, (x_opcion, y_opcion))  # Dibujar la imagen de hover
            texto_opcion = fuente_opciones.render(opcion, True, COLOR_TEXTO_HOVER)  # Cambiar el color del texto a blanco en hover
        else:
            ventana.blit(imagen_normal, (x_opcion, y_opcion))  # Dibujar la imagen predeterminada
            texto_opcion = fuente_opciones.render(opcion, True, COLOR_TEXTO_NORMAL)  # Color del texto predeterminado
        
        # Dibujar la opción en la pantalla centrada
        ventana.blit(texto_opcion, (ANCHO_VENTANA // 2 - texto_opcion.get_width() // 2, y_opcion + 40))  # Ajustar texto sobre la imagen
=======
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
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1

    pygame.display.flip()  # Actualizar pantalla

# Función para detectar si el mouse está sobre una opción
def obtener_opcion_con_mouse(mouse_pos):
    for i, opcion in enumerate(opciones):
<<<<<<< HEAD
        x_opcion = ANCHO_VENTANA // 2 - 270 // 2
        y_opcion = 150 + i * 100
        rect_opcion = pygame.Rect(x_opcion, y_opcion, 270, 60)
=======
        x_opcion = ANCHO_VENTANA // 2 - imagen_ancho // 2
        y_opcion = 200 + i * 80
        rect_opcion = pygame.Rect(x_opcion, y_opcion, imagen_ancho, imagen_alto)
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1
        
        # Comprobar si el mouse está dentro del área del botón
        if rect_opcion.collidepoint(mouse_pos):
            return i
    return None

<<<<<<< HEAD
# Bucle principal con detección de mouse y teclas
=======
# Bucle principal con detección de mouse
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEMOTION:  # Movimiento del mouse
            mouse_pos = event.pos
<<<<<<< HEAD
            nueva_seleccion = obtener_opcion_con_mouse(mouse_pos)  # Cambiar la opción seleccionada según la posición del mouse

            # Reproducir sonido de hover solo si el mouse entra sobre una opción nueva
            if nueva_seleccion != seleccion:
                if nueva_seleccion is not None:
                    pygame.mixer.Sound.play(sonido_hover)
                seleccion = nueva_seleccion
=======
            seleccion = obtener_opcion_con_mouse(mouse_pos)  # Cambiar la opción seleccionada según la posición del mouse
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1

        if event.type == pygame.MOUSEBUTTONDOWN:  # Click del mouse
            if seleccion is not None:
                pygame.mixer.Sound.play(sonido_seleccion)  # Reproducir sonido de selección
                if seleccion == 0:  # Español
                    print("Cambiando a español")
                    textos = cargar_idioma("es")
<<<<<<< HEAD
                    opciones = [textos.get("español", "Español"), textos.get("ingles", "Inglés"), textos.get("regresar", "Regresar")]
                elif seleccion == 1:  # Inglés
                    print("Cambiando a inglés")
                    textos = cargar_idioma("en")
                    opciones = [textos.get("español", "Español"), textos.get("ingles", "Inglés"), textos.get("regresar", "Regresar")]
                elif seleccion == 2:  # Regresar
                    print("Regresando al menú de Opciones")
                    pygame.quit()
                    ejecutar_script('assets/menu/opciones.py')

        if event.type == pygame.KEYDOWN:  # Teclado
            if event.key == pygame.K_DOWN:  # Flecha hacia abajo
                seleccion = (seleccion + 1) % len(opciones)  # Cambiar selección hacia abajo
                pygame.mixer.Sound.play(sonido_hover)
            elif event.key == pygame.K_UP:  # Flecha hacia arriba
                seleccion = (seleccion - 1) % len(opciones)  # Cambiar selección hacia arriba
                pygame.mixer.Sound.play(sonido_hover)
            elif event.key == pygame.K_RETURN:  # Tecla Enter
                pygame.mixer.Sound.play(sonido_seleccion)
                if seleccion == 0:  # Español
                    print("Cambiando a español")
                    textos = cargar_idioma("es")
                    opciones = [textos.get("español", "Español"), textos.get("ingles", "Inglés"), textos.get("regresar", "Regresar")]
                elif seleccion == 1:  # Inglés
                    print("Cambiando a inglés")
                    textos = cargar_idioma("en")
                    opciones = [textos.get("español", "Español"), textos.get("ingles", "Inglés"), textos.get("regresar", "Regresar")]
                elif seleccion == 2:  # Regresar
                    print("Regresando al menú de Opciones")
                    pygame.quit()
                    ejecutar_script('assets/menu/opciones.py')
    dibujar_menu()  # Dibujar menu
=======
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
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1
