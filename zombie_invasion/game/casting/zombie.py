import random
from constants import *
from game.casting.actor import Actor
from game.casting.point import Point

class Zombie(Actor):
    """A zombie that wants to eat the player."""

    def __init__(self, body, image, points, debug = False):
        """Constructs a new Zombie.

        Args:
            body: A new instance of Body.
            image: A new instance of Image.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._image = image
        self._points = points

    def get_body(self):
        """Gets the zombie's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def get_image(self):
        """Gets the zombie's image.
        
        Returns:
            An instance of Image.
        """
        return self._image

    def get_points(self):
        """Gets the zombie's points.
        
        Returns:
            A number representing the brick's points.
        """
        return self._points