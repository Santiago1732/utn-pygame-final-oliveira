import pygame
import sys
from bdd import *
import boton

class Menu():
    def __init__(self, nombre_jugador, sonido_activado):
        super().__init__()
        self.nombre_jugador = nombre_jugador
        self.sonido_activado = sonido_activado

# Inicializar Pygame
pygame.init()

# Configuraciones de la ventana
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Santiago Oliveira - UTN - TP Pygame ')
# fondo = pygame.image.load('../graficos/terreno/lv-0-fondo.png').convert()
# screen.blit(fondo, (0, 0))3

# Colores

pygame.display.set_caption("MENU PRINCIPAL")
#game variables
font = pygame.font.SysFont("arialblack", 40)
# MENU NUEVO
#load button images
jugar = pygame.image.load("../imagenes/JUGAR.jpg").convert_alpha()
opciones= pygame.image.load("../imagenes/OPCIONES.jpg").convert_alpha()
salir = pygame.image.load("../imagenes/SALIR.jpg").convert_alpha()
audio_activar = pygame.image.load('../imagenes/ACTIVAR.jpg').convert_alpha()
audio_desactivar = pygame.image.load('../imagenes/DESACTIVAR.jpg').convert_alpha()
atras = pygame.image.load('../imagenes/ATRAS.jpg').convert_alpha()
ingresar_jugador = pygame.image.load('../imagenes/INGRESE_SU_NOMBRE.jpg').convert_alpha()
atras_juego = pygame.image.load('../imagenes/ATRAS.jpg').convert_alpha()
BLACK = (0, 0, 0)

#create button instances
jugar = boton.Button(400, 150, jugar, 1)
opciones = boton.Button(400, 250, opciones, 1)
salir = boton.Button(400, 350, salir, 1)
audio_activar = boton.Button(400, 150, audio_activar, 1)
audio_desactivar = boton.Button(400, 150, audio_desactivar, 1)
atras = boton.Button(400, 350, atras, 1)
ingresar_jugador = boton.Button(400, 150, ingresar_jugador, 1)
atras_juego = boton.Button(400, 250, atras_juego, 1)
pygame.mixer.music.load('../sonido/level_0/music-lv1.wav')
sonido_activado = True

if sonido_activado:
    pygame.mixer.music.play()

    def main_menu(self):
        game_paused = False
        menu_state = "menu_principal"
        '''
        Representa el menú principal del juego. Muestra opciones como jugar, opciones y salir, y maneja las acciones del usuario en el menú.
        :param self:
        :return:
        '''
        menu = Menu('None',True)
        sonido_activado = True
        nombre_jugador = ''
        estado = "menu_principal"
        while True:
            fondo = pygame.image.load('../graficos/terreno/fondo-menu.png').convert()
            screen.blit(fondo, (0, 0))
            # check if game is paused


            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    match event.key:
                        # NOMBRE JUGADOR
                        case pygame.K_1:
                            menu.nombre_jugador = input_text()
                            return menu

                        # OPCIONES
                        case pygame.K_2:
                            menu.sonido_activado = pantalla_de_opciones()
                            break

                        # SALIR
                        case pygame.K_3:
                            pygame.quit()
                            sys.exit()


            if estado == "menu_principal":
                jugar.draw(screen)
                opciones.draw(screen)
                salir.draw(screen)

            if game_paused == True:
                opciones.draw(screen)


                # if menu_state == "ingresar_jugador":
                #     image = pygame.image.load('../imagenes/INGRESE_SU_NOMBRE.jpg')
                #     screen.blit(image, (350, 150))
                #     player_name = text_input()
                #     if salir.draw(screen):
                #         menu_state = "salir"



            # event handler
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_paused = True
                if event.type == pygame.QUIT:
                    run = False

            pygame.display.update()


    def pantalla_de_juego(self, sonido_activado = True):
        '''
         Esta función representa la pantalla del juego y permite al jugador ingresar su nombre. Devuelve el nombre del jugador.
        :param self:
        :param sonido_activado:
        :return:
        '''
        running = True
        while running:
            screen.fill(WHITE)
            player_name = text_input()

            if player_name is not None:
                return player_name

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.nombre_jugador = pantalla_de_juego(sonido_activado)
                        pygame.display.update()

    def pantalla_de_opciones():
        '''
        representa la pantalla de opciones donde el jugador puede activar o desactivar el sonido y volver al menú principal.
        :return:
        '''
        global sonido_activado  # Usar la variable global

            # atras.draw(screen)


        while True:
            if sonido_activado:
                audio_desactivar.draw(screen)
            else:
                audio_activar.draw(screen)
            atras.draw(screen)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        sonido_activado = not sonido_activado

                        if not sonido_activado:
                            pygame.mixer.music.stop()
                        else:
                            pygame.mixer.music.load('../sonido/level_0/music-lv1.wav')
                            pygame.mixer.music.play()



                    elif event.key == pygame.K_2:
                        return sonido_activado

            pygame.display.update()


    def input_text():
        font = pygame.font.Font(None, 56)
        input_string = ""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return input_string
                    elif event.key == pygame.K_BACKSPACE:
                        input_string = input_string[:-1]
                    else:
                        input_string += event.unicode

            fondo = pygame.image.load('../graficos/terreno/FONDO_INGRESE_SU_NOMBRE.png').convert()
            screen.blit(fondo, (0, 0))
            text_surface = font.render(input_string, True, BLACK)
            screen.blit(text_surface, (695, 165))
            # text_surface = font.render(input_string, True, (0, 0, 0))
            # screen.blit(text_surface, (10, 10))
            pygame.display.flip()

        return input_string




    def dibujar_texto(text, font, color, surface, x, y):
        '''
        dibuja texto en una superficie Pygame con la fuente, color y posición especificados.
        :param text:
        :param font:
        :param color:
        :param surface:
        :param x:
        :param y:
        :return:
        '''
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)


    def mostrar_puntuaciones(screen):
        '''
        muestra las puntuaciones de los jugadores guardades en una base de datos ventana.
        :param screen:
        :return:
        '''
        conn = sqlite3.connect('../base_de_datos/database.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM jugador")
        column_names = [description[0] for description in cursor.description]
        rows = cursor.fetchall()

        pygame.init()
        screen = pygame.display.set_mode((800, 600))

        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        font = pygame.font.SysFont('../graficos/fuentes/HOLIDAYZONE.ttf',24)

        screen.fill(BLACK)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill((0, 0, 0))
            y = 0

            column_text = '     |   '.join(column_names)
            text_surface = font.render(column_text, True, WHITE)
            screen.blit(text_surface, (50, y))
            y += 60  # Ajusta la posición y para la primera fila de datos

            for row in rows:
                cleaned_row = [str(item).strip("('')") for item in row]
                text = font.render(', '.join(cleaned_row), True, WHITE)
                screen.blit(text, (100, y))
                y += 30

            pygame.display.flip()

        pygame.quit()


    # Bucle principal
    def main():
        while True:
            main_menu()

    if __name__ == '__main__':
        main()