from Maze import Maze
from Astar import astar


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    maze = Maze(12, False)
    maze.toString()

    path = astar(maze, maze.startingPoint, maze.endingPoint)
    print("\n\nPATH")
    print(path)
    if path is not None:
        print("\nPATH VALUES")
        temp = []
        for pos in path:
            temp.append(maze.elevation[pos[0]][pos[1]])
        print(temp)
        print("\nMOVES REQUIRED")
        print(len(path) - 1)


