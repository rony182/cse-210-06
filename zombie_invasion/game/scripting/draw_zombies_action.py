from constants import *
from game.scripting.action import Action

class DrawZombiesAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
    
    def execute(self, cast, script, callback):
        zombies = cast.get_actors(ZOMBIE_GROUP)

        for zombie in zombies:
            body = zombie.get_body()

            if zombie.is_debug():
                background_rectangle = body.get_rectangle()
                self._video_service.draw_rectangle(background_rectangle, BLACK)
            
            image = zombie.get_image()
            position = body.get_position()
            self._video_service.draw_image(image, position)