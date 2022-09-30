from interfaz import jugar_con_interfaz
from juego import rellenar_tablero
from tablero import TableroCatan
#Lista de jugadores
jugadores = []
#Tablero
tablero_a_jugar = TableroCatan
rellenar_tablero()
#No se olviden de rellenar el tablero!
jugar_con_interfaz(jugadores,tablero_a_jugar)