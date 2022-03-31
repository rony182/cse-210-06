from constants import *
from game.casting.point import Point
from game.scripting.action import Action


class DrawSpriteAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):

        sprites = cast.get_actors(SPRITES_GROUP)
        if sprites:
          self._video_service.draw_image(sprites[0], Point(CENTER_X - SPRITE_WIDTH / 2, CENTER_Y - SPRITE_HEIGHT / 2))