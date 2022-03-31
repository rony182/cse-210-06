from game.casting.color import Color

# ------------------------------
# GENERAL GAME CONSTANTS
# ------------------------------

# TITLE
GAME_NAME = "Zombie Invasion"
FRAME_RATE = 20

# SCREEN
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 880
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 70
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONT_FILE = "assets\\fonts\\SkullAttack.ttf"
FONT_SMALL = 32
FONT_LARGE = 50

# SOUND
BACKGROUND_MENU= "assets\\sounds\\mixkit-piano-horror.mp3"
SHOT_SOUND = "assets\\sounds\\shot.mp3"
ZOMBIE_GROUP_SOUND = "assets\\sounds\\group_of_zombies.mp3"
ZOMBIE_ATTACK_SOUND = "assets\\sounds\\zombie_attack.mp3"
WELCOME_SOUND = "assets\\sounds\\start.wav"
OVER_SOUND = "assets\\sounds\\over.wav"
BACKGROUND_SOUND = "assets\\sounds\\back_sound.mp3"
IMPACT_SOUND = "assets\\sounds\\mixkit-bullet-impact.wav"
BULLET_MISSED_TARGET = "assets\\sounds\\mixkit-wizard-fire-woosh.wav"

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0,0,0)
WHITE = Color(255,255,255)
BLUE = Color(0,0,255)
GREEN = Color(0,255,0)
YELLOW = Color(255, 255, 0)

# KEYS
LEFT = "left"
RIGHT = "right"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"

# SCENES
NEW_GAME = 0
HOW_TO_PLAY = 1
PLAYER_SELECTION = 2
IN_PLAY = 3
YOU_WIN = 4
GAME_OVER = 5


# -----------------------
# SCRIPTING CONSTANTS
# -----------------------

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# -----------------------
# CASTING CONSTANTS
# -----------------------

# STATS
STATS_GROUP = "stats"
DEFAULT_LIVES = 3


# HUD
SCORE_MARGIN = 20
LIVES_MARGIN = 875
HUD_MARGIN = 20
LIVES_GROUP = "lives"
SCORE_GROUP = "score"
LIVES_FORMAT = "LIVES {}"
SCORE_FORMAT = "SCORE {}"

# BULLET
BULLET_GROUP = "ammo"
BULLET_IMAGE = "assets\\images\\bullet.png"
BULLET_WIDTH = 6
BULLET_HEIGHT = 6
BULLET_VELOCITY = 6
BULLET_QUANTITY = 30


# PLAYER
PLAYER_GROUP = "player"
PLAYER_IMAGES = [f"zombie_invasion\\assets\\images\\player_{n}_30px.png" for n in range(1, 5)]
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 75
PLAYER_RATE = 60
PLAYER_VELOCITY = 7

# ZOMBIES
ZOMBIE_MAX_NUMBER = 10
ZOMBIE_VELOCITY = 1
ZOMBIE_GROUP = "zombies"
ZOMBIE_IMAGES = [f"zombie_invasion\\assets\\images\\zombie_{i}_30px.png" for i in range(1, 5)]
ZOMBIE_WIDTH = 50
ZOMBIE_HEIGHT = 75
ZOMBIE_POINTS = 5

# PLAYER SPRITES
SPRITES_GROUP = "sprites"
PLAYER_IMAGES_BIG = [f"zombie_invasion\\assets\\images\\player_{n}.png" for n in range(1, 5)]
SPRITE_WIDTH = 200
SPRITE_HEIGHT = 352

# DIALOG
DIALOG_GROUP = "dialogs"
GAME_START = "START"
GAME_HELP = "HELP"
WAS_GOOD_GAME = "GAME OVER"