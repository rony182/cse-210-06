from constants import *
from game.casting.body import Body
from game.casting.image import Image
from game.casting.point import Point
from game.scripting.action import Action
from game.scripting.draw_sprite_action import DrawSpriteAction
from game.services.raylib.raylib_video_service import RaylibVideoService


'''This class needs to be finished'''
class ChangePlayerAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        self._n = 0
        
    def execute(self, cast, script, callback):
        """Checks whether the player is pressing lef or right arrow to determine 
        the number of sprite to return.
          Returns:
                  The character's image path."""
        sprites = cast.get_actors(SPRITES_GROUP)
        
        if self._keyboard_service.is_key_down(LEFT):
            # self._change_image_number(-1)
            # if self._n < 0:
            #     self._n + 4
            pass
          
        elif self._keyboard_service.is_key_down(RIGHT):
            # self._change_image_number(1)
            # if self._n > 3:
            #     self._n - 4
            pass
        # return sprites[self._n]

    # def _change_image_number(self, number):
    #   """Changes the number that represents the character's image."""
    #   self._n + number