from constants import *
from game.casting.actor import Actor
from game.casting.point import Point

class Player(Actor):
    """A person that shoots zombies in the game."""

    def __innit__(self, body, image, debug = False):
        """Constructs a new character.
        
        Args:
            body: A new instance of Body.
            image: A new instance of Image.
            debug: Whether it is being debugged.
        """
        super().__init__(debug)
        self._body = body
        self._image = image

    def get_body(self):
        """Gets the character's body.
        
        Returns: An instance of Body.
        """
        return self._body

    def get_image(self):
        """Gets the character's image.
        
        Returns: An instance of Image.
        """
        return self._image

    def move_next(self):
        """Moves the player using its velocity."""
        position = self._body.get_position()
        velocity = self._body.get_velocity()
        new_position = position.add(velocity)
        self._body.set_position(new_position)

    def swing_left(self):
        """Moves the player to the left."""
        velocity = Point(-GUNNER_VELOCITY, 0)
        self._body.set_velocity(velocity)
        
    def swing_right(self):
        """Moves the player to the right."""
        velocity = Point(GUNNER_VELOCITY, 0)
        self._body.set_velocity(velocity)
    
    def stop_moving(self):
        """Stops the player from moving."""
        velocity = Point(0, 0)
        self._body.set_velocity(velocity)