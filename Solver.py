from Astar import astar


class Solver:
    def __init__(self):
        self.totalSteps = 0
        self.steps = 0

    def solveMaze(self, maze):
        if maze.hasDoors:
            print("TBD")
        else:
            path = astar(maze, maze.startingPoint, maze.endingPoint)
            if path is not None:
                self.steps = len(path) - 1
            else:
                self.steps = 0

        self.totalSteps += self.steps

    def stats(self):
        return self.totalSteps
