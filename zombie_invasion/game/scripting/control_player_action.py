from constants import *
from game.scripting.action import Action


class ControlPlayerAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        gunner = cast.get_first_actor(GUNNER_GROUP)
        if self._keyboard_service.is_key_down(LEFT): 
            gunner.swing_left()
        elif self._keyboard_service.is_key_down(RIGHT): 
            gunner.swing_right()  
        else: 
            gunner.stop_moving() 