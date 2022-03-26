import csv
from constants import *
from game.casting.animation import Animation
from game.casting.body import Body
from game.casting.zombie import Zombie
from game.casting.image import Image
from game.casting.label import Label
from game.casting.point import Point
from game.casting.stats import Stats
from game.casting.text import Text 
from game.scripting.change_scene_action import ChangeSceneAction
from game.scripting.check_over_action import CheckOverAction
from game.scripting.collide_borders_action import CollideBordersAction
from game.scripting.collide_zombie_action import CollideZombieAction
from game.scripting.draw_bullet_action import DrawBulletAction
from game.scripting.draw_player_action import DrawPlayerAction
from game.scripting.draw_zombies_action import DrawZombiesAction
from game.scripting.draw_dialog_action import DrawDialogAction
from game.scripting.draw_hud_action import DrawHudAction
from game.scripting.end_drawing_action import EndDrawingAction
from game.scripting.initialize_devices_action import InitializeDevicesAction
from game.scripting.load_assets_action import LoadAssetsAction
from game.scripting.move_bullet_action import MoveBulletAction
from game.scripting.move_player_action import MovePlayerAction
from game.scripting.move_zombie_action import MoveZombieAction
from game.scripting.play_sound_action import PlaySoundAction
from game.scripting.release_devices_action import ReleaseDevicesAction
from game.scripting.start_drawing_action import StartDrawingAction
from game.scripting.timed_change_scene_action import TimedChangeSceneAction
from game.scripting.unload_assets_action import UnloadAssetsAction
from game.services.raylib.raylib_audio_service import RaylibAudioService
from game.services.raylib.raylib_keyboard_service import RaylibKeyboardService
from game.services.raylib.raylib_physics_service import RaylibPhysicsService
from game.services.raylib.raylib_video_service import RaylibVideoService


class SceneManager:
    """The person in charge of setting up the cast and script for each scene."""
    
    AUDIO_SERVICE = RaylibAudioService()
    KEYBOARD_SERVICE = RaylibKeyboardService()
    PHYSICS_SERVICE = RaylibPhysicsService()
    VIDEO_SERVICE = RaylibVideoService(GAME_NAME, SCREEN_WIDTH, SCREEN_HEIGHT)

    CHECK_OVER_ACTION = CheckOverAction()
    COLLIDE_BORDERS_ACTION = CollideBordersAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    COLLIDE_ZOMBIE_ACTION = CollideZombieAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    DRAW_BULLET_ACTION = DrawBulletAction(VIDEO_SERVICE)
    DRAW_ZOMBIES_ACTION = DrawZombiesAction(VIDEO_SERVICE)
    DRAW_DIALOG_ACTION = DrawDialogAction(VIDEO_SERVICE)
    DRAW_HUD_ACTION = DrawHudAction(VIDEO_SERVICE)
    DRAW_PLAYER_ACTION= DrawPlayerAction(VIDEO_SERVICE)
    END_DRAWING_ACTION = EndDrawingAction(VIDEO_SERVICE)
    INITIALIZE_DEVICES_ACTION = InitializeDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    LOAD_ASSETS_ACTION = LoadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)
    MOVE_BULLET_ACTION = MoveBulletAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    MOVE_PLAYER_ACTION = MovePlayerAction()
    RELEASE_DEVICES_ACTION = ReleaseDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    START_DRAWING_ACTION = StartDrawingAction(VIDEO_SERVICE)
    UNLOAD_ASSETS_ACTION = UnloadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)

    # -----------------------
    # SCENE CONSTANTS
    # -----------------------

    # NEW GAME SCENE
    GAME_NAME = "Zombie Invasion"
    START_GAME = "Press ENTER to play"
    HOW_TO_PLAY = "Press H for help"

    def __init__(self):
        pass

    def prepare_scene(self, scene, cast, script):
        if scene == NEW_GAME:
            self._prepare_new_game(cast, script)
        elif scene == HOW_TO_PLAY:
             self._prepare_how_to_play(cast, script)
        elif scene == PLAYER_SELECTION:
            self._prepare_player_selection(script)
        elif scene == IN_PLAY:
            self._prepare_in_play(cast, script)
        elif scene == YOU_WIN:
            self._prepare_you_win(cast, script)
        elif scene == GAME_OVER:    
            self._prepare_game_over(cast, script)
    
    # ----------------------------------------------------------------------------------------------
    # scene methods
    # ----------------------------------------------------------------------------------------------
    
    def _prepare_new_game(self, cast, script):

        self._add_dialog(cast, self.GAME_NAME)
        self._add_dialog(cast, self.START_GAME)
        self._add_dialog(cast, self.HOW_TO_PLAY)

        # Adds video and audio service initialization
        self._add_initialize_script(script)
        # Adds assets
        self._add_load_script(script)
        script.clear_actions(INPUT)
        script.add_action(INPUT, ChangeSceneAction(self.KEYBOARD_SERVICE, HOW_TO_PLAY))
        self._add_output_script(script)
        self._add_unload_script(script)
        self._add_release_script(script)
        
    def _prepare_how_to_play(self, cast, script):
        pass

    def _prepare_player_selection(self, cast, script):
        self._add_bullet(cast)
        self._add_zombies(cast)
        self._add_player(cast)
        self._add_dialog(cast, PREP_TO_LAUNCH)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 2))
        self._add_output_script(script)
        script.add_action(OUTPUT, PlaySoundAction(self.AUDIO_SERVICE, WELCOME_SOUND))
        
    def _prepare_try_again(self, cast, script):
        self._add_bullet(cast)
        self._add_player(cast)
        self._add_dialog(cast, PREP_TO_LAUNCH)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 2))
        self._add_update_script(script)
        self._add_output_script(script)

    def _prepare_in_play(self, cast, script):
        self._activate_bullet(cast)
        cast.clear_actors(DIALOG_GROUP)

        script.clear_actions(INPUT)
        script.add_action(INPUT, self.CONTROL_PLAYER_ACTION)
        self._add_update_script(script)
        self._add_output_script(script)

    def _prepare_game_over(self, cast, script):
        self._add_bullet(cast)
        self._add_player(cast)
        self._add_dialog(cast, WAS_GOOD_GAME)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(NEW_GAME, 5))
        script.clear_actions(UPDATE)
        self._add_output_script(script)

    # ----------------------------------------------------------------------------------------------
    # casting methods
    # ----------------------------------------------------------------------------------------------
    
    #def _activate_bullet(self, cast):
    #    BULLET = cast.get_first_actor(BULLET_GROUP)
    #    BULLET.release()

    #def _add_bullet(self, cast):
    #    cast.clear_actors(BULLET_GROUP)
    #    x = CENTER_X - BULLET_WIDTH / 2
    #    y = SCREEN_HEIGHT - PLAYER_HEIGHT - BULLET_HEIGHT  
    #    position = Point(x, y)
    #    size = Point(BULLET_WIDTH, BULLET_HEIGHT)
    #    velocity = Point(0, 0)
    #    body = Body(position, size, velocity)
    #    image = Image(BULLET_IMAGE)
    #    BULLET = BULLET(body, image, True)
    #    cast.add_actor(BULLET_GROUP, BULLET)

    def _add_zombies(self, cast):
        cast.clear_actors(ZOMBIE_GROUP)
        
        stats = cast.get_first_actor(STATS_GROUP)
        level = stats.get_level() % BASE_LEVELS
        filename = LEVEL_FILE.format(level)

        with open(filename, 'r') as file:
            reader = csv.reader(file, skipinitialspace=True)

            for r, row in enumerate(reader):
                for c, column in enumerate(row):

                    x = FIELD_LEFT + c * ZOMBIE_WIDTH
                    y = FIELD_TOP + r * ZOMBIE_HEIGHT
                    color = column[0]
                    frames = int(column[1])
                    points = ZOMBIE_POINTS 
                    
                    if frames == 1:
                        points *= 2
                    
                    position = Point(x, y)
                    size = Point(ZOMBIE_WIDTH, ZOMBIE_HEIGHT)
                    velocity = Point(0, 0)
                    images = ZOMBIE_IMAGES[color][0:frames]

                    body = Body(position, size, velocity)
                    animation = Animation(images, ZOMBIE_RATE, ZOMBIE_DELAY)

                    zombie = Zombie(body, animation, points)
                    cast.add_actor(ZOMBIE_GROUP, zombie)

    def _add_dialog(self, cast, message):
        cast.clear_actors(DIALOG_GROUP)
        text = Text(message, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        position = Point(CENTER_X, CENTER_Y)
        label = Label(text, position)
        cast.add_actor(DIALOG_GROUP, label)

    def _add_level(self, cast):
        cast.clear_actors(LEVEL_GROUP)
        text = Text(LEVEL_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_LEFT)
        position = Point(HUD_MARGIN, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(LEVEL_GROUP, label)

    def _add_lives(self, cast):
        cast.clear_actors(LIVES_GROUP)
        text = Text(LIVES_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_RIGHT)
        position = Point(SCREEN_WIDTH - HUD_MARGIN, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(LIVES_GROUP, label)

    def _add_score(self, cast):
        cast.clear_actors(SCORE_GROUP)
        text = Text(SCORE_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        position = Point(CENTER_X, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(SCORE_GROUP, label)

    def _add_stats(self, cast):
        cast.clear_actors(STATS_GROUP)
        stats = Stats()
        cast.add_actor(STATS_GROUP, stats)

    def _add_player(self, cast):
        cast.clear_actors(PLAYER_GROUP)
        x = CENTER_X - PLAYER_WIDTH / 2
        y = SCREEN_HEIGHT - PLAYER_HEIGHT
        position = Point(x, y)
        size = Point(PLAYER_WIDTH, PLAYER_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        animation = Animation(PLAYER_IMAGES, PLAYER_RATE)
        player = Player(body, animation)
        cast.add_actor(PLAYER_GROUP, player)

    # ----------------------------------------------------------------------------------------------
    # scripting methods
    # ----------------------------------------------------------------------------------------------
    def _add_initialize_script(self, script):
        script.clear_actions(INITIALIZE)
        script.add_action(INITIALIZE, self.INITIALIZE_DEVICES_ACTION)

    def _add_load_script(self, script):
        script.clear_actions(LOAD)
        script.add_action(LOAD, self.LOAD_ASSETS_ACTION)
    
    def _add_output_script(self, script):
        script.clear_actions(OUTPUT)
        script.add_action(OUTPUT, self.START_DRAWING_ACTION)
        script.add_action(OUTPUT, self.DRAW_HUD_ACTION)
        script.add_action(OUTPUT, self.DRAW_BULLET_ACTION)
        script.add_action(OUTPUT, self.DRAW_ZOMBIES_ACTION)
        script.add_action(OUTPUT, self.DRAW_PLAYER_ACTION)
        script.add_action(OUTPUT, self.DRAW_DIALOG_ACTION)
        script.add_action(OUTPUT, self.END_DRAWING_ACTION)

    def _add_release_script(self, script):
        script.clear_actions(RELEASE)
        script.add_action(RELEASE, self.RELEASE_DEVICES_ACTION)
    
    def _add_unload_script(self, script):
        script.clear_actions(UNLOAD)
        script.add_action(UNLOAD, self.UNLOAD_ASSETS_ACTION)
        
    def _add_update_script(self, script):
        script.clear_actions(UPDATE)
        script.add_action(UPDATE, self.MOVE_BULLET_ACTION)
        script.add_action(UPDATE, self.MOVE_PLAYER_ACTION)
        script.add_action(UPDATE, self.COLLIDE_BORDERS_ACTION)
        script.add_action(UPDATE, self.COLLIDE_ZOMBIES_ACTION)
        script.add_action(UPDATE, self.COLLIDE_PLAYER_ACTION)
        script.add_action(UPDATE, self.MOVE_PLAYER_ACTION)
        script.add_action(UPDATE, self.CHECK_OVER_ACTION)