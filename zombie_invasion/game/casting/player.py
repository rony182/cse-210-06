from constants import *
from game.casting.actor import Actor
from game.casting.point import Point

class Player(Actor):
    """A person that shoots zombies in the game."""

    def __init__(self, body, image, debug = False):
        """Constructs a new character.
        
        Args:
            body: A new instance of Body.
            image: A new instance of I.
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

    def set_image(self, image):
        """Sets the character's image according to the player's choice
        
        Args: A string that contains the image path.
        """
        self._image = image

    def move_next(self):
        """Moves the player using its velocity."""
        position = self._body.get_position()
        velocity = self._body.get_velocity()
        new_position = position.add(velocity)
        self._body.set_position(new_position)

    def stop_moving(self):
        """Stops the player from moving."""
        velocity = Point(0, 0)
        self._body.set_velocity(velocity)   