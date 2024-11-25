import pygame
<<<<<<< HEAD
from personajes import Personaje
=======

>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1
ALTO_VENTANA = 600  # variable para definir alto de la pantalla
ANCHO_VENTANA = 1200  # lo mismo pero ahora el ancho
ALTO_PERSONAJE = 120
ANCHO_PERSONAJE = 120
COLOR_PERSONAJE = (252, 227, 3)
COLOR_BG = (0, 0, 20)  # BG = BACKGROUND (fondo)
<<<<<<< HEAD



IMG_BACKGROUND_PRINCIPIANTE1 = pygame.image.load("assets/niveles/principiante/nivel1/fondocompleto1.jpeg")
IMG_BACKGROUND_PRINCIPIANTE =  Personaje.escalar_img(IMG_BACKGROUND_PRINCIPIANTE1, 1200, 600)

IMG_BACKGROUND_INTERMEDIO1 = pygame.image.load("assets/niveles/intermedio/nivel1/fondocompleto.png")
IMG_BACKGROUND_INTERMEDIO =  Personaje.escalar_img(IMG_BACKGROUND_INTERMEDIO1, 1200, 600)

IMG_BACKGROUND_AVANZADO1 = pygame.image.load("assets/niveles/avanzado/nivel1/fondocompleto.png")
IMG_BACKGROUND_AVANZADO =  Personaje.escalar_img(IMG_BACKGROUND_AVANZADO1, 1200, 600)




=======
IMG_BACKGROUND = pygame.image.load("assets/niveles/principiante/nivel1/fondocompleto.png")
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1
FPS = 60
VELOCIDAD = 7
ESCALA_PERSONAJE = 1.3
MUSICA_FONDO = "assets/musica/fondo_menu.mp3"

# Constantes de nivel1.py movidas aquí
GATO_MIRANDO_AL_RIO = "assets/personajes/naranjo/frente7.png"
IMAGEN_PAUSA = "assets/menu/pausa.png"
IMAGEN_FIN = "assets/items/carta.jpeg"
IMAGEN_FLOTANTE = "assets/items/basura/manzana_mordida.png"
FILAS = 4
VELOCIDAD_FLOTANTE = 2
FONDO_DE_TEXTO = "assets/menu/fondo_de_texto.png"
<<<<<<< HEAD

print("Funciona")
=======
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1
