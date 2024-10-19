import pygame

pygame.init()


ventana=pygame.display.set_mode((1200,600))
pygame.display.set_caption("PESCA-DOS")

jugador=pygame.image.load("assets/personajes/naranjo/gato_1.png")
fondo=pygame.image.load("assets/fondo/menu.png")
ancho_personaje=90
alto_personaje=90
pygame.display.flip()









run=True
while run:
    for event in pygame.event.get():

                
        ventana.blit(fondo(0,0))
        ventana.blit(jugador(50.50))



        if event.type==pygame.QUIT:
            run=False
    pygame.display.update()
pygame.quit()









