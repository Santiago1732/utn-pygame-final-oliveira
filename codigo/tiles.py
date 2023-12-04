import pygame
from support import importar_carpeta

class Tile(pygame.sprite.Sprite):
    def __init__(self,tamaño,x,y):
        super().__init__()
        self.image = pygame.Surface((tamaño,tamaño))
        # self.image.fill('grey')
        self.  rect = self.image.get_rect(topleft = (x,y))

    def update(self,shift):
        self.rect.x += shift

class StaticTile(Tile):
    '''
    Esta clase es una subclase de Tile y representa un "tile" estático con una imagen predefinida. Ttoma una superficie que se utiliza como imagen del "tile".
    '''
    def __init__(self, tamaño,x,y,superficie):
        super().__init__(tamaño,x,y)
        self.image = superficie

class TileAnimada(Tile):
    '''
    Esta clase es otra subclase de Tile y representa un "tile" animado que cambia de imagen con el tiempo.
    Toma un tamaño, coordenadas x e y, y una path que es la ruta al directorio que contiene las imágenes para la animación.
    Tiene un método animar() que cambia la imagen actual del tile y un método update(shift) que actualiza la posición y la animación del tile.
    '''
    def __init__(self,tamaño,x,y,path):
        super().__init__(tamaño,x,y)
        self.frames = importar_carpeta(path)
        self.frame_index = 0
        self.image = self.frames[self.frame_index]

    def animar(self):
        '''
        Avanza la animación del "tile" y actualiza su imagen.
        :return:
        '''
        self.frame_index += 0.15
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]

    def update(self,shift):
        '''
        : Actualiza la posición del "tile" y su animación.
        :param shift:
        :return:
        '''
        self.animar()
        self.rect.x += shift