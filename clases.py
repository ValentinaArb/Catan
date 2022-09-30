class Asentamiento:
    def __init__ (self, jugador):
        self.jugador = jugador

class Ciudad:
    pass

class Camino:
     def __init__ (self, jugador):
        self.jugador = jugador

class Jugador:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color
        self.ladrillo = 0
        self.piedra = 0
        self.trigo = 0
        self.lana = 0
        self.madera = 0
    
    def agregar_recurso(self, recurso):
        if (recurso == "Ladrillo"):
            self.ladrillo = self.ladrillo +1
        if (recurso == "Piedra"):
            self.piedra = self.piedra +1
        if (recurso == "Trigo"):
            self.trigo = self.trigo +1
        if (recurso == "Lana"):
            self.lana = self.lana +1
        if (recurso == "Madera"):
            self.madera = self.madera +1

    def cantidad_de(self, recurso):
        if (recurso == "Ladrillo"):
            return self.ladrillo
        if (recurso == "Piedra"):
            return self.piedra
        if (recurso == "Trigo"):
            return self.trigo
        if (recurso == "Lana"):
            return self.lana
        if (recurso == "Madera"):
            return self.madera