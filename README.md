# Mars Rover Kata

Welcome to the Mars Rover Kata! This kata simulates the movement of a rover on the surface of Mars.

### Implementation Details

- **Custom Decorators:** Implemented custom decorators to handle obstacle detection. The `check_obstacle` decorator ensures that the rover avoids obstacles when executing movement commands.

- **Enum Parameterization:** Used Enum classes to parameterize rover directions (`Direction`) and instructions (`Instruction`). This approach provides clarity and maintainability to the codebase, allowing for easier expansion and modification.

- **Multiple Obstacles:** Extended the functionality to handle multiple obstacles by allowing the `obstacle` parameter to accept a list of tuples representing obstacle coordinates. The rover intelligently avoids all obstacles in its path.

- **Comprehensive Testing:** Developed a comprehensive suite of tests to ensure the correctness and robustness of the Mars Rover simulation. Tests cover individual movement commands, obstacle detection, obstacle avoidance, and overall functionality.

## Getting Started

### Using Docker 🐳

1. Build the Docker image:
   ```
   docker compose build
   ```

2. Run the tests:
   ```
   docker compose run kata pytest
   ```

### Without Docker 🚀

1. Install dependencies locally:
   ```
   pip install -r requirements.txt  
   ```

2. Run the tests:
   ```
   pytest
   ```

____________
Happy coding! 🚀 👩‍💻👨‍💻👩🏽‍💻👨🏻‍💻👨🏿‍💻👩🏻‍💻

