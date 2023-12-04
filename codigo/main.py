import codigo.bdd
from settings import *
from level import Level
from data_juego import level_0, level_1, level_2, level_3
from UI import *
from menu import *
from bdd import crear_db, insertar_jugador
import random

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((ancho_pantalla, altura_pantalla))
clock = pygame.time.Clock()
nombre_jugador = None
# level = Level(level_0,screen)
# sonido_activado = True
menu = main_menu(Menu)

duracion_cancion = 1500
momento_aleatorio = random.randint(0, duracion_cancion)

if menu is not None:
    crear_db()
    level_actual = 0
    levels = [level_0, level_1, level_2, level_3]
    level = Level(levels[level_actual], screen, level_actual)
    ui = UI(screen)

    if menu.sonido_activado:
        duracion_cancion = 10
        momento_aleatorio = random.randint(0, duracion_cancion)
        if menu.sonido_activado:
            level.reproducir_musica_aleatoria(momento_aleatorio, level.vivo,level_actual)

    while True:
        if not level.vivo:
            duracion_cancion = 1
            momento_aleatorio = random.randint(0, duracion_cancion)
            level = Level(levels[level_actual], screen, level_actual)
            if menu.sonido_activado:
                level.reproducir_musica_aleatoria(momento_aleatorio, level.vivo, level_actual)
            level.vivo = True
            level = Level(levels[level_actual], screen, level_actual)
            level.cambia_level = False


        if level.cambia_level:
            pygame.mixer.music.stop()
            momento_aleatorio = random.randint(0, duracion_cancion)
            level_actual += 1
            if menu.sonido_activado:
                level.reproducir_musica_aleatoria(momento_aleatorio, level.vivo, level_actual)
            cantidad_monedas =+ level.cantidad_monedas
            if level_actual >= len(levels):
                mostrar_puntuaciones(screen)
                break
                # current_level_index = 0

            level = Level(levels[level_actual], screen,level_actual)
            level.cambia_level = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                tiempo_transcurrido = pygame.time.get_ticks()
                tiempo_en_segundos = tiempo_transcurrido // 1000  # Convertir a segundos

                horas = tiempo_en_segundos // 3600
                minutos = (tiempo_en_segundos % 3600) // 60
                segundos = tiempo_en_segundos % 60

                tiempo_total = f"{horas:02}:{minutos:02}:{segundos:02}"
                insertar_jugador(menu.nombre_jugador,level_actual,tiempo_total)
                pygame.quit()
                mostrar_puntuaciones(screen)
                sys.exit()

        match level_actual:
            case 0:
                ui.mostrar_monedas(level.cambiar_monedas)
                fondo = pygame.image.load('../graficos/terreno/lv-0-fondo.png').convert()
                screen.blit(fondo, (0, 0))
            case 1:
                ui.mostrar_monedas(level.cambiar_monedas)
                fondo = pygame.image.load('../graficos/terreno/infierno.jpg').convert()
                screen.blit(fondo,(0,0))
                # screen.fill((0, 0, 0))
            case 2:
                ui.mostrar_monedas(level.cambiar_monedas)
                screen.fill((14, 22, 51))
            case 3:
                ui.mostrar_monedas(level.cambiar_monedas)
                screen.fill((14, 22, 51))


        if level.cambia_level:
            level.cambia_level = level.condicion_para_cambiar_de_nivel()
        level.run()
        pygame.display.update()
        clock.tick(60)
