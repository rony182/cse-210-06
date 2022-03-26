from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollidePlayerAction(Action):

    def __init__(self, physics_service, audio_service):
        """Constructs a CollidePlayerAction object."""
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        """Executes the collide player action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of actions in the game.
            callback (ActionCallback): A callback to change the scene.
        """

        # This one should check if the player 
        # collided with a zombie.
        pass