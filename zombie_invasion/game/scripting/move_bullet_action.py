from constants import *
from game.casting.sound import Sound
from game.casting.point import Point
from game.scripting.action import Action


class MoveBulletAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
    
        bullets = cast.get_actors(BULLET_GROUP)
        for bullet in bullets:
            body = bullet.get_body()
            velocity = body.get_velocity()
            position = body.get_position()
            y = position.get_y()    
            position = position.add(velocity)

            if y < 0:
                position = Point(position.get_y(), 0)
            elif y > (SCREEN_HEIGHT - BULLET_HEIGHT):
                position = Point(position.get_x(), SCREEN_HEIGHT - BULLET_HEIGHT)
                
            body.set_position(position)