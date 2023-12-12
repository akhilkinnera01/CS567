import random
import maze

print("Module imported Successfully!")

def create_maze(width, height):
    """
    Creates a maze represented as a 2D grid of 'wall' and 'path' cells.
    Initializes with a simple path for demonstration.
    """
    maze = [['wall' for _ in range(width)] for _ in range(height)]
    for i in range(width):
        maze[1][i] = 'path'  # Creating a simple path
    return maze

def mutate_maze(maze):
    """
    Mutates the maze by randomly changing cells from 'wall' to 'path' or vice versa.
    """
    height = len(maze)
    width = len(maze[0])
    for _ in range(5):  # Mutate 5 cells for example
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        maze[y][x] = 'path' if maze[y][x] == 'wall' else 'wall'
    return maze

# Example code to test the functions directly (optional)
if __name__ == "__main__":
    initial_maze = create_maze(10, 10)
    print("Original Maze:")
    for row in initial_maze:
        print(' '.join(row))

    mutated_maze = mutate_maze(initial_maze)
    print("\nMutated Maze:")
    for row in mutated_maze:
        print(' '.join(row))
