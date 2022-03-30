from constants import *
from game.casting.point import Point
from game.scripting.action import Action


class ControlBulletAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        player = cast.get_first_actor(BULLET_GROUP)
        
        if self._keyboard_service.is_key_pressed(SPACE):
            player.get_body()
            player.shot()
