import random
from constants import *
from game.casting.actor import Actor
from game.casting.point import Point


class Bullet(Actor):
    """A solid, spherical object that is bounced around in the game."""
    
    def __init__(self, body, image, debug = False):
        """Constructs a new Bullet.

        Args:
            body: A new instance of Body.
            image: A new instance of Image.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._image = image

    def get_body(self):
        """Gets the bullet's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def get_image(self):
        """Gets the bullet's image.
        
        Returns:
            An instance of Image.
        """
        return self._image
        
    def shot(self):
        """Shoots the bullet in a straight direction."""
        vy = -BULLET_VELOCITY
        velocity = Point(0, vy)
        self._body.set_velocity(velocity)