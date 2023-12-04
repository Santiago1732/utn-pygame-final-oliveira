import sqlite3

def crear_db():
    '''
    Se conecta a la base de datos y ejecuta una query para crear una tabla.
    :return:
    '''
    try:
        conexion = sqlite3.connect("../base_de_datos/database.db")
        cursor = conexion.cursor()
        # Crear una única tabla jugador con dos columnas: nombre y lv
        cursor.execute("CREATE TABLE jugador (nombre VARCHAR(50), lv VARCHAR(50), tiempo_total VARCHAR(50))")
        conexion.commit()
    except Exception as ex:
        print(ex)
    finally:
        if conexion:
            conexion.close()

def insertar_jugador(nombre_jugador, current_level_index,tiempo_total):
    '''
    Ejecuta una query para insertar datos que llegan por parametro en una tabla
    :param nombre_jugador:
    :param current_level_index:
    :param tiempo_total:
    :return:
    '''
    try:
        conexion = sqlite3.connect("../base_de_datos/database.db")
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO jugador (nombre, lv, tiempo_total) VALUES (?, ?, ?)", (nombre_jugador, current_level_index,tiempo_total))
        conexion.commit()
    except Exception as ex:
        print(ex)
    finally:
        if conexion:
            conexion.close()





