import pygame
import sys

pygame.init()


screen_size = (1200, 600)

screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
pygame.display.set_caption("Mi amigo Mr.Blanco")

# Cargar assets/menu/cinematica/imagenes para cinematica
imagen1 = pygame.image.load("assets/menu/cinematica/imagenes/imagen1.png")
imagen2 = pygame.image.load("assets/menu/cinematica/imagenes/imagen2.png")
imagen3 = pygame.image.load("assets/menu/cinematica/imagenes/imagen3.png")
imagen4 = pygame.image.load("assets/menu/cinematica/imagenes/imagen4.png")
imagen5 = pygame.image.load("assets/menu/cinematica/imagenes/imagen5.png")
imagen6 = pygame.image.load("assets/menu/cinematica/imagenes/imagen6.png")
imagen7 = pygame.image.load("assets/menu/cinematica/imagenes/imagen7.png")
imagen8 = pygame.image.load("assets/menu/cinematica/imagenes/imagen8.png")
imagen9 = pygame.image.load("assets/menu/cinematica/imagenes/imagen9.png")
imagen10 = pygame.image.load("assets/menu/cinematica/imagenes/imagen10.png")
imagen11 = pygame.image.load("assets/menu/cinematica/imagenes/imagen11.png")
imagen12 = pygame.image.load("assets/menu/cinematica/imagenes/imagen12.png")
imagen13 = pygame.image.load("assets/menu/cinematica/imagenes/imagen13.png")
imagen14 = pygame.image.load("assets/menu/cinematica/imagenes/imagen14.png")
imagen15 = pygame.image.load("assets/menu/cinematica/imagenes/imagen15.png")
imagen16 = pygame.image.load("assets/menu/cinematica/imagenes/imagen16.png")
imagen17 = pygame.image.load("assets/menu/cinematica/imagenes/imagen17.png")
imagen18 = pygame.image.load("assets/menu/cinematica/imagenes/imagen18.png")
imagen19 = pygame.image.load("assets/menu/cinematica/imagenes/imagen19.png")
imagen20 = pygame.image.load("assets/menu/cinematica/imagenes/imagen20.png")
imagen21 = pygame.image.load("assets/menu/cinematica/imagenes/imagen21.png")
imagen22 = pygame.image.load("assets/menu/cinematica/imagenes/imagen22.png")
imagen23 = pygame.image.load("assets/menu/cinematica/imagenes/imagen23.png")

# Secuencia de assets/menu/cinematica/imagenes para la cinematica

cinematica = [
    {"imagen": imagen1, "tiempo": 2000}, 
    {"imagen": imagen2, "tiempo": 700}, 
    {"imagen": imagen3, "tiempo": 700},
    {"imagen": imagen4, "tiempo": 2000},
    {"imagen": imagen5, "tiempo": 1000},
    {"imagen": imagen6, "tiempo": 1000},
    {"imagen": imagen7, "tiempo": 1000},
    {"imagen": imagen8, "tiempo": 1000},
    {"imagen": imagen9, "tiempo": 1000},
    {"imagen": imagen10, "tiempo": 1000},
    {"imagen": imagen11, "tiempo": 1000},
    {"imagen": imagen12, "tiempo": 1000}, 
    {"imagen": imagen13, "tiempo": 1000},
    {"imagen": imagen14, "tiempo": 1000},
    {"imagen": imagen15, "tiempo": 1000},
    {"imagen": imagen16, "tiempo": 1000},
    {"imagen": imagen17, "tiempo": 1000},
    {"imagen": imagen18, "tiempo": 1000},
    {"imagen": imagen19, "tiempo": 1000},
    {"imagen": imagen20, "tiempo": 1000},
    {"imagen": imagen21, "tiempo": 1000},
    {"imagen": imagen22, "tiempo": 1000},
    {"imagen": imagen23, "tiempo": 2000},  
]

# Mostrar cinematica

def mostrar_cinematica():
    for escena in cinematica:
     screen.blit(escena["imagen"],(0,0))
     pygame.display.update()
     pygame.time.wait(escena["tiempo"])
     clock.tick(60)
     
mostrar_cinematica()
