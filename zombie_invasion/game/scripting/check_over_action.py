from constants import *
from game.scripting.action import Action


class CheckOverAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        """Executes the check over action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of actions in the game.
            callback (ActionCallback): A callback to change the scene.
        """
        
        # This class should check how many zombies are left
        # and end the game.
        
        pass