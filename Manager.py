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
        print("\nSOLVABLE: ", self.solved)
        print("ALL: ", self.iterations)
        print("SOLVED PERCENT: ", (self.solved / len(self.mazes)) * 100)
        print("AVERAGE LENGTH: ", sum(self.steps) / len(self.mazes))
        # print(self.steps)
        print("MAX LENGTH: ", max(self.steps))

    def experiment(self):
        self.generateGenes()
        self.genetic_alghoritm()

    def genetic_alghoritm(self):
        def initialize_population(gene_pool_size, genes_in_solution, num_solutions):
            population_vector = numpy.zeros(shape=(num_solutions, genes_in_solution), dtype=numpy.uint8)
            for solution_idx in range(num_solutions):
                initial_pop = numpy.random.randint(0, gene_pool_size, size=genes_in_solution).astype(numpy.uint8)
                population_vector[solution_idx, :] = initial_pop
            return population_vector

        def fitness(ga_instance, solution, solution_idx):
            fitMaze = Maze(self.size, self.doors)
            genes = [copy.deepcopy(self.genePool[int(i)]) for i in numpy.round(solution).astype(int)]
            fitMaze.overrideFormGenes(self.size, self.geneSize, genes)
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

        def on_generation(ga_instance):
            sys.stdout.write('\r' + "GENERATION " + str(ga_instance_f.generations_completed))

        start = time.time()

        genePoolSize = len(self.genePool)
        genesInSolution = int(int(self.size) ** 2 / int(self.geneSize) ** 2)
        self.stats()

        initial_population_f = initialize_population(genePoolSize, genesInSolution, 200)
        initial_population_i = initialize_population(genePoolSize, genesInSolution, 1000)

        ga_instance_f = pygad.GA(num_generations=1,
                                 num_parents_mating=2,
                                 fitness_func=fitness,
                                 num_genes=genesInSolution,
                                 initial_population=initial_population_f,
                                 crossover_type="uniform",
                                 crossover_probability=0.4,
                                 mutation_type="random",
                                 mutation_probability=0.01,
                                 mutation_by_replacement=True,
                                 random_mutation_min_val=0,
                                 random_mutation_max_val=genePoolSize - 1,
                                 on_generation=on_generation)

        ga_instance_i = pygad.GA(num_generations=1,
                                 num_parents_mating=2,
                                 fitness_func=fitness,
                                 num_genes=genesInSolution,
                                 initial_population=initial_population_i,
                                 crossover_type="uniform",
                                 crossover_probability=0.4,
                                 mutation_type="random",
                                 mutation_probability=0.01,
                                 mutation_by_replacement=True,
                                 random_mutation_min_val=0,
                                 random_mutation_max_val=genePoolSize - 1,
                                 on_generation=on_generation)

        for i in range(30):
            ga_instance_f.run()
            ga_instance_i.run()

            combined_population = numpy.concatenate((ga_instance_f.population, ga_instance_i.population))
            fitness_combined = numpy.concatenate(
                (ga_instance_f.last_generation_fitness, ga_instance_i.last_generation_fitness))

            sorted_indices = numpy.argsort(fitness_combined)[::-1]

            ga_instance_f.population[:, :] = combined_population[sorted_indices[:200], :]
            ga_instance_f.last_generation_fitness[:] = fitness_combined[sorted_indices[:200]]

            ga_instance_i.population[:, :] = combined_population[sorted_indices[200:], :]
            ga_instance_i.last_generation_fitness[:] = fitness_combined[sorted_indices[200:]]

        solution, solution_fitness, solution_idx = ga_instance_f.best_solution()

        print("\nSOLUTION MAX LENGTH: ", solution_fitness)
        print("SOLUTION AVERAGE LENGTH: ",
              sum(ga_instance_f.last_generation_fitness) / len(ga_instance_f.last_generation_fitness))
        ga_instance_f.plot_fitness()
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
            # if _ % 100 == 0:
            sys.stdout.write('\r' + "GENERATION STATUS: " + str(_))
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
