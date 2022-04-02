from constants import *
from game.scripting.action import Action


class ChangeSceneAction(Action):
    """Constructs a ChangeSceneAction object."""
    def __init__(self, keyboard_service, next_scene):
        self._keyboard_service = keyboard_service
        self._next_scene = next_scene
        
    def execute(self, cast, script, callback):
        """Executes the load assets action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of actions in the game.
            callback (ActionCallback): A callback to change the scene.
        """
        if self._keyboard_service.is_key_pressed(ENTER):
            callback.on_next(self._next_scene)