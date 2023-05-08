import copy

from Maze import Maze
from Solver import Solver


class Manager:
    def __init__(self, iterations=20000, size=12, doors=False, shardSize=2):
        self.iterations = iterations
        self.size = size
        self.doors = doors
        self.shardSize = shardSize
        self.solved = 0
        self.mazes = []
        self.shards = []
        self.steps = []
        self.solver = Solver()

    def stats(self):
        print("SOLVABLE: ", self.solved)
        print("ALL: ", self.iterations)
        print("SOLVED PERCENT: ", self.solved / len(self.mazes))

    def generateShards(self):

        def divideIntoShards():
            block = [0, 0]
            tempPlayer = [[0 for _ in range(self.shardSize)] for _ in range(self.shardSize)]
            tempElevation = [[0 for _ in range(self.shardSize)] for _ in range(self.shardSize)]
            tempDoors = [[0 for _ in range(self.shardSize)] for _ in range(self.shardSize)]
            tempKeys = [[0 for _ in range(self.shardSize)] for _ in range(self.shardSize)]
            tempMaze = Maze(self.shardSize, self.doors, True)
            for _ in range(int(int(self.size) ** 2 / int(self.shardSize) ** 2)):
                redFlag = False
                greenFlag = False
                blueFlag = False
                for i in range(int(self.shardSize)):
                    for j in range(int(self.shardSize)):
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

                self.shards.append(copy.deepcopy(tempMaze))
                # for temp in self.shards:
                #     temp.toString(True)
                block[0] += self.shardSize
                if block[0] > self.size / self.shardSize:
                    block[0] = 0
                    block[1] += self.shardSize
                    if block[1] > self.size / self.shardSize:
                        block[1] = 0


        for _ in range(self.iterations):
            maze = Maze(self.size, self.doors)
            self.mazes.append(copy.deepcopy(maze))
            steps = self.solver.solveMaze(maze)
            if steps:
                self.steps.append(steps)
                self.solved += 1
            else:
                self.steps.append(0)
            divideIntoShards()
