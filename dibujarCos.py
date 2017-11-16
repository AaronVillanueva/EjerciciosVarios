import pygame, math, random

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255,255,255)
AZUL = (0, 0, 255)
ROJO = (255, 0, 0)
NEGRO=(0,0,0)

def generarColorAzar():
    return(random.randint(0,255),random.randint(0,255),random.randint(0,255))


def dibujarEjes(ventana):
    pygame.draw.line(ventana, AZUL, (0, ALTO // 2), (ANCHO, ALTO // 2), 2)
    pygame.draw.line(ventana, AZUL, (ANCHO // 2, 0), (ANCHO // 2, ALTO), 2)

def dibujarCoseno(ventana):
    for angulo in range(-(ANCHO//2),ANCHO//2):
        angRad= math.radians(angulo)
        y= math.cos(angRad)
        y=int(100*y)
        pygame.draw.circle(ventana, ROJO,(angulo+ANCHO//2,ALTO//2-y),2)

def dibujarPolares(ventana):
    angulo=0
    while angulo<360:
    #for angulo in range(-(ANCHO//2),ANCHO//2):
        angRad= math.radians(10*angulo)
        y= math.cos(8*angRad)
        radio=int(300*y)
        x= radio* math.cos(angRad)
        y= radio* math.sin(angRad)
        x=int(x)
        y=int(y)
        colorAzar=generarColorAzar()
        pygame.draw.circle(ventana, colorAzar,(x+ANCHO//2,ALTO//2 - y),2)
        angulo+=.1


def graficarFuncion():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(NEGRO)

        dibujarEjes(ventana)
        #dibujarCoseno(ventana)
        dibujarPolares(ventana)


        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()


def main():
    graficarFuncion()

main()
