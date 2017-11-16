# encoding: UTF-8

import pygame

# Dimensiones de la pantalla
ANCHO = 600
ALTO = 600
# Colores
BLANCO = (255,255,255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)
NEGRO=(0,0,0)

def interpretar(archivo,ventana):
    for linea in open(archivo):
        datos=linea.lower().split()
        if datos[0]=="r":
            x=int(datos[1])
            y=int(datos[2])
            ancho=int(datos[3])
            alto=int(datos[4])
            pygame.draw.rect(ventana, NEGRO,(x,y,ancho,alto),1)
        elif datos[0]=="c":
            x=int(datos[1])
            y=int(datos[2])
            r=int(datos[3])
            pygame.draw.circle(ventana,NEGRO,(x,y),r,1)


def dibujar(archivo):
    # Ejemplo del uso de pygame
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps
    termina = False # Bandera para saber si termina la ejecución

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        # Borrar pantalla
        ventana.fill(BLANCO)

        interpretar(archivo,ventana)

        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps

    pygame.quit()   # termina pygame


def main():
    archivoMain="prueba.pic"
    dibujar(archivoMain)

main()
