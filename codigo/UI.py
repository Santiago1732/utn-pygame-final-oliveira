import pygame

class UI:
    def __init__(self, superficie):
        #setupd
        self.superficie_visualizacion = superficie
        self.monedas_plateadas_contador = pygame.image.load('../graficos/monedas/mon-plateada.png')
        self.monedas_rectangulo = self.monedas_plateadas_contador.get_rect(topleft = (50,61))
        self.fuente = pygame.font.Font('../graficos/fuentes/HOLIDAYZONE.ttf',30)

    def mostrar_monedas(self,cantidad):
        '''
        Muestra las monedas recolectadas por nivel
        :param cantidad:
        :return:
        '''
        self.superficie_visualizacion.blit(self.monedas_plateadas_contador,(20,80))
        cantidad_monedas_superficie = self.fuente.render(str(cantidad),False,'#33323d')
        cantidad_monedas_rectangulo = cantidad_monedas_superficie.get_rect(midleft =(self.monedas_rectangulo.right + 4, self.monedas_rectangulo.centery))
        self.superficie_visualizacion.blit(cantidad_monedas_superficie, cantidad_monedas_rectangulo)
        pass

