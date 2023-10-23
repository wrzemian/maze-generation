import copy
import sys
import pygad
import copy
import numpy
import time

from Maze import Maze
from Solver import solve_maze


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

    def stats(self):
        print("SOLVABLE: ", self.solved)
        print("ALL: ", self.iterations)
        print("SOLVED PERCENT: ", (self.solved / len(self.mazes)) * 100)
        print("AVERAGE LENGTH: ", sum(self.steps) / len(self.mazes))
        # print(self.steps)
        print("MAX LENGTH: ", max(self.steps))

    def experiment(self):
        self.generateGenes()
        self.genetic_alghoritm()

    def genetic_alghoritm(self):
        def fitness(ga_instance, solution, solution_idx):
            fitMaze = Maze(self.size, self.doors)
            genes = [copy.deepcopy(self.genePool[int(i)]) for i in numpy.round(solution).astype(int)]
            fitMaze.overrideFormGenes(self.size, self.geneSize, genes)
            # print("SOLUTION: {s}, START: {x}, STOP: {y}".
            #       format(s=solution_idx, x=fitMaze.findInArray(fitMaze.player, 1), y=fitMaze.findInArray(fitMaze.player, 2)))
            # fitMaze.toString()
            # status = False
            try:
                status = solve_maze(fitMaze)
                if status is not False:
                    return status
                else:
                    result = 0
                    result += fitMaze.checkElevation()
                    result += fitMaze.checkMultipleThingsOnTile()
                    result += fitMaze.checkDoors()
                    result += fitMaze.checkKeys()
                    result += fitMaze.checkPlayerDoorAmount()

                    if result == 0:
                        return -0.1
                    else:
                        return result
            except IndexError as e:
                fitMaze.visualize(True)

        start = time.time()

        genePoolSize = len(self.genePool)
        genesInSolution = int(int(self.size) ** 2 / int(self.geneSize) ** 2)
        self.stats()

        # print("STARTING MAZE:\n")
        # print(manager.mazes[0].toString())
        # for gene in manager.genePool:
        #     print(gene.toString())

        num_solutions = 1200
        population_vector = numpy.zeros(shape=(num_solutions, genesInSolution))
        for solution_idx in range(num_solutions):
            initialPop = numpy.random.randint(0, genePoolSize, size=genesInSolution)
            initialPop = initialPop.astype(numpy.uint8)
            population_vector[solution_idx, :] = initialPop

        # print(population_vector)
        bestSol = 0
        bestSolParams = [0, 0]
        counter = 0
        ga_instance = 0
        ga_instance = pygad.GA(num_generations=30,
                               num_parents_mating=2,
                               fitness_func=fitness,
                               num_genes=genesInSolution,
                               initial_population=population_vector,
                               crossover_type="uniform",
                               crossover_probability=0.4,
                               mutation_type="random",
                               mutation_probability=0.01,
                               mutation_by_replacement=True,
                               random_mutation_min_val=0,
                               random_mutation_max_val=genePoolSize - 1)

        ga_instance.run()
        solution, solution_fitness, solution_idx = ga_instance.best_solution()
        print("BEST SOL: ", solution_fitness)
        ga_instance.plot_fitness()
        end = time.time()
        print("\n\nELAPSED TIME: ", end - start)


    def generateGenes(self):

        def divideIntoGenes():
            block = [0, 0]
            tempPlayer = [[0 for _ in range(self.geneSize)] for _ in range(self.geneSize)]
            tempElevation = [[0 for _ in range(self.geneSize)] for _ in range(self.geneSize)]
            tempDoors = [[0 for _ in range(self.geneSize)] for _ in range(self.geneSize)]
            tempKeys = [[0 for _ in range(self.geneSize)] for _ in range(self.geneSize)]
            tempMaze = Maze(self.geneSize, self.doors)
            for _ in range(int(int(self.size) ** 2 / int(self.geneSize) ** 2)):
                keysArr = [[], [], []]
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
                            if maze.keys[i + block[0]][j + block[1]] == 1:
                                keysArr[0].append(maze.keys[i + block[0]][j + block[1]])
                            if maze.keys[i + block[0]][j + block[1]] == 2:
                                keysArr[1].append(maze.keys[i + block[0]][j + block[1]])
                            if maze.keys[i + block[0]][j + block[1]] == 3:
                                keysArr[2].append(maze.keys[i + block[0]][j + block[1]])


                tempMaze.override(tempPlayer, tempElevation, tempDoors, tempKeys,
                                  self.doors, keysArr)
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
            maze.randomize()
            # maze.visualize(True)
            self.mazes.append(copy.deepcopy(maze))
            steps = solve_maze(maze)
            if steps:
                self.steps.append(steps)
                self.solved += 1
            else:
                self.steps.append(0)
            divideIntoGenes()


