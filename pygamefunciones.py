import pygame, math

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255,255,255)
AZUL = (0, 0, 255)
ROJO = (255, 0, 0)

def dibujarEjes(ventana):
    pygame.draw.line(ventana, AZUL, (0, ALTO // 2), (ANCHO, ALTO // 2), 2)
    pygame.draw.line(ventana, AZUL, (ANCHO // 2, 0), (ANCHO // 2, ALTO), 2)

def dibujarCoseno(ventana):
    for angulo in range(-(ANCHO//2),ANCHO//2):
        angRad= math.radians(angulo)
        y= math.cos(angRad)
        y=int(100*y)
        pygame.draw.circle(ventana, ROJO,(angulo+ANCHO//2,ALTO//2-y),2)

def graficarFuncion():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)

        dibujarEjes(ventana)
        dibujarCoseno(ventana)


        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()


def main():
    graficarFuncion()

main()
