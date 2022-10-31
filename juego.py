import random
import clases

ORDEN_ESPECIAL = True
list_fichas = {}


def tirar_dados():

    dados = (random.randint(1,6)) + (random.randint(1,6))
    
    return (dados)

def seisochos(tablero, num):
    adys = []
    so = False
    for arista in list_fichas[num]:
        for pos, aris in list_fichas.items():
            if arista in aris and pos != num:
                adys.append(pos)
    
    for ady in adys:
        if tablero.obtener_numero_de_ficha(ady) == 6 or tablero.obtener_numero_de_ficha(ady) == 8:
            so = True

    return so    

def rellenar_tablero(tablero):
    
    recursos = ["Ladrillo", "Ladrillo", "Ladrillo", "Piedra", "Piedra", "Piedra", "Trigo", "Trigo", "Trigo", "Trigo", "Lana", "Lana", "Lana", "Lana", "Madera", "Madera", "Madera", "Madera"]
    numeros = [2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12]

    random.shuffle(recursos)
    random.shuffle(numeros)
    rec_num = []


    for n in range(1, 20):
        list_fichas[n] = []
        for ñ in range(1, 7):
            list_fichas[n].append(tablero.obtener_arista(n, ñ)) #creo q esta sintaxis esta mal pero algo asj hay q hacer


    for i in range(19):
        if (i != 9 and i != 18):
            recurso = recursos[i]
            tablero.colocar_recurso(i+1,recurso)

            numero = numeros[i]
            if numero != 6 and numero != 8:
                tablero.colocar_numero(i+1,numero)
            if numero == 6 or numero == 8:
                if not seisochos(tablero, numero):
                    tablero.colocar_numero(i+1,numero)
                else:
                    finded = False
                    for b in range(1, i+1):
                        numb = tablero.obtener_numero_de_ficha(b)
                        if seisochos(tablero, b) == False and numb != 6 and numb != 8:
                            tablero.colocar_numero(i+1,numb)
                            tablero.colocar_numero(b, numero)
                            finded = True
                    if not finded:
                        if len(numeros) > i+1 and numeros[i+1] != 6 and numeros[i+1] != 8:
                            tablero.colocar_numero(i+1, numeros[i+1])
                            numeros[i+1] = numero
                        elif len(numeros) > i+2 and numeros[i+2] != 6 and numeros[i+2] != 8:
                            tablero.colocar_numero(i+1, numeros[i+2])
                            numeros[i+2] = numero
                        elif len(numeros) > i+3 and numeros[i+3] != 6 and numeros[i+3] != 8:
                            tablero.colocar_numero(i+1, numeros[i+3])
                            numeros[i+3] = numero

        if (i == 18):
            recurso = recursos[9]
            tablero.colocar_recurso(i+1,recurso)

            numero = numeros[9]
            if numero != 6 and numero != 8:
                tablero.colocar_numero(i+1,numero)
            if numero == 6 or numero == 8:
                if not seisochos(tablero, numero):
                    tablero.colocar_numero(i+1,numero)
                else:
                    finded = False
                    for b in range(1, i+1):
                        numb = tablero.obtener_numero_de_ficha(b)
                        if seisochos(tablero, b) == False and numb != 6 and numb != 8:
                            tablero.colocar_numero(i+1,numb)
                            tablero.colocar_numero(b, numero)
                            finded = True
                    if not finded:
                        if len(numeros) > i+1 and numeros[i+1] != 6 and numeros[i+1] != 8:
                            tablero.colocar_numero(i+1, numeros[i+1])
                            numeros[i+1] = numero
                        elif len(numeros) > i+2 and numeros[i+2] != 6 and numeros[i+2] != 8:
                            tablero.colocar_numero(i+1, numeros[i+2])
                            numeros[i+2] = numero
                        elif len(numeros) > i+3 and numeros[i+3] != 6 and numeros[i+3] != 8:
                            tablero.colocar_numero(i+1, numeros[i+3])
                            numeros[i+3] = numero

        if tablero.obtener_numero_de_ficha(10) != "":
            if not seisochos(tablero, 19): 
                tablero.colocar_numero(19, tablero.obtener_numero_de_ficha(10)) 
            elif not seisochos(tablero, 18):
                tablero.colocar_numero(18, tablero.obtener_numero_de_ficha(10)) 
            elif not seisochos(tablero, 17):
                tablero.colocar_numero(17, tablero.obtener_numero_de_ficha(10)) 
            elif not seisochos(tablero, 16):
                tablero.colocar_numero(16, tablero.obtener_numero_de_ficha(10)) 
            elif not seisochos(tablero, 15):
                tablero.colocar_numero(15, tablero.obtener_numero_de_ficha(10)) 
            elif not seisochos(tablero, 14):
                tablero.colocar_numero(14, tablero.obtener_numero_de_ficha(10)) 
            tablero.colocar_numero(10, "")
        
    fichas_keys = {
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        8: 0,
        9: 0,
        10: 0,
        11: 0,
        12: 0
    }
    missing_key = []
    extra_key = []

    for h in range(1, 20):
        print(f'ficha:{h} numero:{tablero.obtener_numero_de_ficha(h)}')

    print('_____________________________________________')

    for j in range(1, 20):
        if j != 10:
            if tablero.obtener_numero_de_ficha(j) == "" or tablero.obtener_numero_de_ficha(j) == 0:
                tablero.colocar_numero(j, 2)
                fichas_keys[tablero.obtener_numero_de_ficha(j)]+=1
                print(j)
            else: 
                #print(f"El keyerror es: {tablero.obtener_numero_de_ficha(j)}; j: {j}")
                fichas_keys[tablero.obtener_numero_de_ficha(j)]+=1
            
    #print(fichas_keys)
    

    for key, value in fichas_keys.items():
        if key in range(3, 12) and (value == 1 or value == 0):
            if value == 1:
                missing_key.append(key)
            elif value == 0:
                missing_key.append(key)
                missing_key.append(key)
        if key in range(3, 12) and value >= 3:
            for e in range(2, value):
                extra_key.append(key)
        if (key == 2 and value == 0) or (key == 12 and value == 0):
            print("lol")
            missing_key.append(key)
        #if key == 2:
            #print(value)
        if (key == 2 and value >= 2) or (key == 12 and value >= 2):
            #print("Hay un dos")
            for e in range(1, value):
                extra_key.append(key)


    print(missing_key)
    print(extra_key)

    pos_ficha = {}
    for p in range(1, 20):
        pos_ficha[p] = tablero.obtener_numero_de_ficha(p)

    for posicion, ficha in pos_ficha.items():
        if ficha in extra_key:
            tablero.colocar_numero(posicion, missing_key[0])
            missing_key.pop(0)
            extra_key.remove(ficha)

    

    for d in range(1, 20):
        if tablero.obtener_numero_de_ficha(d) == 6 or tablero.obtener_numero_de_ficha(d) == 8:
            if seisochos(tablero, d):
                print('error?')

    if tablero.obtener_numero_de_ficha(10) != '':
        for u in range(1 ,20):
            if tablero.obtener_numero_de_ficha(u) == '':
                num_swapped = tablero.obtener_numero_de_ficha(10)
                tablero.colocar_numero(10, '')
                tablero.colocar_numero(u, num_swapped)
                u=21
    

    for d in range(1, 20):
        if tablero.obtener_numero_de_ficha(d) == 6 or tablero.obtener_numero_de_ficha(d) == 8:
            if seisochos(tablero, d):
                for y in range(1, 20):
                    if y != 10:
                        if tablero.obtener_numero_de_ficha(y) != 6 and tablero.obtener_numero_de_ficha(y) != 8:
                            if not seisochos(tablero, y):
                                nam = tablero.obtener_numero_de_ficha(d)
                                tablero.colocar_numero(d, tablero.obtener_numero_de_ficha(y))
                                tablero.colocar_numero(y, nam)
                                y = 21


   #prueba si hay error
    for d in range(1, 20):
        if tablero.obtener_numero_de_ficha(d) == 6 or tablero.obtener_numero_de_ficha(d) == 8:
            if seisochos(tablero, d):
                print('error :(')
                pruebadeerror


    
    for h in range(1, 20):
        print(f'ficha:{h} numero:{tablero.obtener_numero_de_ficha(h)}')
    
    a

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
    jugadores.reverse()
    for i in range(len(jugadores)):
        segundo_asentamiento = input("Coloque segundo asentamiento:").split(" ")
        tablero.colocar_asentamiento(int(segundo_asentamiento[0]),int(segundo_asentamiento[1]),clases.Asentamiento(jugadores[i]))
        
        segundo_camino = input("Coloque segundo camino:").split(" ")
        tablero.colocar_camino(int(segundo_camino[0]),int(segundo_camino[1]),clases.Camino(jugadores[i]))
    jugadores.reverse()#extra 1

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