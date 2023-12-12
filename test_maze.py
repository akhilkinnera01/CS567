import unittest
import io
import sys
from maze import Maze  # Make sure to import the Maze class from your maze.py file

class TestMaze(unittest.TestCase):
    def test_maze_creation(self):
        maze = Maze(10, 10)
        self.assertEqual(len(maze.grid), 10)
        self.assertEqual(len(maze.grid[0]), 10)
        self.assertTrue(all(cell == 'wall' for row in maze.grid for cell in row))

    def test_path_creation(self):
        maze = Maze(10, 10)
        maze.create_path()
        self.assertEqual(maze.grid[1], ['path'] * 10)

    def test_maze_mutation(self):
        maze = Maze(10, 10)
        maze.create_path()
        old_grid = [row[:] for row in maze.grid]
        maze.mutate()
        self.assertNotEqual(maze.grid, old_grid)

    def test_display(self):
        maze = Maze(10, 10)
        maze.create_path()

        captured_output = io.StringIO()          # Create a StringIO object to capture output
        sys.stdout = captured_output             # Redirect stdout
        maze.display()                           # Call the display function
        sys.stdout = sys.__stdout__              # Reset redirect

        # The expected output is the maze structure as a string
        expected_output = ''
        for row in maze.grid:
            expected_output += ' '.join(row) + '\n'

        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == "__main__":
    unittest.main()
