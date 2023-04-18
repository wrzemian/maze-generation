from Astar import astar


class Solver:
    def __init__(self):
        self.totalSteps = []
        self.allMazes = []
        self.steps = 0

    def solveMaze(self, maze):
        if maze.hasDoors:
            path = astar(maze, maze.startingPoint, maze.endingPoint)
            if path is not None:
                self.steps = len(path) - 1
                print("exit reached without key interactions")
            else:
                print("exit unreachable without key")
                if maze.doorNumber == 1:
                    print("one key mode")
                    path = astar(maze, maze.startingPoint, maze.redKey)
                    if path is not None:
                        print("reached key, going for exit")
                        maze.redKeyActivated = True
                        self.steps = len(path) - 1
                        path = astar(maze, maze.redKey, maze.endingPoint)
                        if path is not None:
                            print("exit reached")
                            self.steps += len(path) - 1
                        else:
                            self.steps = 0
                            print("key reached, no path to exit")
                    else:
                        self.steps = 0
                        print("failed to reach key")
                if maze.doorNumber == 2:
                    print("two key mode")
                    keyorder = [maze.redKey, maze.greenKey]

        else:
            path = astar(maze, maze.startingPoint, maze.endingPoint)
            if path is not None:
                self.steps = len(path) - 1
            else:
                self.steps = 0

        print("\n\nITERATION STEPS")
        print("".join(str(self.steps)))
        print("\n\n")
        self.allMazes.append(maze)
        self.totalSteps.append(self.steps)

    def stats(self):
        for i in range(len(self.usingDoors)):
            if self.usingDoors[i]:
                self.allMazes[i].toString(True)

        return sum(self.totalSteps)
