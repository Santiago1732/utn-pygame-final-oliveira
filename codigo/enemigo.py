import pygame
from tiles import TileAnimada
from random import randint

class Enemigo(TileAnimada):
    def __init__(self,tamaño,x,y,path):
        super().__init__(tamaño,x,y,path)
        self.rect.y += tamaño - self.image.get_size()[1]
        self.velocidad = randint(3,5)

    def movimiento(self):
        '''
        Actualiza la posición del enemigo al moverlo hacia la izquierda a una velocidad determinada.
        :return:
        '''
        self.rect.x -= self.velocidad

    def imagen_reversa(self):
        '''
        Cambia la imagen del enemigo para que se vea en la dirección opuesta si su velocidad es positiva.
        :return:
        '''
        if self.velocidad > 0:
            self.image = pygame.transform.flip(self.image,True,False)


    def reversa(self):
        '''
         Invierte la dirección de movimiento del enemigo multiplicando su velocidad por -1.
        :return:
        '''
        self.velocidad *= -1


    def update(self,shift):
        '''
         Actualiza la posición horizontal del enemigo, su animación, su movimiento y la dirección de la imagen en función del desplazamiento proporcionado (shift).
        :param shift:
        :return:
        '''
        self.rect.x += shift
        self.animar()
        self.movimiento()
        self.imagen_reversa()