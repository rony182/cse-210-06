from constants import *
from random import randint
from game.casting.body import Body
from game.casting.image import Image
from game.casting.point import Point
from game.casting.zombie import Zombie
from game.scripting.action import Action


class AddZombieAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        
        zombies = cast.get_actors(ZOMBIE_GROUP)
        if len(zombies) < ZOMBIE_MAX_NUMBER:
            
            i = randint(0, 3)
            img = Image(ZOMBIE_IMAGES[i])
            # Get random positions for the zombie to appear
            x = randint(0, SCREEN_WIDTH)
            # Create the Zombie body
            body = Body(Point(x, 0), Point(ZOMBIE_WIDTH, ZOMBIE_HEIGHT), Point(0, ZOMBIE_VELOCITY))
            # Create Zombie
            zombie = Zombie(body, img, (i + 1) * 10)
            # Add Zombie to the cast
            cast.add_actor(ZOMBIE_GROUP, zombie)