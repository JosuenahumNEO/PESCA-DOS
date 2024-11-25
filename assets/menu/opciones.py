import pygame
import sys
import os
import json
<<<<<<< HEAD
import subprocess
=======
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1

# Configuración del sistema
pygame.init()
pygame.mixer.init()

# Leer argumento para el estado de mostrar_video_inicio
mostrar_video_inicio = True
if len(sys.argv) > 1:
    mostrar_video_inicio = bool(int(sys.argv[1]))

# Definir constantes para el menú
ANCHO_VENTANA = 1200
<<<<<<< HEAD
ALTO_VENTANA = 600  # Texto normal en blanco sobre fondo caramelo
=======
ALTO_VENTANA = 600# Texto normal en blanco sobre fondo caramelo
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1
COLOR_TEXTO_NORMAL = (255, 255, 255)  # Blanco
COLOR_TEXTO_HOVER = (255, 223, 129)  # Dorado Claro o Amarillo
FUENTE_TEXTO = pygame.font.Font("assets/fonts/press.ttf", 40)
FUENTE_OPCIONES = pygame.font.Font("assets/fonts/press.ttf", 22)

<<<<<<< HEAD
def ejecutar_script(script):
    subprocess.Popen([sys.executable, script])  # Ejecuta el script en un nuevo proceso
=======
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1
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

# Cambiar el idioma a español por defecto
textos = cargar_idioma("es")

# Crear ventana
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Pesca-Dos (Opciones)")

# Cargar imagen de fondo
try:
    fondo_opciones = pygame.image.load("assets/menu/mar_muelle_nuevo4.png")
    fondo_opciones = pygame.transform.scale(fondo_opciones, (ANCHO_VENTANA, ALTO_VENTANA))
except pygame.error as e:
    print(f"No se pudo cargar la imagen de fondo: {e}")
    fondo_opciones = None

# Cargar imágenes de botones (normal y hover)
imagenes_boton = {}
for i, opcion in enumerate(textos.values()):  # Suponiendo que el número de opciones es igual a la cantidad de imágenes
    imagen_normal = pygame.image.load(f"assets/menu/f(2).png")
    imagen_hover = pygame.image.load(f"assets/menu/f-hover(2).png")

    # Redimensionar las imágenes detrás de los botones
    imagen_normal = pygame.transform.scale(imagen_normal, (280, 100))  # Escalar a 200x50 píxeles
    imagen_hover = pygame.transform.scale(imagen_hover, (280, 98))    # Escalar a 200x50 píxeles

    imagenes_boton[i] = {"normal": imagen_normal, "hover": imagen_hover}

# Cargar animaciones del gato
animaciones = []
for i in range(2):
    try:
        # Asegúrate de que las rutas de las imágenes son correctas
        img = pygame.image.load(f"assets/personajes/naranjo/cat_{i}.png")
        img = pygame.transform.scale(img, (160, 160))  # Escalar a 160x160
        animaciones.append(img)
    except pygame.error as e:
        print(f"No se pudo cargar la imagen: {e}")
        animaciones = []  # Aseguramos que animaciones esté vacío si hay un error
        break

# Verificar que animaciones tenga contenido antes de usarla
if not animaciones:
    print("Error: Las imágenes del gato no se cargaron correctamente.")
    sys.exit()  # Salir si no se pudo cargar las imágenes

# Opciones del menú (Las opciones ahora son dinámicas según el idioma)
opciones = [textos["idioma"], textos["historia"], textos["controles"], textos["regresar"]]

# Inicializar la variable seleccion con un valor válido
seleccion = 0  # Se asegura que 'seleccion' tenga un valor inicial válido

# Variables para el movimiento del fondo y el gato
posicion_fondo_x = -20
velocidad_fondo = 0.2
posicion_gato_x = 500  # Posición inicial del gato
frame_gato = 1  # Para controlar el frame de la animación
direccion_gato = -1  # -1 para izquierda, 1 para derecha

def dibujar_menu():
    global seleccion  # Aseguramos que seleccion es global
<<<<<<< HEAD

=======
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1
    # Dibujar fondo
    if fondo_opciones:
        ventana.blit(fondo_opciones, (posicion_fondo_x, 0))
        ventana.blit(fondo_opciones, (posicion_fondo_x + ANCHO_VENTANA, 0))

<<<<<<< HEAD
    # Dibujar gato **ANTES** de las opciones, para que esté detrás de las imágenes de los botones
    gato_actual = animaciones[frame_gato]
    if direccion_gato == 1:  # Si va hacia la derecha, invertir imagen
        gato_actual = pygame.transform.flip(gato_actual, True, False)
        
    ventana.blit(gato_actual, (posicion_gato_x, 430))

=======
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1
    # Dibujar título
    titulo_texto = FUENTE_TEXTO.render(textos["opciones"], True, (252, 186, 3))
    ventana.blit(titulo_texto, (ANCHO_VENTANA // 2 - titulo_texto.get_width() // 2, 100))
    
    # Dibujar opciones
    for i, opcion in enumerate(opciones):
        x_opcion = ANCHO_VENTANA // 2 - 100
<<<<<<< HEAD
        y_opcion = 200 + i * 90

        # Detectar si el ratón está sobre la opción
=======
        y_opcion = 250 + i * 90

        # Detectar si el ratón está sobre la opción
        #este codigo en teoria no deberia de funcionar pero lo hace
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if x_opcion <= mouse_x <= x_opcion + 200 and y_opcion + 15 <= mouse_y <= y_opcion + 55:
            imagen_boton = imagenes_boton[i]["hover"]  # Cambiar a hover
            if seleccion != i:
                seleccion = i
                pygame.mixer.Sound.play(sonido_hover)
        else:
            imagen_boton = imagenes_boton[i]["normal"]  # Mostrar imagen normal

        # Si el botón está seleccionado con el teclado, también mostrar la imagen hover
        if seleccion == i:
            imagen_boton = imagenes_boton[i]["hover"]

        # Mostrar la imagen del botón detrás del texto
        ventana.blit(imagen_boton, (x_opcion - 40, y_opcion - 20))

        # Dibujar texto sobre la imagen
        if i == seleccion:
            texto_opcion = FUENTE_OPCIONES.render(opcion, True, COLOR_TEXTO_HOVER)
        else:
            texto_opcion = FUENTE_OPCIONES.render(opcion, True, COLOR_TEXTO_NORMAL)

        ventana.blit(texto_opcion, (ANCHO_VENTANA // 2 - texto_opcion.get_width() // 2, y_opcion + 15))

<<<<<<< HEAD
    pygame.display.flip()  # Actualizar pantalla
=======
    # Dibujar gato
    gato_actual = animaciones[frame_gato]
    if direccion_gato == 1:  # Si va hacia la derecha, invertir imagen
        gato_actual = pygame.transform.flip(gato_actual, True, False)
        
    ventana.blit(gato_actual, (posicion_gato_x, 430))

    pygame.display.flip()  # Actualizar pantalla

>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1
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
                if seleccion == 0:  # Cambiar idioma
                    print("Abriendo menú de idioma")
                    pygame.quit()
<<<<<<< HEAD
                    ejecutar_script('assets/menu/idioma.py')
                elif seleccion == 1:  # Historia
                    print("Abriendo historia...")
                    pygame.quit()
                    ejecutar_script('assets/menu/cinematica/definitivacine.py')
                elif seleccion == 2:  # Controles
                    print("Abriendo controles...")
                    pygame.quit()
                    ejecutar_script('assets/menu/controles.py')
=======
                    os.system('python assets/menu/idioma.py')
                elif seleccion == 1:  # Historia
                    print("Abriendo historia...")
                    pygame.quit()
                    os.system('python assets/menu/cinematica/definitivacine.py')
                elif seleccion == 2:  # Controles
                    print("Abriendo controles...")
                    pygame.quit()
                    os.system('python assets/menu/controles.py')
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1
                elif seleccion == 3:  # Regresar
                    print("Regresando al menú principal...")
                    pygame.quit()

        # Detectar clic del mouse
<<<<<<< HEAD
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = event.pos
            for i, opcion in enumerate(opciones):
                x_opcion = ANCHO_VENTANA // 2 - 100
                y_opcion = 200 + i * 90  # Asegúrate de que coincida con la posición de los botones
=======
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Botón izquierdo del mouse
            mouse_x, mouse_y = event.pos
            for i, opcion in enumerate(opciones):
                x_opcion = ANCHO_VENTANA // 2 - 100
                y_opcion = 250 + i * 80
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1
                if x_opcion <= mouse_x <= x_opcion + 200 and y_opcion + 15 <= mouse_y <= y_opcion + 55:
                    seleccion = i
                    pygame.mixer.Sound.play(sonido_seleccion)
                    # Manejo de opciones
                    if seleccion == 0:
                        print("Abriendo menú de idioma")
                        pygame.quit()
<<<<<<< HEAD
                        ejecutar_script('assets/menu/idioma.py')
                    elif seleccion == 1:
                        print("Abriendo historia...")
                        pygame.quit()
                        ejecutar_script('assets/menu/cinematica/definitivacine.py')
                    elif seleccion == 2:
                        print("Abriendo controles...")  
                        pygame.quit()                    
                        ejecutar_script('assets/menu/controles.py')
                    elif seleccion == 3:  # Regresar
                        print("Regresando al menú principal...")
                        pygame.mixer.Sound.play(sonido_seleccion)
=======
                        os.system('python assets/menu/idioma1.py')
                    elif seleccion == 1:
                        print("Abriendo historia...")
                        pygame.quit()
                        os.system('python assets/menu/cinematica/definitivacine.py')
                    elif seleccion == 2:
                        print("Abriendo controles...")
                        pygame.quit()
                        os.system('python assets/menu/controles.py')
                    elif seleccion == 3:  # Regresar
                        print("Regresando al menú principal...")
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1
                        pygame.quit()

    # Actualizar posición del fondo
    posicion_fondo_x -= velocidad_fondo
    if posicion_fondo_x <= -ANCHO_VENTANA - 20:
        posicion_fondo_x = -20

    # Actualizar animación del gato
    frame_gato = (frame_gato + 1) % len(animaciones)

    # Controlar la posición del gato
<<<<<<< HEAD
    posicion_gato_x += direccion_gato * 3
    if posicion_gato_x < -800:
        direccion_gato = 1
    elif posicion_gato_x > ANCHO_VENTANA:
        posicion_gato_x = -160
        direccion_gato = -1
=======
    posicion_gato_x += direccion_gato * 3  # Mover el gato en la dirección actual
    if posicion_gato_x < -800:  # Cambiar dirección al llegar a -800
        direccion_gato = 1  # Cambiar a ir a la derecha
    elif posicion_gato_x > ANCHO_VENTANA:  # Reiniciar posición si se sale por la derecha
        posicion_gato_x = -160  # Reiniciar posición fuera de la pantalla a la izquierda
        direccion_gato = -1  # Cambiar a ir a la izquierda
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1

    dibujar_menu()  # Dibujar el menú

pygame.quit()
