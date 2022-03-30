from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideBulletAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        bullets = cast.get_actors(BULLET_GROUP)
        zombies = cast.get_actors(ZOMBIE_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)
        
        for zombie in zombies:

            for bullet in bullets:
                bullet_body = bullet.get_body()
                zombie_body = zombie.get_body()

                if self._physics_service.has_collided(bullet_body, zombie_body):
                    sound = Sound(IMPACT_SOUND)
                    self._audio_service.play_sound(sound)
                    #points = zombie.get_points()
                    #stats.add_points(points)
                    cast.remove_actor(ZOMBIE_GROUP, zombie)
                    cast.remove_actor(BULLET_GROUP, bullet)