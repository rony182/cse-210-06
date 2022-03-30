from constants import *
from game.scripting.action import Action


class MoveZombieAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        
        zombies = cast.get_actors(ZOMBIE_GROUP)
        for zombie in zombies:
            body = zombie.get_body()
            position = body.get_position()
            velocity = body.get_velocity()
            position = position.add(velocity)
            body.set_position(position)
            
            if body.get_position().get_y() > SCREEN_HEIGHT:
                cast.remove_actor(ZOMBIE_GROUP, zombie)