from constants import *
from game.casting.body import Body
from game.casting.bullet import Bullet
from game.casting.image import Image
from game.casting.point import Point
from game.scripting.action import Action

BULLET_FILEPATH = "zombie_invasion\\assets\\images\\bullet.png"
class ControlBulletAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        player = cast.get_first_actor(PLAYER_GROUP)
        
        if self._keyboard_service.is_key_pressed(SPACE):
            position = player.get_body().get_position()
            body = Body(position, Point(BULLET_WIDTH, BULLET_HEIGHT), Point(0, -BULLET_VELOCITY))
            img = Image(f"zombie_invasion\\{BULLET_IMAGE}")

            bullet = Bullet(body, img)

            cast.add_actor(BULLET_GROUP, bullet)