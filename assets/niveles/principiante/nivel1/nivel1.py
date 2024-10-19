import pygame
import sys
import os
import random


# Configuración del sistema
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../")))#para saltar carpetas hacia arriba
import constantes


from personajes import Personaje

pygame.init()
pygame.mixer.init()



# Cargar imágenes y sonidos

#aqui estamos haciendo un ciclo del 1 al 3. hay dos imagenes para la animcaion del 
#gato: "cat_1", "cat_2". este ciclo lo estamos colocando en cat_{i}.png para que 
# cuando se active "animaciones=[]" se comienzen a sobreponer las imagenes indefinidamente#

animaciones = []
for i in range(2):
    try:
        img = pygame.image.load(f"assets/personajes/naranjo/cat_{i}.png")
        img = Personaje.escalar_img(img, 120, 120) #llamamos a la funcion "escalar_img" de personajes.py y rellenamos#
        animaciones.append(img)
    except pygame.error as e:
        print(f"No se pudo cargar la imagen: {e}") #si hay algun error con esta imagen y no se puede cargar imprimira 
                                                    #en la terminal que no se pudo cargar la imagen #
        

ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))#aqui se define el alto y ancho de la ventana
pygame.display.set_caption("PESCA-DOS (Principiante-Nivel 1)")#aqui colocamos el nombre del juego


# imágenes para los botones de pausa y música
imagen_play = pygame.image.load("assets/menu/play.png")
imagen_pause = pygame.image.load("assets/menu/pause.png")
imagen_audio = pygame.image.load("assets/menu/audio.png")
imagen_noaudio = pygame.image.load("assets/menu/noaudio.png")

# Escalamos las imagenes, primero se llaman y luego se les ajusta el tamaño. como dato no se puede hacer esto al revez
imagen_play = Personaje.escalar_img(imagen_play, 50, 50)
imagen_pause = Personaje.escalar_img(imagen_pause, 50, 50) #aqui solo definimos el tamaño de 50 pixeles de alto X 50 pixeles de ancho
imagen_audio = Personaje.escalar_img(imagen_audio, 50, 50)
imagen_noaudio = Personaje.escalar_img(imagen_noaudio, 50, 50)

# Inicialmente, mostrar las imágenes "play" y "audio"
imagen_boton_pausa = imagen_play    # esto se necesitara al momento de hacer la animacion de pause y mute
imagen_boton_musica = imagen_audio



# Cargar imágenes adicionales
gato_mirando_al_rio = pygame.image.load(constantes.GATO_MIRANDO_AL_RIO)
gato_mirando_al_rio = Personaje.escalar_img(gato_mirando_al_rio, 120, 120)


#------------------------------imagenes del final del nivel, descomentar despues----------------------------

#imagen_fin = pygame.image.load(constantes.IMAGEN_FIN)
#imagen_fin = personajes.escalar_img(imagen_fin, 200, 200)

# imagen_mrblanco = pygame.image.load("assets/personajes/blanco/MrBlanco.png")
# imagen_mrblanco = personajes.escalar_img(imagen_mrblanco, 90, 90)
#------------------------------------------------------------------------------------------------------------

sonido_golpe = pygame.mixer.Sound("assets/musica/golpe_1.mp3")  #sonido que se reproduce cuando se golpea un objeto

# Lista de las imagenes basura, etso es una prueba, cambiar despues.
imagenes_basura = [
    pygame.image.load("assets/items/basura/botella_vidrio.png"),
    pygame.image.load("assets/items/basura/lata_atun.png"),
    pygame.image.load("assets/items/basura/lata_aplastada.png"),
    pygame.image.load("assets/items/basura/manzana_mordida.png"),
    pygame.image.load("assets/items/basura/botella_plastico_aplastada.png")

]

#el tamaño general de las imagenes de la basura
imagenes_basura = [Personaje.escalar_img(img, 50, 50) for img in imagenes_basura]



# Variables del juego
posiciones_flotantes = [random.randint(50, constantes.ANCHO_VENTANA - 100) for _ in range(constantes.FILAS)]
direcciones_flotantes = [1] * constantes.FILAS
velocidad_flotante = constantes.VELOCIDAD_FLOTANTE
alturas_flotantes = [180 + i * 60 for i in range(constantes.FILAS)]

# Asignar imágenes aleatorias a cada objeto flotante
imagenes_flotantes = [random.choice(imagenes_basura) for _ in range(constantes.FILAS)]

jugador = Personaje(500, 500, animaciones)

mover_izquierda = False
mover_derecha = False

juego_en_pausa = False
musica_muted = False
fuente = pygame.font.Font("assets/fonts/press.ttf", 36)  # Cambiar a la tipografía del 

# Variables para la lata
lata_posicion = [0, 0]  # Posición inicial de la lata
anzuelo_lanzado = False  #en el bucle principal cuando se presione la tecla SPACE se pasara a true
lata_velocidad = 5  # Velocidad de la lata

contador_puntos = 0  #contador inicial del juego
nivel_completado = False  # Nueva variable para controlar si el nivel ha sido completado
anzuelos_disponibles = 10  # Contador de anzuelos

reloj = pygame.time.Clock() 
tiempo = 60 #tiempo inicial del reloj, irá de manera descendente 

sonido_fondo = pygame.mixer.Sound(constantes.MUSICA_FONDO) #aqui se llama del archivo "constantes.py" la constante donde se encuentra la musica de fondo
pygame.mixer.Sound.play(sonido_fondo, -1) #aqui se reproduce la cancion y el -1 es para que cuando acabe la cancion se vuelva a reproducir

# Botones rectangulares
boton_musica_rect = pygame.Rect(10, 110, 50, 50) #  Este es el tamaño de boton de la musica
boton_pausa_rect = pygame.Rect(10, 50, 50, 50)  # Este es el tamaño del boton para pausar el juego





##################  BUCLE PRINCIPAL  ##################

run = True
while run: #mientras la variable run esté activa el bucle se iniciará, si esta variable se pasa a false el bucle se detiene junto con el nivel
    reloj.tick(constantes.FPS) #se calcula la velocidad de cuadros por segundo del reloj, se llama a fps (dentro de constantes.py)
    if not juego_en_pausa and tiempo > 0: #si el tiempo en pausa (true) cambia a false y el timepo es mayor a 0 (osea que si todavia en el nivel te queda timepo) va a hacer:
        tiempo -= 1 / constantes.FPS#       que el tiempo se pare

    ventana.blit(constantes.IMG_BACKGROUND, (0, 0)) # y que la imagen de fondo se sobreponga atras de las basuras
    delta_x = 0 # que el jugador no se pueda mover ya que esta variable va a pasar a 0 y esto impide que el jugador muestre movimiento

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

    # Renderizar tiempo, puntos y anzuelos
    texto_tiempo = fuente.render(f'Tiempo: {int(tiempo)}', True, (255, 0, 0))
    ventana.blit(texto_tiempo, (10, 10))
    
    
    texto_puntos = fuente.render(f'Puntos: {contador_puntos}', True, (255, 0, 0))
    ventana.blit(texto_puntos, (constantes.ANCHO_VENTANA - texto_puntos.get_width() - 10, 10))
    
    
    
    texto_anzuelos = fuente.render(f'Anzuelos:{anzuelos_disponibles}', True, (255, 0, 0))
    ventana.blit(texto_anzuelos, (constantes.ANCHO_VENTANA - texto_anzuelos.get_width() - 10, 50))

    # Mover y dibujar objetos  carta
    flotantes_activos = False  # Variable para verificar si hay flotantes activos
    for i in range(constantes.FILAS):
        x = posiciones_flotantes[i]
        y = alturas_flotantes[i]
        if not juego_en_pausa and tiempo > 0 and not nivel_completado:
            ventana.blit(imagenes_flotantes[i], (x, y))  # Usar imagen aleatoria
            x += velocidad_flotante * direcciones_flotantes[i]
            if x >= constantes.ANCHO_VENTANA - imagenes_flotantes[i].get_width() or x <= 0:
                direcciones_flotantes[i] *= -1
            posiciones_flotantes[i] = x
            flotantes_activos = True  # Hay al menos un flotante activo

    # Mostrar la lata si ha sido lanzada 
    if anzuelo_lanzado: 
        img_anzuelo = pygame.image.load("assets/items/anzuelo.png")# se crea la variable de la imagen del anzuelo
        img_anzuelo = Personaje.escalar_img(img_anzuelo, 50, 50)  #le asignamos tamaño a la imagen del anzuelo
        lata_posicion[1] -= lata_velocidad  # Mover la lata hacia arriba
        ventana.blit(img_anzuelo, (lata_posicion[0], lata_posicion[1])) #aqui se muestra la imagen del anzuelo

        # Comprobar colisiones con los objetos flotantes
        for i in range(constantes.FILAS): #el rango es 4
            if (posiciones_flotantes[i] < lata_posicion[0] < posiciones_flotantes[i] + imagenes_flotantes[i].get_width() and
                alturas_flotantes[i] < lata_posicion[1] < alturas_flotantes[i] + imagenes_flotantes[i].get_height()):
                
                # Reiniciar posiciones al chocar
                anzuelo_lanzado = False  # Reiniciar el lanzamiento
                lata_posicion = [jugador.forma.x + 35, jugador.forma.y - 20]  # Resetear posición de la lata
                contador_puntos += 1  # Aumentar contador de puntos
                imagenes_flotantes[i] = random.choice(imagenes_basura)  # Cambiar a una nueva imagen de basura

    # Mostrar imagen de "MrBlanco" si el contador llega a 4
    if contador_puntos >= 4:
        nivel_completado = True  # Cambiar el estado a completado
        mensaje_final = fuente.render("¡FELICIDADES!, NIVEL 1 COMPLETADO", True, (255, 215, 0))
        ventana.blit(mensaje_final, (constantes.ANCHO_VENTANA // 2 - mensaje_final.get_width() // 2, 
                                      constantes.ALTO_VENTANA // 2 - mensaje_final.get_height() // 2))
       # ventana.blit(imagen_mrblanco, (300, 0))  # Mostrar imagen de MrBlanco

    # Mensaje final si se quedan sin anzuelos
    if anzuelos_disponibles <= 0:
        mover_derecha=False
        mover_izquierda=False
        
        
        mensaje_final = fuente.render("Sin anzuelos ¡se terminó la pesca!", True, (255, 215, 0))
        ventana.blit(mensaje_final, (constantes.ANCHO_VENTANA // 2 - mensaje_final.get_width() // 2, 
                                      constantes.ALTO_VENTANA // 2 - mensaje_final.get_height() // 2))
       # ventana.blit(imagen_fin, (constantes.ANCHO_VENTANA // 2 - imagen_fin.get_width() // 2, 
        #                           constantes.ALTO_VENTANA // 2 - imagen_fin.get_height() // 2))

    # Manejar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                mover_izquierda = True
            if event.key == pygame.K_RIGHT  or event.key == pygame.K_d:
                mover_derecha = True
            if event.key == pygame.K_SPACE and not juego_en_pausa and tiempo > 0 and anzuelos_disponibles > 0:
                anzuelo_lanzado = True
                lata_posicion = [jugador.forma.x + 35, jugador.forma.y - 20]  # Posición de la lata al lanzarla
                anzuelos_disponibles -= 1  # Disminuir el contador de anzuelos
            if event.key == pygame.K_p:
                juego_en_pausa = not juego_en_pausa
                if juego_en_pausa:
                    imagen_boton_pausa = imagen_pause  # Cambiar imagen a "pause"
                else:
                    imagen_boton_pausa = imagen_play  # Cambiar imagen a "play"
            if event.key == pygame.K_m:
                musica_muted = not musica_muted
                if musica_muted:
                    pygame.mixer.pause()  # Mutear música
                    imagen_boton_musica = imagen_noaudio  # Cambiar imagen a "no audio"
                else:
                    pygame.mixer.unpause()  # Reanudar música
                    imagen_boton_musica = imagen_audio  # Cambiar imagen a "audio"
                    
        if event.type == pygame.KEYUP :
            if event.key == pygame.K_LEFT  or event.key == pygame.K_a:
                mover_izquierda = False
            if event.key == pygame.K_RIGHT  or event.key == pygame.K_d:
                mover_derecha = False
                
        
    # Mensaje final si se quedan sin anzuelos
    if anzuelos_disponibles <= 0:
        mover_derecha=False  #el personaje no se puede mover a la derecha
        mover_izquierda=False#  ni a la izquierda
        
        
        
        
        mensaje_final = fuente.render("Sin anzuelos ¡se terminó la pesca!", True, (255, 215, 0))
        ventana.blit(mensaje_final, (constantes.ANCHO_VENTANA // 2 - mensaje_final.get_width() // 2, 
                                      constantes.ALTO_VENTANA // 2 - mensaje_final.get_height() // 2))
       # ventana.blit(imagen_fin, (constantes.ANCHO_VENTANA // 2 - imagen_fin.get_width() // 2, 
        #                           constantes.ALTO_VENTANA // 2 - imagen_fin.get_height() // 2))

    # Dibujar botones de música y pausa
    ventana.blit(imagen_boton_pausa, boton_pausa_rect)
    ventana.blit(imagen_boton_musica, boton_musica_rect)

    # Actualizar pantalla
    pygame.display.flip()

# Limpiar recursos al finalizar movimiento
pygame.quit()
