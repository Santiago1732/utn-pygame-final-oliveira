import pygame
from codigo.support import importar_carpeta

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, superficie):
        super().__init__()
        self.importar_imagenes()
        self.imagen_index = 0
        self.velocidad_animacion = 0.15
        self.image = self.animaciones['inactivo'][self.imagen_index]
        self.rect = self.image.get_rect(topleft=pos)
        self.posicion_inicial = pos

        # movimiento player
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -16
                                                        # tupla
        self.colission_rectangulo = pygame.Rect(self.rect.topleft, (35,self.rect.height))

        # self.superficie_visualiazcion = superficie

        self.cara_derecha = True
        self.en_el_piso = False
        self.en_el_techo = False
        self.a_la_derecha = False
        self.a_la_izquierda = False

        # self.cantidad_monedas = 0
        self.vivo = True
        self.sonido_salto = pygame.mixer.Sound('../sonido/level_0/salto.mp3')

        @property
        def imagen_index(self):
            return self._imagen_index

        @imagen_index.setter
        def imagen_index(self, value):
            self._imagen_index = value

        @property
        def velocidad_animacion(self):
            return self._velocidad_animacion

        @velocidad_animacion.setter
        def velocidad_animacion(self, value):
            self._velocidad_animacion = value

        @property
        def direction(self):
            return self._direction

        @direction.setter
        def direction(self, value):
            self._direction = value

        @property
        def speed(self):
            return self._speed

        @speed.setter
        def speed(self, value):
            self._speed = value

        @property
        def gravity(self):
            return self._gravity

        @gravity.setter
        def gravity(self, value):
            self._gravity = value

        @property
        def jump_speed(self):
            return self._jump_speed

        @jump_speed.setter
        def jump_speed(self, value):
            self._jump_speed = value

        @property
        def vivo(self):
            return self._vivo

        @vivo.setter
        def vivo(self, value):
            self._vivo = value

    def importar_imagenes(self):
        '''
           Importa imagenes de una carpeta específica
           Se crea un diccionario y se construye un path para cada animación
           :param numero_str:
           :return:
           '''
        imagenes_path = '../graficos/character/'
        self.animaciones  = {'inactivo':[], 'saltando':[], 'corriendo':[],'cayendo':[]}

        for animacion in self.animaciones.keys():
            path_completo = imagenes_path + animacion
            self.animaciones[animacion] = importar_carpeta(path_completo)

    def animar(self):
        '''

        :return:
        '''

        animacion = self.animaciones[self.estado]

        # loop por cada index
        self.imagen_index += self.velocidad_animacion
        if self.imagen_index >= len(animacion):
            self.imagen_index = 0

        imagen = animacion[int(self.imagen_index)]
        if self.cara_derecha:
            # CHEQUEAR
            self.image = imagen
            self.rect.bottomleft = self.colission_rectangulo.bottomleft
        else:
            flipped_image = pygame.transform.flip(imagen,True,False)
            self.image = flipped_image
            self.rect.bottomright = self.colission_rectangulo.bottomright


    def get_input(self):
        '''
        Captura la entrada del usuario a través del teclado. Cambia la dirección y el estado del personaje en función de las teclas presionadas (derecha, izquierda, arriba para saltar).
        :param self:
        :return:
        '''
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 0.8
            # DIRECCION DE LA CARA
            self.cara_derecha = True
        elif keys[pygame.K_LEFT]:
            self.direction.x = -0.8
            # DIRECCION DE LA CARA
            self.cara_derecha = False
        else:
            self.direction.x = 0

        if keys[pygame.K_UP] and self.en_el_piso:
            self.sonido_salto.play()
            self.jump()

    # {'inactivo': [], 'saltando': [], 'corriendo': [], 'cayendo': []}
    def obtener_estado(self):
        '''
        Determina el estado actual del personaje (como 'saltando', 'cayendo', 'corriendo', 'inactivo') basándose en su dirección y movimiento.
        :param self:
        :return:
        '''
        if self.direction.y < 0:
            self.estado = 'saltando'
        elif self.direction.y > 1:
            self.estado = 'cayendo'
        else:
            if self.direction.x != 0:
                self.estado = 'corriendo'
            else:
                self.estado = 'inactivo'


    def apply_gravity(self):
        '''
        Aplica la gravedad al personaje, modificando el comprotamiento en su movimiento vertical.
        :return:
        '''
        self.direction.y += self.gravity
        # self.rect.y += self.direction.y
        self.colission_rectangulo.y += self.direction.y

    def jump(self):
        '''
        hace que el personaje salte
        :return:
        '''
        self.direction.y = self.jump_speed


    def update(self):
        '''
         Función principal que se llama en cada fotograma del juego. Gestiona la entrada del usuario, actualiza el estado del personaje, y aplica la animación y la gravedad.
        :return:
        '''
        self.get_input()
        self.obtener_estado()
        self.animar()
