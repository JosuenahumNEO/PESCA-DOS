import pygame
import constantes

class Personaje():
    def __init__(self, x, y, animaciones):
        self.flip = False  # Controla si la imagen debe estar volteada
        self.animaciones = animaciones
        self.index = 0
        self.image = self.animaciones[self.index]
        self.forma = pygame.Rect(0, 0, constantes.ANCHO_PERSONAJE, constantes.ALTO_PERSONAJE)
        self.forma.center = (x, y)
        self.velocidad = 0
    
    def movimiento(self, delta_x, delta_y):
        if delta_x < 0:  # Movimiento a la derecha
            self.flip = False
        elif delta_x > 0:  # Movimiento a la izquierda
            self.flip = True
        
        self.forma.x += delta_x
        self.forma.y += delta_y
        self.velocidad = abs(delta_x) + abs(delta_y)
        self.animar()
    
    def animar(self):
        if self.velocidad > 0:  # Solo cambia la animación si el personaje se mueve
            self.index += 0.1  # Cambia el índice de animación (0.1 para animación fluida)
            if self.index >= len(self.animaciones):
                self.index = 0
            self.image = self.animaciones[int(self.index)]
    
    def dibujar(self, ventana):
        imagen_flip = pygame.transform.flip(self.image, self.flip, False)
        ventana.blit(imagen_flip, self.forma)
        
        
        
    def escalar_img(image, width, height):
        return pygame.transform.scale(image, (width, height))
