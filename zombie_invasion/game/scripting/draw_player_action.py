from constants import *
from game.scripting.action import Action


class DrawPlayerAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        gunner = cast.get_first_actor(GUNNER_GROUP)
        body = gunner.get_body()

        if gunner.is_debug():
            gun = body.get_rectangle()
            self._video_service.draw_rectangle(gun, YELLOW)
            
        animation = gunner.get_animation()
        image = animation.next_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)