import pygame,sys

class Interfaz:
    def __init__(self,superficie):
        self.superficie_visualizacion = superficie
        self.monedas = pygame.image.load('../graficos/monedas/moneda_interfaz.png')
        self.monedas_rectangulo = self.monedas.get_rect(topleft = (50,61))
        self.fuente = pygame.font.Font('../graficos/fuentes/HOLIDAYZONE.ttf',60)

    def mostrar_monedas(self,cantidad):
        '''
        mostrar la cantidad de monedas en la interfaz visual del juego.
        :param cantidad:
        :return:
        '''
        self.superficie_visualizacion.blit(self.monedas, self.monedas_rectangulo)
        monedas_cantidad = self.fuente.render(str(cantidad),False,'#33323d')
        monedas_rectangulo = monedas_cantidad.get_rect(midleft = (self.monedas_rectangulo.right + 4 ,self.monedas_rectangulo.centery))
        self.superficie_visualizacion.blit(monedas_cantidad,monedas_rectangulo)
        pass
