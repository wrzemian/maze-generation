import Maze


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    maze = Maze.Maze()
    maze.initDoors()
    print('\n'.join(' '.join(str(x) for x in row) for row in maze.doors))
