import random
import clases

ORDEN_ESPECIAL = False

def tirar_dados():

    dados = (random.randint(1,6)) + (random.randint(1,6))
    
    return (dados)

def rellenar_tablero(tablero):
    
    recursos = ["Ladrillo", "Ladrillo", "Ladrillo", "Piedra", "Piedra", "Piedra", "Trigo", "Trigo", "Trigo", "Trigo", "Lana", "Lana", "Lana", "Lana", "Madera", "Madera", "Madera", "Madera"]
    numeros = [2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12]

    random.shuffle(recursos)
    random.shuffle(numeros)
    rec_num = []

    for i in range (19):
        if (i != 9 and i != 18):
            recurso = recursos[i]
            tablero.colocar_recurso(i+1,recurso)

            numero = numeros[i]
            tablero.colocar_numero(i+1,numero)

        if (i == 18):
            recurso = recursos[9]
            tablero.colocar_recurso(i+1,recurso)

            numero = numeros[9]
            tablero.colocar_numero(i+1,numero)

def dar_recursos(dados, tablero):
    for i in range (1, 20):
        if (tablero.obtener_numero_de_ficha(i) == dados):
            for k in range (1,7):
                if not (tablero.obtener_asentamiento(i,k)) == None:
                    rec = tablero.obtener_recurso_de_ficha(i)
                    jug = tablero.obtener_asentamiento(i,k).jugador
                    jug.agregar_recurso(rec)

def jugar_catan(jugadores,tablero):
    for i in range (len(jugadores)):
        primer_asentamiento = input("Coloque primer asentamiento:").split(" ")
        tablero.colocar_asentamiento(int(primer_asentamiento[0]),int(primer_asentamiento[1]),clases.Asentamiento(jugadores[i]))

        primer_camino = input("Coloque primer camino:").split(" ")
        tablero.colocar_camino(int(primer_camino[0]),int(primer_camino[1]),clases.Camino(jugadores[i]))

        segundo_asentamiento = input("Coloque segundo asentamiento:").split(" ")
        tablero.colocar_asentamiento(int(segundo_asentamiento[0]),int(segundo_asentamiento[1]),clases.Asentamiento(jugadores[i]))
        
        segundo_camino = input("Coloque segundo camino:").split(" ")
        tablero.colocar_camino(int(segundo_camino[0]),int(segundo_camino[1]),clases.Camino(jugadores[i]))

    jugando = True
    
    while (jugando):
        for i in range (len(jugadores)):
            dados = tirar_dados()
            print (dados)
            dar_recursos(dados,tablero)
            comm = input("Ingrese comando: ")
            comm = comm.split(" ")
            if (comm[0] == "fin"):
                jugando = False
                break
            if (comm[0] == "pas"):
                pass
            if (comm[0] == "ase"):
                tablero.colocar_asentamiento(int(comm[1]), int(comm[2]), clases.Asentamiento(jugadores[i]))
            if (comm[0] == "cam"):
                tablero.colocar_camino(int(comm[1]), int(comm[2]), clases.Camino(jugadores[i]))
    
        #python -m pytest tests.py::TestInicio