from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action
from game.casting.point import Point

class CollideBordersAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service    
        
    def execute(self, cast, script, callback):
        
        player = cast.get_first_actor(PLAYER_GROUP)
        body = player.get_body()
        position = body.get_position()
        x = position.get_x()
                
        if x < FIELD_LEFT:
            player.stop_moving()
            
        elif x >= (FIELD_RIGHT - PLAYER_WIDTH):
            player.stop_moving()