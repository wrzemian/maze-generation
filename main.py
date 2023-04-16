from Maze import Maze
from Astar import astar


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    maze = Maze(12, False)
    maze.toString()

    path = astar(maze, maze.startingPoint, maze.endingPoint)
    print("\n\nPATH")
    print(path)
    print("\n\nMOVES REQUIRED")
    print(len(path) - 1)


