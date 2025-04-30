class Nivel:
    def __init__(self, id, nombre, tematica, mecanica_clave, dificultad, variaciones):
        self.id = id
        self.nombre = nombre
        self.tematica = tematica
        self.mecanica_clave = mecanica_clave
        self.dificultad = dificultad
        self.variaciones = variaciones

    def mostrar_info(self):
        print(f"Nivel {self.id}: {self.nombre}")
        print(f"  Temática: {self.tematica}")
        print(f"  Mecánica clave: {self.mecanica_clave}")
        print(f"  Dificultad: {self.dificultad}")
        print(f"  Variaciones: {self.variaciones}")
        print("-" * 40)

# Lista de niveles predefinidos para Nexus
niveles = [
    Nivel(1, "Nexo Aurora", "Ruinas flotantes", "Plataformas móviles simples", "Baja", "Introducción a salto y combate"),
    Nivel(2, "Nexo Obscura", "Minas subterráneas", "Paredes destructibles", "Media-baja", "Enemigos que aparecen y desaparecen"),
    Nivel(3, "Nexo Fractal", "Bosque espejado", "Ramas reflejadas con espejos", "Media", "Uso intensivo del Nexo-Shift"),
    Nivel(4, "Nexo Corrosión", "Ciudad mecánica", "Zonas corrosivas con daño por tiempo", "Media-alta", "Cronómetro activo y obstáculos letales"),
    Nivel(5, "Nexo Umbral", "Vértice dimensional", "Cambio simultáneo entre dos realidades", "Alta", "Puzzles multicapas y jefes gemelos"),
    Nivel(6, "El Gran Vacío", "Epicentro final", "Arena abierta con fases de jefe", "Épica", "Combate en tres fases con moral final")
]

# Mostrar información de todos los niveles
for nivel in niveles:
    nivel.mostrar_info()