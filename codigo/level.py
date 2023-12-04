import pygame

from pygame import *
from codigo import player
from support import importar_csv_layout, importar_graficos
from settings import tiles_tamaño
from tiles import Tile, StaticTile
from enemigo import Enemigo
from player import Player
from settings import *
from UI import *
from data_juego import levels
import random

class Level:
    def __init__(self, level_data, superficie, level_actual):
        self.superficie_visualizacion = superficie
        self.mundo_shift = 0
        self.x_actual = None
        # PL AYER
        mapa_player = importar_csv_layout(level_data['player'])
        self.player = pygame.sprite.GroupSingle()
        self.player_setup(mapa_player)
        self.goal = pygame.sprite.GroupSingle()
        self.cambia_level = False
        self.level_actual = level_actual
        self.movimiento_pantalla = False
        self.ui = UI(superficie)
        self.cambiar_monedas = 0
        self.vivo = True
        self.sonido_moneda = pygame.mixer.Sound('../sonido/level_0/moneda.mp3')
        self.sonido_dolor = pygame.mixer.Sound('../sonido/level_0/dolor.mp3')
        self.sonido_lv_up = pygame.mixer.Sound('../sonido/level_0/mu_online_level_up.mp3')
        self.sonido_dolor_enemigo = pygame.mixer.Sound('../sonido/level_0/Minecraft Damage - Sound Effect.mp3')
        self.cantidad_monedas = 0

        @property
        def superficie_visualizacion(self):
            return self._superficie_visualizacion

        @superficie_visualizacion.setter
        def superficie_visualizacion(self, superficie):
            self._superficie_visualizacion = superficie

        @property
        def mundo_shift(self):
            return self._mundo_shift

        @mundo_shift.setter
        def mundo_shift(self, shift):
            self._mundo_shift = shift

        @property
        def x_actual(self):
            return self._x_actual

        @x_actual.setter
        def x_actual(self, x_actual):
            self._x_actual = x_actual

        @property
        def player(self):
            return self._player

        @player.setter
        def player(self, player):
            self._player = player

        @property
        def goal(self):
            return self._goal

        @goal.setter
        def goal(self, goal):
            self._goal = goal

        @property
        def cambia_level(self):
            return self._cambia_level

        @cambia_level.setter
        def cambia_level(self, cambia_level):
            self._cambia_level = cambia_level

        @property
        def level_actual(self):
            return self._level_actual

        @level_actual.setter
        def level_actual(self, level_actual):
            self._level_actual = level_actual

        @property
        def movio_pantalla(self):
            return self._movio_pantalla

        @movio_pantalla.setter
        def movio_pantalla(self, movio_pantalla):
            self._movio_pantalla = movio_pantalla

        @property
        def ui(self):
            return self._ui

        @ui.setter
        def ui(self, ui):
            self._ui = ui

        @property
        def cambiar_monedas(self):
            return self._cambiar_monedas

        @cambiar_monedas.setter
        def cambiar_monedas(self, cambiar_monedas):
            self._cambiar_monedas = cambiar_monedas

        @property
        def vivo(self):
            return self._vivo

        @vivo.setter
        def vivo(self, vivo):
            self._vivo = vivo

        @property
        def sonido_moneda(self):
            return self._sonido_moneda

        @sonido_moneda.setter
        def sonido_moneda(self, sonido_moneda):
            self._sonido_moneda = sonido_moneda

        @property
        def sonido_dolor(self):
            return self._sonido_dolor

        @sonido_dolor.setter
        def sonido_dolor(self, sonido_dolor):
            self._sonido_dolor = sonido_dolor

        @property
        def sonido_lv_up(self):
            return self._sonido_lv_up

        @sonido_lv_up.setter
        def sonido_lv_up(self, sonido_lv_up):
            self._sonido_lv_up = sonido_lv_up

        @property
        def sonido_lv_0(self):
            return self._sonido_lv_0

        @sonido_lv_0.setter
        def sonido_lv_0(self, sonido_lv_0):
            self._sonido_lv_0 = sonido_lv_0

        @property
        def sonido_lv_1(self):
            return self._sonido_lv_1

        @sonido_lv_1.setter
        def sonido_lv_1(self, sonido_lv_1):
            self._sonido_lv_1 = sonido_lv_1

        @property
        def sonido_lv_2(self):
            return self._sonido_lv_2

        @sonido_lv_2.setter
        def sonido_lv_2(self, sonido_lv_2):
            self._sonido_lv_2 = sonido_lv_2

        @property
        def sonido_lv_3(self):
            return self._sonido_lv_3

        @sonido_lv_3.setter
        def sonido_lv_3(self, sonido_lv_3):
            self._sonido_lv_3 = sonido_lv_3

        @property
        def cantidad_monedas(self):
            return self._cantidad_monedas

        @cantidad_monedas.setter
        def cantidad_monedas(self, cantidad_monedas):
            self._cantidad_monedas = cantidad_monedas


        if self.level_actual == 0:
            # LV 0
            mapa_terreno = importar_csv_layout(level_data['terreno'])
            self.terreno_sprites = self.crear_grupo_tiles(mapa_terreno, 'terreno')

            mapa_monedas = importar_csv_layout(level_data['monedas'])
            self.modenas_sprites = self.crear_grupo_tiles(mapa_monedas, 'monedas')

            mapa_moneda_plateada = importar_csv_layout(level_data['monedas_plateada'])
            self.modenas_plateadas_sprites = self.crear_grupo_tiles(mapa_moneda_plateada, 'monedas_plateada')

            mapa_enemigo = importar_csv_layout(level_data['enemigo'])
            self.enemigo_sprites = self.crear_grupo_tiles(mapa_enemigo, 'enemigo')

        if self.level_actual == 1:
            # LV 2
            mapa_terreno = importar_csv_layout(level_data['terreno'])
            self.terreno_sprites = self.crear_grupo_tiles(mapa_terreno, 'terreno')

            mapa_monedas = importar_csv_layout(level_data['monedas'])
            self.modenas_sprites = self.crear_grupo_tiles(mapa_monedas, 'monedas')

            mapa_moneda_plateada = importar_csv_layout(level_data['monedas_plateada'])
            self.modenas_plateadas_sprites = self.crear_grupo_tiles(mapa_moneda_plateada, 'monedas_plateada')

            mapa_enemigo = importar_csv_layout(level_data['enemigo'])
            self.enemigo_sprites = self.crear_grupo_tiles(mapa_enemigo, 'enemigo')

            mapa_lava = importar_csv_layout(level_data['lavax'])
            self.lava_sprites = self.crear_grupo_tiles(mapa_lava, 'lavax')

        if self.level_actual == 2:
            # LV 2
            mapa_terreno = importar_csv_layout(level_data['terreno'])
            self.terreno_sprites = self.crear_grupo_tiles(mapa_terreno, 'terreno')

            mapa_monedas = importar_csv_layout(level_data['monedas'])
            self.modenas_sprites = self.crear_grupo_tiles(mapa_monedas, 'monedas')

            mapa_moneda_plateada = importar_csv_layout(level_data['monedas_plateada'])
            self.modenas_plateadas_sprites = self.crear_grupo_tiles(mapa_moneda_plateada, 'monedas_plateada')

            mapa_enemigo = importar_csv_layout(level_data['enemigo'])
            self.enemigo_sprites = self.crear_grupo_tiles(mapa_enemigo, 'enemigo')

            mapa_pinches = importar_csv_layout(level_data['pinches'])
            self.pinches_sprites = self.crear_grupo_tiles(mapa_pinches, 'pinches')

        if self.level_actual == 3:
            # LV 3
            mapa_terreno = importar_csv_layout(level_data['terreno'])
            self.terreno_sprites = self.crear_grupo_tiles(mapa_terreno, 'terreno')

            mapa_monedas = importar_csv_layout(level_data['monedas'])
            self.modenas_sprites = self.crear_grupo_tiles(mapa_monedas, 'monedas')

            mapa_moneda_plateada = importar_csv_layout(level_data['monedas_plateada'])
            self.modenas_plateadas_sprites = self.crear_grupo_tiles(mapa_moneda_plateada, 'monedas_plateada')

            mapa_enemigo = importar_csv_layout(level_data['enemigo'])
            self.enemigo_sprites = self.crear_grupo_tiles(mapa_enemigo, 'enemigo')

    def crear_grupo_tiles(self, layout, tipo):
        '''
        Crea los tiles 64x64 correspondiente en base al nivel, incluyendo al jugador, el terreno, monedas, enemigos etc. Utilizando imagenes png cargadas en otros directorios
        :param layout:
        :param tipo:
        :return:
        '''
        grupo_sprites = pygame.sprite.Group()

        for fila_index, fila in enumerate(layout):
            for columna_index, val in enumerate(fila):
                if self.level_actual == 0:
                    if val != '-1':
                        x = columna_index * tiles_tamaño
                        y = fila_index * tiles_tamaño

                        if tipo == 'terreno':
                            lista_mosaicos_terreno = importar_graficos('../graficos/terreno/fondoTerreno.png')
                            tile_superficie = lista_mosaicos_terreno[int(val)]
                            sprite = StaticTile(tiles_tamaño, x, y, tile_superficie)
                            grupo_sprites.add(sprite)

                        if tipo == 'monedas':
                            lista_mosaicos_monedas = importar_graficos('../graficos/monedas/Coins-PNG.png')
                            tile_superficie = lista_mosaicos_monedas[int(val)]
                            sprite = StaticTile(tiles_tamaño, x, y, tile_superficie)
                            grupo_sprites.add(sprite)

                        if tipo == 'monedas_plateada':
                            lista_mosaicos_monedas = importar_graficos('../graficos/monedas/monedas-plateadas.png')
                            tile_superficie = lista_mosaicos_monedas[int(val)]
                            sprite = StaticTile(tiles_tamaño, x, y, tile_superficie)
                            grupo_sprites.add(sprite)

                        if tipo == 'enemigo':
                            sprite = Enemigo(tiles_tamaño, x, y,'../graficos/enemigo/corriendo')

                            grupo_sprites.add(sprite)

                        # if tipo == 'reestricciones':
                        #     sprite = Tile(tiles_tamaño, x, y)

                if self.level_actual == 1:
                    if val != '-1':
                        x = columna_index * tiles_tamaño
                        y = fila_index * tiles_tamaño

                        if tipo == 'terreno':
                            lista_mosaicos_terreno = importar_graficos('../graficos/terreno/LV2.png')
                            tile_superficie = lista_mosaicos_terreno[int(val)]
                            sprite = StaticTile(tiles_tamaño, x, y, tile_superficie)
                            grupo_sprites.add(sprite)

                        if tipo == 'monedas_plateada':
                            lista_mosaicos_monedas = importar_graficos('../graficos/monedas/monedas-plateadas.png')
                            tile_superficie = lista_mosaicos_monedas[int(val)]
                            sprite = StaticTile(tiles_tamaño, x, y, tile_superficie)
                            grupo_sprites.add(sprite)

                        if tipo == 'monedas':
                            lista_mosaicos_monedas = importar_graficos('../graficos/monedas/Coins-PNG.png')
                            tile_superficie = lista_mosaicos_monedas[int(val)]
                            sprite = StaticTile(tiles_tamaño, x, y, tile_superficie)
                            grupo_sprites.add(sprite)

                        if tipo == 'lavax':
                            lista_mosaicos_terreno = importar_graficos('../graficos/terreno/lava2.jpg')
                            tile_superficie = lista_mosaicos_terreno[int(val)]
                            sprite = StaticTile(tiles_tamaño, x, y, tile_superficie)
                            grupo_sprites.add(sprite)

                        if tipo == 'enemigo':
                            sprite = Enemigo(tiles_tamaño, x, y,'../graficos/enemigo/volando')
                            grupo_sprites.add(sprite)

                if self.level_actual == 2:
                    if val != '-1':
                        x = columna_index * tiles_tamaño
                        y = fila_index * tiles_tamaño

                        if tipo == 'terreno':
                            lista_mosaicos_terreno = importar_graficos('../graficos/terreno/lv-2.png')
                            tile_superficie = lista_mosaicos_terreno[int(val)]
                            sprite = StaticTile(tiles_tamaño, x, y, tile_superficie)
                            grupo_sprites.add(sprite)

                        if tipo == 'monedas_plateada':
                            lista_mosaicos_monedas = importar_graficos('../graficos/monedas/monedas-plateadas.png')
                            tile_superficie = lista_mosaicos_monedas[int(val)]
                            sprite = StaticTile(tiles_tamaño, x, y, tile_superficie)
                            grupo_sprites.add(sprite)

                        if tipo == 'monedas':
                            lista_mosaicos_monedas = importar_graficos('../graficos/monedas/Coins-PNG.png')
                            tile_superficie = lista_mosaicos_monedas[int(val)]
                            sprite = StaticTile(tiles_tamaño, x, y, tile_superficie)
                            grupo_sprites.add(sprite)

                        if tipo == 'pinches':
                            lista_mosaicos_terreno = importar_graficos('../graficos/terreno/pinches.png')
                            tile_superficie = lista_mosaicos_terreno[int(val)]
                            sprite = StaticTile(tiles_tamaño, x, y, tile_superficie)
                            grupo_sprites.add(sprite)

                        if tipo == 'enemigo':
                            sprite = Enemigo(tiles_tamaño, x, y,'../graficos/enemigo/corriendo_nieve')
                            grupo_sprites.add(sprite)

                if self.level_actual == 3:
                    if val != '-1':
                        x = columna_index * tiles_tamaño
                        y = fila_index * tiles_tamaño

                        if tipo == 'terreno':
                            lista_mosaicos_terreno = importar_graficos('../graficos/terreno/lv3-tileset.png')
                            tile_superficie = lista_mosaicos_terreno[int(val)]
                            sprite = StaticTile(tiles_tamaño, x, y, tile_superficie)
                            grupo_sprites.add(sprite)

                        if tipo == 'monedas_plateada':
                            lista_mosaicos_monedas = importar_graficos(
                                '../graficos/monedas/monedas-plateadas.png')
                            tile_superficie = lista_mosaicos_monedas[int(val)]
                            sprite = StaticTile(tiles_tamaño, x, y, tile_superficie)
                            grupo_sprites.add(sprite)

                        if tipo == 'monedas':
                            lista_mosaicos_monedas = importar_graficos('../graficos/monedas/Coins-PNG.png')
                            tile_superficie = lista_mosaicos_monedas[int(val)]
                            sprite = StaticTile(tiles_tamaño, x, y, tile_superficie)
                            grupo_sprites.add(sprite)

                        if tipo == 'enemigo':
                            sprite = Enemigo(tiles_tamaño, x, y,'../graficos/enemigo/corriendo')
                            grupo_sprites.add(sprite)

                        if tipo == 'enemigo_2':
                            sprite = Enemigo(tiles_tamaño, x, y,'../graficos/enemigo/volando')
                            grupo_sprites.add(sprite)

                        if tipo == 'enemigo_3':
                            sprite = Enemigo(tiles_tamaño, x, y,'../graficos/enemigo/corriendo_nieve')
                            grupo_sprites.add(sprite)

        return grupo_sprites

    def scroll_x(self):
        '''
        Mueve la pantalla según la posición del jugador
        :return:
        '''
        player = self.player.sprite
        player_x = player.rect.centerx
        direccion_x = player.direction.x
        # print(player_x)
        # print(direccion_x)

        if player_x < ancho_pantalla / 4 and direccion_x < 0:
            self.mundo_shift = 8
            player.speed = 0
        elif player_x > ancho_pantalla - (ancho_pantalla / 4) and direccion_x > 0:
            self.movimiento_pantalla = True
            self.mundo_shift = -8
            player.speed = 0
        else:
            self.mundo_shift = 0
            player.speed = 8

    def calcular_desplazamiento_inicial(self):
        '''
        Calcula el desplazamiento inicial
        :return:
        '''
        player = self.player.sprite
        valor_inicial_sprite = player.posicion_inicial
        return valor_inicial_sprite

    def colission_enemigo(self):
        '''
        Detecta la colisión con sprites que representan a enemigos
        :return:
        '''
        player = self.player.sprite
        if pygame.sprite.spritecollide(player, self.enemigo_sprites, False):
            print("colisions")
            self.sonido_dolor.play()
            # player.cantidad_vidas -= 1
            self.vivo = False
            self.reiniciar_nivel()

    def colission_enemigo_2(self):
        colision_enemigos = pygame.sprite.spritecollide(self.player.sprite, self.enemigo_sprites, False)
        if colision_enemigos:
            for enemigo in colision_enemigos:
                enemigo_centro = enemigo.rect.centery
                enemigo_top = enemigo.rect.top
                player_bot = self.player.sprite.rect.bottom
                if enemigo_top < player_bot < enemigo_centro and self.player.sprite.direction.y >= 0:
                    self.sonido_dolor_enemigo.play()
                    enemigo.kill()
                else:
                    self.sonido_dolor.play()
                    # player.cantidad_vidas -= 1
                    self.vivo = False
                    self.reiniciar_nivel()

    def colission_terreno_hiriente_kava(self):
        '''
        Detecta la colisión con sprites que representa a lava en el lv 1
        :return:
        '''
        player = self.player.sprite
        if pygame.sprite.spritecollide(player, self.lava_sprites, False):
            self.sonido_dolor.play()
            # player.cantidad_vidas -= 1
            self.vivo = False
            self.reiniciar_nivel()

    def colission_terreno_hiriente_pinches(self):
        '''
        Detecta la colisión con Sprites que representan a los pinches del lv 2
        :return:
        '''
        player = self.player.sprite
        if pygame.sprite.spritecollide(player, self.pinches_sprites, False):
            self.sonido_dolor.play()
            # player.cantidad_vidas -= 1
            self.vivo = False
            self.reiniciar_nivel()

    def reiniciar_nivel(self):
        '''
        Reinicia el nivel
        :return:
        '''
        player = self.player.sprite
        self.terreno_sprites.draw(self.superficie_visualizacion)
        self.terreno_sprites.update(self.mundo_shift)
        self.player.sprite.rect.topleft = player.posicion_inicial


    def player_setup(self, layout):
        '''
        Genera el sprite que será el jugador
        :param layout:
        :return:
        '''
        for fila_index, fila in enumerate(layout):
            for columna_index, val in enumerate(fila):
                x = columna_index * tiles_tamaño
                y = fila_index * tiles_tamaño
                if val == '0':
                    sprite = Player((x, y), self.superficie_visualizacion)
                    self.player.add(sprite)
                if val == '1':
                    # REVISAR QUE HACER CON ESTO
                    algo_superficie = pygame.image.load('../graficos/character/inactivo/6.png').convert_alpha()
                    sprite = StaticTile(tiles_tamaño, x, y, algo_superficie)
                    self.goal.add(sprite)

    def horizontal_movement_colission(self):
        '''
        Maneja la colisión de movimiento horizontal entre los sprites
        :return:
        '''
        player = self.player.sprite
        player.colission_rectangulo.x += player.direction.x * player.speed
        for sprite in self.terreno_sprites.sprites():
            if sprite.rect.colliderect(player.colission_rectangulo):
                if player.direction.x < 0:
                    player.colission_rectangulo.left = sprite.rect.right
                    player.a_la_derecha = True
                    self.x_actual = player.rect.left
                elif player.direction.x > 0:
                    player.colission_rectangulo.right = sprite.rect.left
                    player.a_la_izquierda = True
                    self.x_actual = player.rect.right

        # if player.a_la_izquierda and (player.rect.left < self.x_actual or player.direction.x >= 0):
        #     player.a_la_izquierda = False
        # if player.a_la_derecha and (player.rect.right < self.x_actual or player.direction.x <= 0):
        #     player.a_la_derecha = False

    def vertical_movement_colission(self):
        '''
        Maneja la colisión de movimiento vertical entre los sprites
        :return:
        '''
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.terreno_sprites.sprites():
            if sprite.rect.colliderect(player.colission_rectangulo):
                # EN EL PISO
                if player.direction.y > 0:
                    player.colission_rectangulo.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.en_el_piso = True

                    # EN EL TECHO
                elif player.direction.y < 0:
                    player.colission_rectangulo.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.en_el_techo = True


        if player.en_el_piso and player.direction.y < 0 or player.direction.y > 1:
            player.en_el_piso = False
        # if player.en_el_techo and player.direction.y > 0:
        #     player.en_el_techo = False

    def enemigo_colission_reversa(self):
        '''
        Maneja la colisión de movimiento en reversa de los sprites que representan enemigos
        :return:
        '''
        for enemigo in self.enemigo_sprites.sprites():
            if pygame.sprite.spritecollide(enemigo, self.terreno_sprites, False):
                enemigo.reversa()


    def monedas_plateada_coliision(self):
        '''
        Maneja la colisión de movimiento horizontal entre los sprites que representan monedas plateadas
        :return:
        '''
        player = self.player.sprite
        colision_monedas = pygame.sprite.spritecollide(self.player.sprite, self.modenas_plateadas_sprites, True)
        contadorMonedas = 0
        if colision_monedas:
            self.sonido_moneda.play()
            self.cambiar_monedas += 1
            return 1

    def condicion_para_cambiar_de_nivel(self):
        '''
        Maneja la colisión al tocar el sprite que representa la moneda dorada que generará el cambio de nivel cuando player la colisione
        :return:
        '''
        retorno = False
        colision_monedas = pygame.sprite.spritecollide(self.player.sprite, self.modenas_sprites, True)
        if colision_monedas:
            self.sonido_lv_up.play()
            retorno = True
            return retorno

    def cambiar_monedas(self,cantidad):
        '''
        Actualiza la cantidad de monedas en la interfaz
        :param cantidad:
        :return:
        '''
        self.ui.monedas_plateadas_contador += cantidad

    def reproducir_sonido(self, lv_actual):

        '''
        Reproduce el sonido según el lv
        :param lv_actual:
        :return:
        '''
        match lv_actual:
            case 0:
                self.sonido_lv_0.play()
            case 1:
                self.sonido_lv_1.play()
            case 2:
                self.sonido_lv_2.play()

    def apagar_sonido(self, lv_actual):
        '''
        Apaga el sonido según el lv
        :param lv_actual:
        :return:
        '''
        match lv_actual:
            case 0:
                self.sonido_lv_0.stop()
            case 1:
                self.sonido_lv_1.stop()
            case 2:
                self.sonido_lv_2.stop()

    def reproducir_musica_aleatoria(self,momento_aleatorio,vivo,lv):
        '''
        Reproduce música en el tiempo aleatorio de un archivo .wav
        :param momento_aleatorio:
        :param vivo:
        :return:
        '''
        # Inicializar Pygame Mixer
        pygame.mixer.init()

        # Cargar y reproducir una canción
        # pygame.mixer.music.load('../sonido/level_0/onlymp3.to - TOP 7 MELHORES MUSICA DO JOGO MU ONLINE -X2oWmHD2hik-192k-1701208484.mp3')

        match lv:
            case 0:
                pygame.mixer.music.stop()
                pygame.mixer.music.load('../sonido/level_0/music-lv1.wav')
                pygame.mixer.music.play()
                pygame.mixer.music.set_pos(momento_aleatorio)
            case 1:
                pygame.mixer.music.stop()
                pygame.mixer.music.load('../sonido/level_0/Sonic-The-Hedgehog-OST-Marble-Zone.wav')
                pygame.mixer.music.play()
                pygame.mixer.music.set_pos(momento_aleatorio)
            case 2:
                pygame.mixer.music.stop()
                pygame.mixer.music.load('../sonido/level_0/music-lv3.wav')
                pygame.mixer.music.play()
                pygame.mixer.music.set_pos(momento_aleatorio)
            case 3:
                pygame.mixer.music.stop()
                pygame.mixer.music.load('../sonido/level_0/music-lv2.wav')
                pygame.mixer.music.play()
                pygame.mixer.music.set_pos(momento_aleatorio)

    def run(self):
        '''
        Función principal del juego
        :return:
        '''

        # TERRENO
        self.terreno_sprites.draw(self.superficie_visualizacion)
        self.terreno_sprites.update(self.mundo_shift)

        if hasattr(self, 'lava_sprites'):
            self.lava_sprites.draw(self.superficie_visualizacion)
            self.lava_sprites.update(self.mundo_shift)

        if hasattr(self,'pinches_sprites'):
            self.pinches_sprites.draw(self.superficie_visualizacion)
            self.pinches_sprites.update(self.mundo_shift)

        # LAVA
        # self.lava_sprites.draw(self.superficie_visualizacion)
        # self.lava_sprites.update(self.mundo_shift)

        # MONEDAS
        self.modenas_sprites.draw(self.superficie_visualizacion)
        self.modenas_sprites.update(self.mundo_shift)

        self.modenas_plateadas_sprites.draw(self.superficie_visualizacion)
        self.modenas_plateadas_sprites.update(self.mundo_shift)

        # ENEMIGO
        self.enemigo_sprites.update(self.mundo_shift)
        self.enemigo_colission_reversa()
        self.enemigo_sprites.draw(self.superficie_visualizacion)

        # self.reestricciones_sprites.update(self.mundo_shift)

        # PLAYER
        self.player.update()
        self.horizontal_movement_colission()
        self.vertical_movement_colission()
        self.scroll_x()
        self.player.draw(self.superficie_visualizacion)
        self.cambia_level = self.condicion_para_cambiar_de_nivel()
        self.monedas_plateada_coliision()
        self.ui.mostrar_monedas(self.cambiar_monedas)
        # self.colission_enemigo()
        self.colission_enemigo_2()

        if hasattr(self, 'lava_sprites'):
            self.colission_terreno_hiriente_kava()

        if hasattr(self, 'pinches_sprites'):
            self.colission_terreno_hiriente_pinches()

        pass
