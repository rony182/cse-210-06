from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action
from game.casting.player import Player


class CollideZombieAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        self._player= Player()
        
    def execute(self, cast, script, callback):
        zombies = cast.get_actors(ZOMBIE_GROUP)
        gunner = self._player
        
        for zombie in zombies:
            zombie_body= zombie.get_body()
            player_body = gunner.get_body()
            if self._physics_service.has_collided(player_body, zombie_body):
                sound = Sound(ZOMBIE_ATTACK_SOUND)
                self._audio_service.play_sound(sound)
                stats = cast.get_first_actor(STATS_GROUP)
                stats.lose_life()
                
                if stats.get_lives() > 0:
                    callback.on_next(TRY_AGAIN)
                else:
                    callback.on_next(GAME_OVER)
                    self._audio_service.play_sound(OVER_SOUND)