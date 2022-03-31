from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action
from game.casting.point import Point

class CollideBordersAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        self._breach_count = 0
        
    def execute(self, cast, script, callback):
        
        player = cast.get_first_actor(PLAYER_GROUP)
        body = player.get_body()
        position = body.get_position()
        x = position.get_x()
                
        if x < FIELD_LEFT:
            player.stop_moving()
            
        elif x >= (FIELD_RIGHT - PLAYER_WIDTH):
            player.stop_moving()

        zombies = cast.get_actors(ZOMBIE_GROUP)
        for zombie in zombies:
            zombie_body = zombie.get_body()
            zombie_position = zombie_body.get_position()
            y = zombie_position.get_y()

            if y >= (FIELD_BOTTOM):
                stats = cast.get_first_actor(STATS_GROUP)
                self._breach_counter()
                if self._breach_count >= 10:
                    stats.lose_life()
                    self._reset_breach_counter()
            
                if stats.get_lives() == 0:
                    callback.on_next(GAME_OVER)
                    sound = Sound(OVER_SOUND)
                    self._audio_service.play_sound(sound)
    
    def _breach_counter(self):
        """Counts how many zombies passed by the player."""
        self._breach_count += 1
    
    def _reset_breach_counter(self):
        """Resets the breach counter."""
        self._breach_count = 0