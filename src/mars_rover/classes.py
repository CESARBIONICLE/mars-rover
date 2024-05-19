from enum import Enum
from typing import List

from src.mars_rover.decorators import check_obstacle


class Direction(Enum):
    """Enumeration for cardinal directions."""
    NORTH = "north"
    EAST = "east"
    SOUTH = "south"
    WEST = "west"


class MarsRover:
    """Class representing a Mars rover robot"""

    def __init__(self, position: str, coordinates: tuple, obstacles: List[tuple] = None):
        """
        Initialize the MarsRover object.

        Args:
            position (str): The initial direction the rover is facing as a string.
            coordinates (tuple): The initial coordinates (x, y) of the rover.
            obstacles (List[tuple]): List of coordinates (x, y) of obstacles. Default is None.
        """
        self.position = Direction(position)
        self.coordinates = coordinates
        self.obstacles = obstacles if obstacles is not None else []

    @check_obstacle
    def forward(self):
        """Move the rover forward based on its current direction."""
        x, y = self.coordinates
        if self.position == Direction.NORTH:
            return x, y + 1
        elif self.position == Direction.SOUTH:
            return x, y - 1
        elif self.position == Direction.EAST:
            return x + 1, y
        elif self.position == Direction.WEST:
            return x - 1, y

    @check_obstacle
    def backward(self):
        """Move the rover backward based on its current direction."""
        x, y = self.coordinates
        if self.position == Direction.NORTH:
            return x, y - 1
        elif self.position == Direction.SOUTH:
            return x, y + 1
        elif self.position == Direction.EAST:
            return x - 1, y
        elif self.position == Direction.WEST:
            return x + 1, y

    def right(self):
        """Turn the rover 90 degrees to the right."""
        direction_map = {
            Direction.NORTH: Direction.EAST,
            Direction.EAST: Direction.SOUTH,
            Direction.SOUTH: Direction.WEST,
            Direction.WEST: Direction.NORTH
        }
        self.position = direction_map[self.position]

    def left(self):
        """Turn the rover 90 degrees to the left."""
        direction_map = {
            Direction.NORTH: Direction.WEST,
            Direction.WEST: Direction.SOUTH,
            Direction.SOUTH: Direction.EAST,
            Direction.EAST: Direction.NORTH
        }
        self.position = direction_map[self.position]

    def receive_instructions(self, instructions_list):
        """
        Receive a list of instructions and execute them.

        Args:
            instructions_list (list): A list of instruction values (e.g., 'f', 'b', 'r', 'l').
        """
        command_map = {
            'f': self.forward,
            'b': self.backward,
            'r': self.right,
            'l': self.left
        }
        for instruction in instructions_list:
            if instruction in command_map:
                command_map[instruction]()
            else:
                raise ValueError(f"Invalid instruction: {instruction}")

    def is_obstacle(self, coordinates):
        """
        Check if the given coordinates are an obstacle.

        Args:
            coordinates (tuple): The coordinates to check.

        Returns:
            bool: True if the coordinates are an obstacle, False otherwise.
        """
        return coordinates in self.obstacles

    @staticmethod
    def avoid_obstacle(coordinates):
        """
        Handle the situation when the rover encounters an obstacle.
        """
        print(f"Obstacle detected in {coordinates}. Movement halted.")
