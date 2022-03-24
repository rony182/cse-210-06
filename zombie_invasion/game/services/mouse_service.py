import pyray
from game.casting.point import Point

class MouseService:
    """A mouse service inteface."""

    def __init__(self):
        """Constructs a new MouseService"""
        self._mouse_keys = {
            "left" : pyray.MOUSE_BUTTON_LEFT,
            "right" : pyray.MOUSE_BUTTON_RIGHT,
            "middle" : pyray.MOUSE_BUTTON_MIDDLE
        }

    def get_coordinates(self):
        """Gets the current mouse coordinates as a Point.
        
        Returns:
            Point: An instance of the game.casting.Point class.
        """
        x = pyray.get_mouse_x()
        y = pyray.get_mouse_y()
        return Point(x, y)

    def has_mouse_moved(self):
        """Whether or not the mouse has moved since the last frame.
        
        Returns:
            True if the mouse moved; false if otherwise.
        """
        raise NotImplementedError("not implemented in base class")
    
    def is_button_down(self, button):
        """Detects if the given button is pressed.
        
        Args:
            button: A string containing the button value, e.g. 'left', 'right' or 'middle'.

        Returns:
            True if the button is pressed; false if otherwise.
        """
        return pyray.is_mouse_button_down(self._mouse_keys[button])
    
    def is_button_pressed(self, button):
        """Detects if the given button was pressed once.
        
        Args:
            button: A string containing the button value, e.g. 'left', 'right' or 'middle'.

        Returns:
            True if the button was pressed once; false if otherwise.
        """
        return pyray.is_mouse_button_pressed(self._mouse_keys[button])

    def is_button_released(self, button):
        """Detects if the given button was released once.
        
        Args:
            button: A string containing the button value, e.g. 'left', 'right' or 'middle'.

        Returns:
            True if the button was released once; false if otherwise.
        """
        return pyray.is_mouse_button_released(self._mouse_keys[button])
    
    def is_button_up(self, button):
        """Detects if the given button is released.
        
        Args:
            button: A string containing the button value, e.g. 'left', 'right' or 'middle'.

        Returns:
            True if the button is released; false if otherwise.
        """
        return pyray.is_mouse_button_up(self._mouse_keys[button])