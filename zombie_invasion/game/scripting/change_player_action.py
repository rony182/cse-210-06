from constants import *
from game.casting.body import Body
from game.casting.image import Image
from game.casting.point import Point
from game.scripting.action import Action

'''This class needs to be finished'''
class ChangePlayerAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        sprite = cast.get_first_actor(SPRITES_GROUP)
        
        if self._keyboard_service.is_key_down(LEFT):
          pass
            
        elif self._keyboard_service.is_key_down(RIGHT):
          pass

        
        