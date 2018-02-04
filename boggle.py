from string import ascii_uppercase
from random import choice

def make_grid(width, height):
    """
    Creates a grid that will hold all of the tiles
    for a boggle game, with letters inside each of the coordinates.
    
    We use the random - choice and send it ascii_uppercase to generate letters
    for each of the grid coordinates
    """
    return {(row, col): choice(ascii_uppercase) 
        for row in range(height)
        for col in range(width)
    }
        