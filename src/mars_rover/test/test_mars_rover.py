import pytest
from src.mars_rover.classes import MarsRover, Direction


def test_mars_rover_move_forward_north():
    """Tests that the rover moves one step north (positive Y) when facing North."""
    mars_rover = MarsRover(position=Direction.NORTH.value, coordinates=(0, 0))
    mars_rover.forward()
    assert mars_rover.coordinates == (0, 1)


def test_mars_rover_move_backward_north():
    """Tests that the rover moves one step backward (negative Y) when facing North."""
    mars_rover = MarsRover(position=Direction.NORTH.value, coordinates=(0, 0))
    mars_rover.backward()
    assert mars_rover.coordinates == (0, -1)


def test_mars_rover_full_rotation_right():
    """Tests that the rover can perform a complete 360-degree rotation to the right."""
    mars_rover = MarsRover(position=Direction.NORTH.value, coordinates=(0, 0))
    expected_directions = [Direction.EAST, Direction.SOUTH, Direction.WEST, Direction.NORTH]
    for expected_direction in expected_directions:
        mars_rover.right()
        assert mars_rover.position == expected_direction


def test_mars_rover_full_rotation_left():
    """Tests that the rover can perform a complete 360-degree rotation to the left."""
    mars_rover = MarsRover(position=Direction.NORTH.value, coordinates=(0, 0))
    expected_directions = [Direction.WEST, Direction.SOUTH, Direction.EAST, Direction.NORTH]
    for expected_direction in expected_directions:
        mars_rover.left()
        assert mars_rover.position == expected_direction


def test_mars_rover_follows_instructions():
    """Tests that the rover follows a sequence of movement instructions (forward, turn right)."""
    mars_rover = MarsRover(position=Direction.NORTH.value, coordinates=(0, 0))
    instructions = ['f', 'r', 'f', 'f']  # Move forward, turn right, move forward twice
    mars_rover.receive_instructions(instructions)
    assert mars_rover.coordinates == (2, 1)
    assert mars_rover.position == Direction.EAST


def test_mars_rover_avoids_obstacle_when_moving_forward():
    """Tests that the rover doesn't move forward if there's a registered obstacle in its path."""
    mars_rover = MarsRover(position=Direction.NORTH.value, coordinates=(0, 0), obstacles=[(0, 1)])
    instructions = ['f']  # Move forward (but there's an obstacle)
    mars_rover.receive_instructions(instructions)
    assert mars_rover.coordinates == (0, 0)  # Rover stays in place to avoid collision


def test_mars_rover_identifies_obstacle():
    """Tests that the rover can identify a specific location as an obstacle."""
    mars_rover = MarsRover(position=Direction.NORTH.value, coordinates=(0, 0), obstacles=[(0, 1)])
    assert mars_rover.is_obstacle((0, 1)) is True
    assert mars_rover.is_obstacle((1, 1)) is False  # This is not a registered obstacle


def test_mars_rover_avoids_multiple_obstacles_when_moving_forward():
    """Tests that the rover doesn't move forward if there are registered obstacles in its path."""
    mars_rover = MarsRover(position=Direction.NORTH.value, coordinates=(0, 0),
                           obstacles=[(0, 1), (1, 0)])
    instructions = ['f']  # Move forward (but there are obstacles)
    mars_rover.receive_instructions(instructions)
    assert mars_rover.coordinates == (0, 0)  # Rover stays in place to avoid collision


def test_mars_rover_avoids_multiple_obstacles_when_moving_backward():
    """Tests that the rover doesn't move backward if there are registered obstacles in its path."""
    mars_rover = MarsRover(position=Direction.NORTH.value, coordinates=(0, 0),
                           obstacles=[(0, -1), (1, 0)])
    instructions = ['b']  # Move backward (but there are obstacles)
    mars_rover.receive_instructions(instructions)
    assert mars_rover.coordinates == (0, 0)  # Rover stays in place to avoid collision


def test_mars_rover_can_move_with_initial_multiple_obstacles():
    """Tests that the rover can still move forward even with obstacles in its initial position."""
    mars_rover = MarsRover(position=Direction.NORTH.value, coordinates=(0, 0),
                           obstacles=[(0, 0), (1, 1)])
    mars_rover.forward()
    assert mars_rover.coordinates == (0, 1)


def test_mars_rover_can_move_with_initial_obstacle():
    """Tests that the rover can still move forward even with an obstacle in its initial position.
       This is because the obstacle is considered to be at its current location."""
    mars_rover = MarsRover(position=Direction.NORTH.value, coordinates=(0, 0), obstacles=[(0, 0)])
    mars_rover.forward()
    assert mars_rover.coordinates == (0, 1)


def test_mars_rover_raises_error_for_invalid_instruction():
    """Tests that the rover raises a ValueError for instructions that are not 'f', 'b', 'l', or 'r'."""
    mars_rover = MarsRover(position=Direction.NORTH.value, coordinates=(0, 0))
    with pytest.raises(ValueError, match="Invalid instruction: x"):
        mars_rover.receive_instructions(['x'])
