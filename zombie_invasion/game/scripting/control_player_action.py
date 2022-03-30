from constants import *
from game.casting.point import Point
from game.scripting.action import Action


class ControlPlayerAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        player = cast.get_first_actor(PLAYER_GROUP)
        
        if self._keyboard_service.is_key_down(LEFT): 
            player.get_body().set_velocity(Point(-PLAYER_VELOCITY, 0))
            player.move_next()

        elif self._keyboard_service.is_key_down(RIGHT):
            player.get_body().set_velocity(Point(PLAYER_VELOCITY, 0)) 
            player.move_next()  
        
        else: 
            player.stop_moving() 