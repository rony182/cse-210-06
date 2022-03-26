from constants import *
from game.scripting.action import Action


class MoveZombieAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        zombie = cast.get_first_actor(ZOMBIE_GROUP)
        body = zombie.get_body()
        position = body.get_position()
        velocity = body.get_velocity()
        position = position.add(velocity)
        body.set_position(position)

# trying to make the zombies to track the Gunnar and move towards it.
    # def execute(elf, cast, script, callback):
    #     zombie = cast.get_first_actor(ZOMBIE_GROUP)
    #     for zomb in zombie:
    #         if zomb.get_x() < GUNNER_GROUP.get_x():
    #             zomb.x += ZOMBIE_VELOCITY
    #         elif zomb.x > GUNNER_GROUP.get_x():
    #             zomb.x -= ZOMBIE_VELOCITY
    #         elif zomb.y < GUNNER_GROUP.get_x():
    #             zomb.y += ZOMBIE_VELOCITY
    #         elif zomb.y > GUNNER_GROUP.get_x():
    #             zomb.y -= ZOMBIE_VELOCITY