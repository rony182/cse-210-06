from game.scripting.action import Action


class LoadAssetsAction(Action):

    def __init__(self, audio_service, video_service):
        """Constructs a LoadAssetsAction object.
        """
        self._audio_service = audio_service
        self._video_service = video_service

    def execute(self, cast, script, callback):
        """Executes the load assets action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of actions in the game.
            callback (ActionCallback): A callback to change the scene.
        """
        self._audio_service.load_sounds("batter/assets/sounds")
        self._video_service.load_fonts("batter/assets/fonts")
        self._video_service.load_images("batter/assets/images")
        