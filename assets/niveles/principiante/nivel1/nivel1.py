import pygame
import sys
import os
import random
<<<<<<< HEAD
import subprocess
=======
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1

# Configuración del sistema
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../")))  # para saltar carpetas hacia arriba
import constantes
from personajes import Personaje

pygame.init()
pygame.mixer.init()
<<<<<<< HEAD
def manejar_sonido_victoria(contador_puntos):
    global sonido_victoria_reproducido  # Aseguramos que usamos la variable global

    if contador_puntos >= 4 and not sonido_victoria_reproducido:
        pygame.mixer.Sound.stop(sonido_fondo)  # Detener la música de fondo
        pygame.mixer.Sound.play(pygame.mixer.Sound("assets/musica/win_sound.mp3"))  # Reproducir el sonido de victoria
        sonido_victoria_reproducido = True  # Marcar que el sonido se ha reproducido

def ejecutar_script(script):
    subprocess.Popen([sys.executable, script])  # Ejecuta el script en un nuevo proceso
=======
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1

# Cargar imágenes y sonidos
animaciones = []
for i in range(2):
    try:
        img = pygame.image.load(f"assets/personajes/naranjo/cat_{i}.png")
        img = Personaje.escalar_img(img, 120, 120)  # Llamamos a la función "escalar_img" de personajes.py
        animaciones.append(img)
    except pygame.error as e:
        print(f"No se pudo cargar la imagen: {e}")

ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))  # Define el alto y ancho de la ventana
pygame.display.set_caption("PESCA-DOS (Principiante-Nivel 1)")  # Título del juego

# Cargar imágenes para los botones de pausa y música
imagen_play = pygame.image.load("assets/menu/play.png")
imagen_pause = pygame.image.load("assets/menu/pause.png")
imagen_audio = pygame.image.load("assets/menu/audio.png")
imagen_noaudio = pygame.image.load("assets/menu/noaudio.png")

# Escalamos las imágenes
tamaño_boton = 70
imagen_play = Personaje.escalar_img(imagen_play, tamaño_boton, tamaño_boton)
imagen_pause = Personaje.escalar_img(imagen_pause, tamaño_boton, tamaño_boton)
imagen_audio = Personaje.escalar_img(imagen_audio, tamaño_boton, tamaño_boton)
imagen_noaudio = Personaje.escalar_img(imagen_noaudio, tamaño_boton, tamaño_boton)

# Inicialmente, mostrar las imágenes "play" y "audio"
imagen_boton_pausa = imagen_play
imagen_boton_musica = imagen_audio

# Cargar imágenes adicionales
gato_mirando_al_rio = pygame.image.load(constantes.GATO_MIRANDO_AL_RIO)
gato_mirando_al_rio = Personaje.escalar_img(gato_mirando_al_rio, 120, 120)

<<<<<<< HEAD
sonido_golpe = pygame.mixer.Sound("assets/musica/boton.mp3")  # Sonido al golpear un objeto

# Lista de imágenes basura
imagenes_basura = [
    pygame.image.load("assets/items/basura/bolsa.png"),
    pygame.image.load("assets/items/basura/hojas.png"),
    pygame.image.load("assets/items/basura/llanta.png"),
=======
sonido_golpe = pygame.mixer.Sound("assets/musica/golpe_1.mp3")  # Sonido al golpear un objeto

# Lista de imágenes basura
imagenes_basura = [
    pygame.image.load("assets/items/basura/botella_vidrio.png"),
    pygame.image.load("assets/items/basura/lata_atun.png"),
    pygame.image.load("assets/items/basura/lata_aplastada.png"),
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1
    pygame.image.load("assets/items/basura/manzana_mordida.png"),
    pygame.image.load("assets/items/basura/botella_plastico_aplastada.png")
]

# Tamaño general de las imágenes de la basura
<<<<<<< HEAD
imagenes_basura = [Personaje.escalar_img(img, 70, 60) for img in imagenes_basura]

#imagen_contador_basuras = pygame.image.load("assets/items/basura/lata_aplastada.png")
#imagen_contador_basuras = Personaje.escalar_img(imagen_contador_basuras, 20, 20)

#imagen_contador_anzuelos = pygame.image.load("assets/items/anzuelo.png")
#imagen_contador_anzuelos = Personaje.escalar_img(imagen_contador_anzuelos, 30, 30)

# Variables del juego
posiciones_flotantes = [random.randint(50, constantes.ANCHO_VENTANA - 100) for _ in range(17)]
direcciones_flotantes = [2] * 17  # si se aumenta este parámetro las basuras van más rápido
velocidad_flotante = constantes.VELOCIDAD_FLOTANTE
alturas_flotantes = [310 + i * 40 for i in range(17)]

# Asignar imágenes aleatorias a cada objeto flotante
imagenes_flotantes = [random.choice(imagenes_basura) for _ in range(17)]

jugador = Personaje(500, 550, animaciones)#posicion inicial
=======
imagenes_basura = [Personaje.escalar_img(img, 90, 80) for img in imagenes_basura]

imagen_contador_basuras = pygame.image.load("assets/items/basura/lata_aplastada.png")
imagen_contador_basuras = Personaje.escalar_img(imagen_contador_basuras, 50, 50)

imagen_contador_anzuelos = pygame.image.load("assets/items/anzuelo.png")
imagen_contador_anzuelos = Personaje.escalar_img(imagen_contador_anzuelos, 50, 50)

# Variables del juego
posiciones_flotantes = [random.randint(50, constantes.ANCHO_VENTANA - 100) for _ in range(constantes.FILAS)]
direcciones_flotantes = [2] * constantes.FILAS  # si se aumenta este parámetro las basuras van más rápido
velocidad_flotante = constantes.VELOCIDAD_FLOTANTE
alturas_flotantes = [180 + i * 60 for i in range(constantes.FILAS)]

# Asignar imágenes aleatorias a cada objeto flotante
imagenes_flotantes = [random.choice(imagenes_basura) for _ in range(constantes.FILAS)]

jugador = Personaje(500, 500, animaciones)
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1

mover_izquierda = False
mover_derecha = False

juego_en_pausa = False
musica_muted = False
fuente = pygame.font.Font("assets/fonts/press.ttf", 36)

# Variables para la lata
anzuelo_posicion = [0, 0]
anzuelo_lanzado = False
anzuelo_velocidad = 5

<<<<<<< HEAD
FILAS=4

contador_puntos = 0  # Contador inicial del juego
nivel_completado = False  # Controla si el nivel ha sido completado
anzuelos_disponibles = 15  # Contador de anzuelos

reloj = pygame.time.Clock()
tiempo = 29  # Tiempo inicial del reloj
=======
contador_puntos = 0  # Contador inicial del juego
nivel_completado = False  # Controla si el nivel ha sido completado
anzulos_disponibles = 10  # Contador de anzuelos

reloj = pygame.time.Clock()
tiempo = 60  # Tiempo inicial del reloj
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1

pygame.mixer.stop()
sonido_fondo = pygame.mixer.Sound(constantes.MUSICA_FONDO)  # Música de fondo
pygame.mixer.Sound.play(sonido_fondo, -1)  # Reproducir música en bucle

# Cargar sonido de "select_level1.mp3"
sonido_select = pygame.mixer.Sound("assets/musica/unpause.mp3")

# Botones rectangulares
boton_musica_rect = pygame.Rect(10, 110, 50, 50)  # Tamaño del botón de música
boton_pausa_rect = pygame.Rect(10, 50, 50, 50)  # Tamaño del botón para pausar el juego
<<<<<<< HEAD
#                                                                                                                                                         botones rect de fin de nivel
 #                                                                                                           1___________________________________________ nivel completado
# Crear el botón "Regresar"
boton_regresar = pygame.image.load("assets/menu/regresar.png")  # Imagen para el botón de regresar
boton_regresar = Personaje.escalar_img(boton_regresar, 300, 150)
boton_regresar_rect = boton_regresar.get_rect(topleft=(850,325))

# Crear el botón "Siguiente nivel"
boton_siguiente = pygame.image.load("assets/menu/siguiente.png")  # Imagen para el botón de siguiente nivel
boton_siguiente = Personaje.escalar_img(boton_siguiente, 300, 150)
boton_siguiente_rect = boton_siguiente.get_rect(topleft=(850,450))

#                                                                                                            2___________________________________________sin anzuelos
                                                                                                            
                                                                                                            

                                                    # Crear el botón "Regresar"
boton_regresar2 = pygame.image.load("assets/menu/regresar.png")  # Imagen para el botón de regresar                 regresar
boton_regresar2 = Personaje.escalar_img(boton_regresar2, 300, 150)
boton_regresar_rect2 = boton_regresar2.get_rect(topleft=(550,450))

# Crear el botón "Siguiente nivel"
boton_siguiente2 = pygame.image.load("assets/menu/siguiente.png")  # Imagen para el botón de siguiente nivel        reintentar
boton_siguiente2 = Personaje.escalar_img(boton_siguiente2, 300, 150)
boton_siguiente_rect2 = boton_siguiente2.get_rect(topleft=(850,450))                                                        
                                                                                                            
                                                                                                            
                                                                                                            
                                                                                                            
#                                                                                                            3___________________________________________sin tiempo




# Crear el botón "Regresar"
boton_regresar3 = pygame.image.load("assets/menu/regresar.png")  #                                              regresar
boton_regresar3 = Personaje.escalar_img(boton_regresar3, 300, 150)
boton_regresar_rect3 = boton_regresar3.get_rect(topleft=(750,325))

# Crear el botón "Siguiente nivel"
boton_siguiente3 = pygame.image.load("assets/menu/repetir.png")  #                                              reintentar
boton_siguiente3 = Personaje.escalar_img(boton_siguiente3, 300, 150)
boton_siguiente_rect3 = boton_siguiente3.get_rect(topleft=(850,450))








=======


# Crear el botón "Regresar"
boton_regresar = pygame.image.load("assets/menu/regresar.jpg")  # Imagen para el botón de regresar
boton_regresar = Personaje.escalar_img(boton_regresar, 200, 100)
boton_regresar_rect = boton_regresar.get_rect(center=(constantes.ANCHO_VENTANA // 2, constantes.ALTO_VENTANA // 2 + 100))

# Crear el botón "Siguiente nivel"
boton_siguiente = pygame.image.load("assets/menu/siguiente.jpg")  # Imagen para el botón de siguiente nivel
boton_siguiente = Personaje.escalar_img(boton_siguiente, 200, 100)
boton_siguiente_rect = boton_siguiente.get_rect(center=(constantes.ANCHO_VENTANA // 2, constantes.ALTO_VENTANA // 2 + 200))
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1

# Cargar las imágenes de fin de juego (ajustadas a 600x1200)
imagen_gameover_tiempo = pygame.image.load("assets/menu/seacaboeltiempo.png")
imagen_gameover_anzuelos = pygame.image.load("assets/menu/sinanzuelos.png")
imagen_nivel_completado = pygame.image.load("assets/menu/nivelcompletado.png")

# Escalar las imágenes a 600x1200
imagen_gameover_tiempo = Personaje.escalar_img(imagen_gameover_tiempo, 1200, 600)
imagen_gameover_anzuelos = Personaje.escalar_img(imagen_gameover_anzuelos, 1200, 600)
imagen_nivel_completado = Personaje.escalar_img(imagen_nivel_completado, 1200, 600)

<<<<<<< HEAD
imagen_tiempo = pygame.image.load("assets/menu/tiempo.png")  # Imagen del anzuelo 
imagen_tiempo = Personaje.escalar_img(imagen_tiempo, 300, 120)  # Escalar imagen

imagen_anzuelos = pygame.image.load("assets/menu/anzuelos.png")  # Imagen del anzuelo 
imagen_anzuelos = Personaje.escalar_img(imagen_anzuelos, 300, 120)  # Escalar imagen

imagen_basura = pygame.image.load("assets/menu/basura.png")  # Imagen del anzuelo 
imagen_basura = Personaje.escalar_img(imagen_basura, 300, 120)  # Escalar imagen
#                                                                                                                                      imagenes de los botones
#  imágenes de los botones con el efecto hover                                      #       1 _______________________________________ nivel completado
imagen_regresar_hover= pygame.image.load("assets/menu/regresar-hover.png")
imagen_siguiente_hover = pygame.image.load("assets/menu/siguiente-hover.png")
imagen_regresar = pygame.image.load("assets/menu/regresar.png")
imagen_siguiente = pygame.image.load("assets/menu/siguiente.png")
# Escalar las imágenes
imagen_regresar = Personaje.escalar_img(imagen_regresar, 300, 150)
imagen_siguiente = Personaje.escalar_img(imagen_siguiente, 300, 150)
imagen_regresar_hover = Personaje.escalar_img(imagen_regresar_hover, 300, 150)
imagen_siguiente_hover = Personaje.escalar_img(imagen_siguiente_hover, 300, 150)

#  imágenes de los botones con el efecto hover                                      #       2 _________________________________________sin anzuelos
imagen_regresar_hover2= pygame.image.load("assets/menu/regresar-hover.png")
imagen_siguiente_hover2 = pygame.image.load("assets/menu/repetir-hover.png")
imagen_regresar2 = pygame.image.load("assets/menu/regresar.png")
imagen_siguiente2 = pygame.image.load("assets/menu/repetir.png")
# Escalar las imágenes
imagen_regresar2 = Personaje.escalar_img(imagen_regresar2, 270, 120)
imagen_siguiente2 = Personaje.escalar_img(imagen_siguiente2, 270, 120)
imagen_regresar_hover2 = Personaje.escalar_img(imagen_regresar_hover2, 270, 120)
imagen_siguiente_hover2 = Personaje.escalar_img(imagen_siguiente_hover2, 270, 120)

#  imágenes de los botones con el efecto hover                                      #       3 _________________________________________sin tiempo
imagen_regresar_hover3= pygame.image.load("assets/menu/regresar-hover.png")
imagen_regresar3 = pygame.image.load("assets/menu/regresar.png")
imagen_siguiente_hover3= pygame.image.load("assets/menu/repetir-hover.png")
imagen_siguiente3 = pygame.image.load("assets/menu/repetir.png")

# Escalar las imágenes
imagen_regresar3 = Personaje.escalar_img(imagen_regresar3, 300, 150)
imagen_regresar_hover3 = Personaje.escalar_img(imagen_regresar_hover3, 300, 150)
imagen_siguiente3 = Personaje.escalar_img(imagen_siguiente3, 300, 150)
imagen_siguiente_hover3 = Personaje.escalar_img(imagen_siguiente_hover3, 300, 150)


sonido_victoria_reproducido = False

=======
imagen_tiempo = pygame.image.load("assets/menu/f(2).png")  # Imagen del anzuelo 
imagen_tiempo = Personaje.escalar_img(imagen_tiempo, 550, 150)  # Escalar imagen
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1

##################  BUCLE PRINCIPAL  ##################
run = True
while run:
    reloj.tick(constantes.FPS)  # Controlar FPS
    if not juego_en_pausa and tiempo > 0:  # Si no está en pausa y el tiempo es mayor que 0
        tiempo -= 1 / constantes.FPS  # Decrementar tiempo de 1 en 1

<<<<<<< HEAD
    ventana.blit(constantes.IMG_BACKGROUND_PRINCIPIANTE, (0, 0))  

    ventana.blit(imagen_tiempo, (-25, 0))  # coordenada donde se coloca la imagen detrás del tiempo    
    ventana.blit(imagen_anzuelos, (920, -10))  # coordenada donde se coloca la imagen detrás dell contador de anzuelos
    ventana.blit(imagen_basura, (920, 90))  # coordenada donde se coloca la imagen detrás dell contador de anzuelos
     
    boton_musica_rect = pygame.Rect(10, 170, tamaño_boton, tamaño_boton)  # Tamaño dinámico del botón de música
    boton_pausa_rect = pygame.Rect(10, 100, tamaño_boton, tamaño_boton)  # Tamaño dinámico del botón para pausar el juego
    
    #ventana.blit(imagen_contador_basuras, (830, 0))  # coordenada donde se coloca la imagen detrás del tiempo
    #ventana.blit(imagen_contador_anzuelos, (980, 50))  # coordenada donde se coloca la imagen detrás del tiempo
=======
    ventana.blit(constantes.IMG_BACKGROUND, (0, 0))  

    ventana.blit(imagen_tiempo, (-70, -45))  # coordenada donde se coloca la imagen detrás del tiempo
    
    boton_musica_rect = pygame.Rect(10, 170, tamaño_boton, tamaño_boton)  # Tamaño dinámico del botón de música
    boton_pausa_rect = pygame.Rect(10, 90, tamaño_boton, tamaño_boton)  # Tamaño dinámico del botón para pausar el juego
    
    ventana.blit(imagen_contador_basuras, (870, 0))  # coordenada donde se coloca la imagen detrás del tiempo
    ventana.blit(imagen_contador_anzuelos, (980, 50))  # coordenada donde se coloca la imagen detrás del tiempo
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1
    # Mostrar los botones de pausa y música en la pantalla
    ventana.blit(imagen_boton_pausa, boton_pausa_rect.topleft)  # Dibujar botón de pausa
    ventana.blit(imagen_boton_musica, boton_musica_rect.topleft)  # Dibujar botón de música

    delta_x = 0  # Inicializa movimiento

    # Controlar el movimiento del jugador
    if mover_derecha and not juego_en_pausa and tiempo > 0 and not nivel_completado:
        delta_x = constantes.VELOCIDAD
    if mover_izquierda and not juego_en_pausa and tiempo > 0 and not nivel_completado:
        delta_x = -constantes.VELOCIDAD

    if (jugador.forma.x + delta_x > 0 and 
        jugador.forma.x + delta_x < constantes.ANCHO_VENTANA - jugador.forma.width):
        jugador.movimiento(delta_x, 0)

    # Mostrar el gato mirando al río si no hay movimiento
    if not mover_izquierda and not mover_derecha:
        ventana.blit(gato_mirando_al_rio, jugador.forma.topleft)
    else:
        jugador.dibujar(ventana)

    # Escribir tiempo, puntos y anzuelos
<<<<<<< HEAD
    texto_tiempo = fuente.render(f'{int(tiempo)}', True, (0, 0, 0))
    ventana.blit(texto_tiempo, (130, 40))  # posición en la pantalla
 
    # Mostrar los puntos y anzuelos
    texto_puntos = fuente.render(f'{contador_puntos}/4', True, (0, 0, 0))
    ventana.blit(texto_puntos, (constantes.ANCHO_VENTANA - texto_puntos.get_width() - 115, 27))  # posición en la pantallla

    texto_anzuelos = fuente.render(f'{anzuelos_disponibles}', True, (0, 0, 0))
    ventana.blit(texto_anzuelos, (constantes.ANCHO_VENTANA - texto_anzuelos.get_width() - 130, 125))  

    # Mover y dibujar objetos flotantes
    flotantes_activos = False
    for i in range(FILAS):
=======
    texto_tiempo = fuente.render(f'Tiempo: {int(tiempo)}', True, (0, 0, 0))
    ventana.blit(texto_tiempo, (10, 10))  # posición en la pantalla

    # Mostrar los puntos y anzuelos
    texto_puntos = fuente.render(f': {contador_puntos} / 4', True, (255, 0, 0))
    ventana.blit(texto_puntos, (constantes.ANCHO_VENTANA - texto_puntos.get_width() - 10, 10))  # posición en la pantallla

    texto_anzuelos = fuente.render(f': {anzulos_disponibles}', True, (255, 0, 0))
    ventana.blit(texto_anzuelos, (constantes.ANCHO_VENTANA - texto_anzuelos.get_width() - 10, 50))  

    # Mover y dibujar objetos flotantes
    flotantes_activos = False
    for i in range(constantes.FILAS):
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1
        x = posiciones_flotantes[i]
        y = alturas_flotantes[i]
        if nivel_completado:  # Si el nivel ha sido completado, no mover objetos flotantes
            continue
        if imagenes_flotantes[i] is not None:  # Solo dibujar imágenes que no sean None
            ventana.blit(imagenes_flotantes[i], (x, y))  # Dibujar imagen flotante
            x += velocidad_flotante * direcciones_flotantes[i]
            if x >= constantes.ANCHO_VENTANA - imagenes_flotantes[i].get_width() or x <= 0:
                direcciones_flotantes[i] *= -1
            posiciones_flotantes[i] = x
            flotantes_activos = True

    # Mostrar el anzuelo si ha sido lanzado
    if anzuelo_lanzado:
        imagenAnzuelos = pygame.image.load("assets/items/anzuelo.png")  # Imagen del anzuelo
        imagenAnzuelos = Personaje.escalar_img(imagenAnzuelos, 50, 50)  # Escalar imagen
        anzuelo_posicion[1] -= anzuelo_velocidad  # Mover la lata hacia arriba
        lanzar_anzuelo = ventana.blit(imagenAnzuelos, (anzuelo_posicion[0], anzuelo_posicion[1]))  # Mostrar anzuelo

        # Comprobar colisiones con los objetos flotantes
<<<<<<< HEAD
        for i in range(17):
=======
        for i in range(constantes.FILAS):
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1
            if imagenes_flotantes[i] is not None:  # Solo proceder si la imagen no es None
                if (posiciones_flotantes[i] < anzuelo_posicion[0] < posiciones_flotantes[i] + imagenes_flotantes[i].get_width() and
                    alturas_flotantes[i] < anzuelo_posicion[1] < alturas_flotantes[i] + imagenes_flotantes[i].get_height()):
                    sonido_golpe.play()  # Reproducir sonido de golpe
<<<<<<< HEAD
                    anzuelo_posicion = [jugador.forma.x + 35, jugador.forma.y -1000]  # Resetear posición el "-1000" teletransporta el anzuelo a 1000 px arrirba de la pantalla, pero no se elimina jaja 
                    if anzuelo_posicion:
                        print("¡Basura pescada! :D")
                    
                    contador_puntos += 1  # Aumentar contador de puntos
                    imagenes_flotantes[i] = None # Cambiar imagen de basura a None
                    
    # Mostrar mensaje de fin de juego si se completa el nivel
    if contador_puntos >= 4:
        nivel_completado = True
        
        manejar_sonido_victoria(contador_puntos)
    # Mostrar el mensaje final si el tiempo llega a 0, los anzuelos se acaban o el nivel se completa
    # Mostrar mensaje de fin de juego si el tiempo llega a 0, los anzuelos se acaban o el nivel se completa
    if tiempo <= 0 and not nivel_completado:  # Solo si el nivel no está completado                                               sin timepo      3
        ventana.blit(imagen_gameover_tiempo, (constantes.ANCHO_VENTANA // 2 - imagen_gameover_tiempo.get_width() // 2,
                                            constantes.ALTO_VENTANA // 2 - imagen_gameover_tiempo.get_height() // 2))

        # Mostrar los botones "Regresar" y "Siguiente nivel"
        ventana.blit(boton_regresar3, boton_regresar_rect3.topleft)
        ventana.blit(boton_siguiente3, boton_siguiente_rect3.topleft)

        if boton_regresar_rect3.collidepoint(pygame.mouse.get_pos()):
            ventana.blit(imagen_regresar_hover3, boton_regresar_rect3.topleft)  # Mostrar imagen con hover
        else:
            ventana.blit(imagen_regresar3, boton_regresar_rect3.topleft)  # Mostrar imagen normal

    
    
    
    elif anzuelos_disponibles <= 0:                                                                                               # sin anzuelos    2
        ventana.blit(imagen_gameover_anzuelos, (constantes.ANCHO_VENTANA // 2 - imagen_gameover_anzuelos.get_width() // 2,
                                            constantes.ALTO_VENTANA // 2 - imagen_gameover_anzuelos.get_height() // 2))
        
        
        

        # Mostrar el botón "Regresar"
        if boton_regresar_rect2.collidepoint(pygame.mouse.get_pos()):
            ventana.blit(imagen_regresar_hover2, (boton_regresar_rect2.x, boton_regresar_rect2.y + y))  # Mostrar imagen con hover
        else:
            ventana.blit(imagen_regresar2, (boton_regresar_rect2.x, boton_regresar_rect2.y + y))  # Mostrar imagen normal

        # Mostrar el botón "repetir"
        if boton_siguiente_rect2.collidepoint(pygame.mouse.get_pos()):
            ventana.blit(imagen_siguiente_hover2, (boton_siguiente_rect2.x, boton_siguiente_rect2.y + y))  # Mostrar imagen con hover
        else:
            ventana.blit(imagen_siguiente2, (boton_siguiente_rect2.x, boton_siguiente_rect2.y + y))  # Mostrar imagen normal

        
        

    elif contador_puntos >= 4:                                                                                                  #nivel completado    1
=======
                    anzuelo_posicion = [jugador.forma.x + 35, jugador.forma.y - 20]  # Resetear posición
                    contador_puntos += 1  # Aumentar contador de puntos
                    imagenes_flotantes[i] = None  # Cambiar imagen de basura a None

    # Mostrar mensaje de fin de juego si se completa el nivel
    if contador_puntos >= 4:
        nivel_completado = True
        pygame.mixer.Sound.stop(sonido_fondo)  # Detener música principal
        pygame.mixer.Sound.play(pygame.mixer.Sound("assets/musica/win_sound.mp3"))  # Reproducir sonido de victoria

    # Mostrar el mensaje final si el tiempo llega a 0, los anzuelos se acaban o el nivel se completa
    if tiempo <= 0:
        ventana.blit(imagen_gameover_tiempo, (constantes.ANCHO_VENTANA // 2 - imagen_gameover_tiempo.get_width() // 2,
                                             constantes.ALTO_VENTANA // 2 - imagen_gameover_tiempo.get_height() // 2))

    elif anzulos_disponibles <= 0:
        ventana.blit(imagen_gameover_anzuelos, (constantes.ANCHO_VENTANA // 2 - imagen_gameover_anzuelos.get_width() // 2,
                                               constantes.ALTO_VENTANA // 2 - imagen_gameover_anzuelos.get_height() // 2))

    elif contador_puntos >= 4:
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1
        ventana.blit(imagen_nivel_completado, (constantes.ANCHO_VENTANA // 2 - imagen_nivel_completado.get_width() // 2,
                                              constantes.ALTO_VENTANA // 2 - imagen_nivel_completado.get_height() // 2))

        # Mostrar los botones "Regresar" y "Siguiente nivel"
        ventana.blit(boton_regresar, boton_regresar_rect.topleft)
<<<<<<< HEAD
        # Mostrar los puntos y anzuelos
        ventana.blit(boton_siguiente, boton_siguiente_rect.topleft)
        
        if boton_regresar_rect.collidepoint(pygame.mouse.get_pos()):
            ventana.blit(imagen_regresar_hover, boton_regresar_rect.topleft)  # Mostrar imagen con hover
            #pygame.mixer.Sound.play(pygame.mixer.Sound("assets/musica/boton.mp3"))
        else:
            ventana.blit(imagen_regresar, boton_regresar_rect.topleft)  # Mostrar imagen normal

        if boton_siguiente_rect.collidepoint(pygame.mouse.get_pos()):
            ventana.blit(imagen_siguiente_hover, boton_siguiente_rect.topleft)  # Mostrar imagen con hover
            #pygame.mixer.Sound.play(pygame.mixer.Sound("assets/musica/boton.mp3"))
        else:
               ventana.blit(imagen_siguiente, boton_siguiente_rect.topleft)  # Mostrar imagen normal
        
    

    pygame.display.flip()  # Actualizar pantalla


=======
        ventana.blit(boton_siguiente, boton_siguiente_rect.topleft)

    pygame.display.flip()  # Actualizar pantalla

>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1
    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
<<<<<<< HEAD
            
=======
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1
            if boton_pausa_rect.collidepoint(event.pos):  # Verificar si el clic está sobre el botón de pausa
                juego_en_pausa = not juego_en_pausa  # Cambiar estado de pausa
                if juego_en_pausa:
                    imagen_boton_pausa = imagen_pause  # Cambiar imagen a "pause"
                    pygame.mixer.Sound.play(pygame.mixer.Sound("assets/musica/unpause.mp3"))
<<<<<<< HEAD
                    
=======
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1
                else:
                    imagen_boton_pausa = imagen_play  # Cambiar imagen a "play"
                    pygame.mixer.Sound.play(pygame.mixer.Sound("assets/musica/pausar.mp3"))
                
            elif boton_musica_rect.collidepoint(event.pos):  # Verificar si el clic está sobre el botón de música
                musica_muted = not musica_muted  # Cambiar estado de música
                if musica_muted:
                    pygame.mixer.pause()  # Mutear música
                    imagen_boton_musica = imagen_noaudio  # Cambiar imagen a "no audio"
                else:
                    pygame.mixer.unpause()  # Reanudar música
                    imagen_boton_musica = imagen_audio  # Cambiar imagen a "audio"
<<<<<<< HEAD
                    
  
                    
                    
                    #                                      BOTONES QUE APARECEN AL FINALIZAR O NO EL NIVEL
                    
                    
            #________________________________________________________________________________________________________________________________________________________________________________  NIVEL COMPLETADO
            elif boton_regresar_rect.collidepoint(event.pos):  # Verificar si el clic está sobre el botón de "Regresar"                     regresar        nivel completado
                # Volver al menú principal o nivel anterior
                pygame.quit()
                ejecutar_script("assets/menu/principiante.py")

            elif boton_siguiente_rect.collidepoint(event.pos):  # Verificar si el clic está sobre el botón de "Siguiente nivel"             boton siguiente nivel completado
                # Siguiente nivel o transición interna sin ejecutar otro archivo
                pygame.quit()
                ejecutar_script("assets/niveles/principiante/nivel2/nivel2.py")

            #________________________________________________________________________________________________________________________________________________________________________________  SIN ANZUELOS
            elif boton_regresar_rect2.collidepoint(event.pos):  # Verificar si el clic está sobre el botón de "Regresar"                     regresar        nivel completado
                # Volver al menú principal o nivel anterior
                pygame.quit()
                ejecutar_script("assets/menu/principiante.py")

            elif boton_siguiente_rect2.collidepoint(event.pos):  # Verificar si el clic está sobre el botón de "Siguiente nivel"             boton repetir nivel sin anzuelos
                # Siguiente nivel o transición interna sin ejecutar otro archivo
                pygame.quit()
                ejecutar_script("assets/niveles/principiante/nivel1/nivel1.py")

            #________________________________________________________________________________________________________________________________________________________________________________ SIN TIEMPO
            elif boton_regresar_rect3.collidepoint(event.pos):  # Verificar si el clic está sobre el botón de "Regresar"                     regresar        nivel completado
                # Volver al menú principal o nivel anterior
                pygame.quit()
                ejecutar_script("assets/menu/principiante.py")

            elif boton_siguiente_rect3.collidepoint(event.pos):  # Verificar si el clic está sobre el botón de "Siguiente nivel"             boton repetir nivel sin tiempo
                # Siguiente nivel o transición interna sin ejecutar otro archivo
                pygame.quit()
                ejecutar_script("assets/niveles/principiante/nivel1/nivel1.py")
     
            #________________________________________________________________________________________________________________________________________________________________________________
=======

            elif boton_regresar_rect.collidepoint(event.pos):  # Verificar si el clic está sobre el botón de "Regresar"
                # Volver al menú principal o nivel anterior
                juego_en_pausa = False
                nivel_completado = False
                contador_puntos = 0
                anzulos_disponibles = 10
                tiempo = 60
                os.system("main.py")
                # Cargar lógica o pantallas previas sin cambiar de archivo

            elif boton_siguiente_rect.collidepoint(event.pos):  # Verificar si el clic está sobre el botón de "Siguiente nivel"
                # Siguiente nivel o transición interna sin ejecutar otro archivo
                pass
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1

        ###################### Funciones de teclas ##################################
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                mover_izquierda = True
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                mover_derecha = True
<<<<<<< HEAD
            if event.key == pygame.K_SPACE and not juego_en_pausa and tiempo > 0 and anzuelos_disponibles > 0:
                anzuelo_lanzado = True
                anzuelo_posicion = [jugador.forma.x + 35, jugador.forma.y - 20]  # Posición de la lata al lanzarla
                anzuelos_disponibles -= 1  # Disminuir el contador de anzuelos
            if tiempo == 15:
                pygame.mixer.Sound.play(pygame.mixer.Sound("assets/musica/alert.mp3"))
            if tiempo == 0 or anzuelos_disponibles == 0:
=======
            if event.key == pygame.K_SPACE and not juego_en_pausa and tiempo > 0 and anzulos_disponibles > 0:
                anzuelo_lanzado = True
                anzuelo_posicion = [jugador.forma.x + 35, jugador.forma.y - 20]  # Posición de la lata al lanzarla
                anzulos_disponibles -= 1  # Disminuir el contador de anzuelos
            if tiempo == 15:
                pygame.mixer.Sound.play(pygame.mixer.Sound("assets/musica/alert.mp3"))
            if tiempo == 0 or anzulos_disponibles == 0:
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1
                pygame.mixer.Sound.play(pygame.mixer.Sound("assets/musica/gameover.mp3"))

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                mover_izquierda = False
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                mover_derecha = False
<<<<<<< HEAD
            if event.key ==  pygame.K_p:
                
                juego_en_pausa = not juego_en_pausa  # Cambiar estado de pausa
                if juego_en_pausa:
                        imagen_boton_pausa = imagen_pause  # Cambiar imagen a "pause"
                        pygame.mixer.Sound.play(pygame.mixer.Sound("assets/musica/unpause.mp3"))
                else:
                        imagen_boton_pausa = imagen_play  # Cambiar imagen a "play"
                        pygame.mixer.Sound.play(pygame.mixer.Sound("assets/musica/pausar.mp3"))
                
            if event.key == pygame.K_m:
                musica_muted = not musica_muted  # Cambiar estado de música
                if musica_muted:
                    pygame.mixer.pause()  # Mutear música
                    imagen_boton_musica = imagen_noaudio  # Cambiar imagen a "no audio"
                else:
                    pygame.mixer.unpause()  # Reanudar música
                    imagen_boton_musica = imagen_audio  # Cambiar imagen a "audio"
=======
>>>>>>> 2cdf67de6b1c593535456b1379ac5791a8fa5ee1

pygame.quit()  # Cerrar el juego
sys.exit()
