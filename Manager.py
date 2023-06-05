import copy
import sys

from Maze import Maze
from Solver import Solver


class Manager:
    def __init__(self, iterations=20000, size=12, doors=False, geneSize=2):
        self.iterations = iterations
        self.size = size
        self.doors = doors
        self.geneSize = geneSize
        self.solved = 0
        self.mazes = []
        self.genePool = []
        self.steps = []
        self.solver = Solver()

    def stats(self):
        print("SOLVABLE: ", self.solved)
        print("ALL: ", self.iterations)
        print("SOLVED PERCENT: ", (self.solved / len(self.mazes)) * 100)
        print("AVERAGE LENGTH: ", sum(self.steps) / len(self.mazes))
        # print(self.steps)
        print("MAX LENGTH: ", max(self.steps))

    def generateGenes(self):

        def divideIntoShards():
            block = [0, 0]
            tempPlayer = [[0 for _ in range(self.geneSize)] for _ in range(self.geneSize)]
            tempElevation = [[0 for _ in range(self.geneSize)] for _ in range(self.geneSize)]
            tempDoors = [[0 for _ in range(self.geneSize)] for _ in range(self.geneSize)]
            tempKeys = [[0 for _ in range(self.geneSize)] for _ in range(self.geneSize)]
            tempMaze = Maze(self.geneSize, self.doors, True)
            for _ in range(int(int(self.size) ** 2 / int(self.geneSize) ** 2)):
                redFlag = False
                greenFlag = False
                blueFlag = False
                for i in range(int(self.geneSize)):
                    for j in range(int(self.geneSize)):
                        # print("i: ", i)
                        # print("j: ", j)
                        # print("block: ", block)
                        # print("val: ", maze.player[i + block[0]][j + block[1]])
                        tempPlayer[i][j] = maze.player[i + block[0]][j + block[1]]
                        tempElevation[i][j] = maze.elevation[i + block[0]][j + block[1]]
                        if maze.hasDoors:
                            tempDoors[i][j] = maze.doors[i + block[0]][j + block[1]]
                            tempKeys[i][j] = maze.keys[i + block[0]][j + block[1]]
                            if maze.keys[i + block[0]][j + block[1]] == 1 and redFlag is not False:
                                redFlag = True
                            if maze.keys[i + block[0]][j + block[1]] == 2 and greenFlag is not False:
                                greenFlag = True
                            if maze.keys[i + block[0]][j + block[1]] == 3 and blueFlag is not False:
                                blueFlag = True

                tempMaze.override(tempPlayer, tempElevation, tempDoors, tempKeys,
                                  self.doors, [redFlag, greenFlag, blueFlag])
                # print("ITERATION: ", _)
                # tempMaze.toString()

                self.genePool.append(copy.deepcopy(tempMaze))
                # for temp in self.shards:
                #     temp.toString(True)
                block[0] += self.geneSize
                if block[0] >= self.size:
                    block[0] = 0
                    block[1] += self.geneSize
                    if block[1] >= self.size:
                        block[1] = 0

        for _ in range(self.iterations):
            if _ % 100 == 0:
                sys.stdout.write('\r' + "GENERATION STATUS: " + str(round(_ / self.iterations, 2) * 100) + "%")
            maze = Maze(self.size, self.doors)
            self.mazes.append(copy.deepcopy(maze))
            steps = self.solver.solveMaze(maze)
            if steps:
                self.steps.append(steps)
                self.solved += 1
            else:
                self.steps.append(0)
            divideIntoShards()


