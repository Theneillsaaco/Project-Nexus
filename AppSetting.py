"""AppSetting.py"""

# Nombre del juego
GAMENAME = "Proyecto Nexus"

# Tamaño de la pantalla
DISPLAYRADIO = 1280, 720

# Tiempo donde eres inmune
INVULNERABLETIMER = 1.5

# Velocidad de Movimiento
VELOCITYHORIZONTAL = 200
VELOCITYVERTICAL = -600

# Gravedad
GRAVETY = 1000

# Cuadro de combate
BATTLE_BOX_WIDTH = 300
BATTLE_BOX_HEIGHT = 150
BATTLE_BOX_X = (DISPLAYRADIO[0] - BATTLE_BOX_WIDTH) // 2
BATTLE_BOX_Y = (DISPLAYRADIO[1] - BATTLE_BOX_HEIGHT) // 2

# Jugador
PLAYER_SIZE = 20
PLAYER_MAX_HEALTH = 100

# Enemigo Slime
ENEMYSLIME_DAMAGE = 10