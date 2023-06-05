import numpy
import pygad
import copy

from Maze import Maze
from Astar import astar
from Solver import Solver
from Manager import Manager
import time
batchSize = 100
mazeSize = 12
geneSize = 3
doorStatus = True
genesInSolution = int(int(mazeSize) ** 2 / int(geneSize) ** 2)
solver = Solver()
manager = Manager(batchSize, mazeSize, doorStatus, geneSize)
genePoolSize = 0


def fitness(ga_instance, solution, solution_idx):
    fitMaze = Maze(mazeSize, doorStatus)
    genes = [copy.deepcopy(manager.genePool[int(i)]) for i in numpy.round(solution).astype(int)]
    fitMaze.overrideFormGenes(mazeSize, geneSize, genes)
    # print("SOLUTION: {s}, START: {x}, STOP: {y}".
    #       format(s=solution_idx, x=fitMaze.findInArray(fitMaze.player, 1), y=fitMaze.findInArray(fitMaze.player, 2)))
    # fitMaze.toString()
    # status = False
    try:
        status = solver.solveMaze(fitMaze)
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
        fitMaze.toString(True)


def callback_generation(ga_instance):
    print('\r' + "Generation = {generation}, Fitness = {fitness}"
          .format(generation=ga_instance.generations_completed, fitness=ga_instance.best_solution()[1]), end='')


if __name__ == '__main__':
    start = time.time()

    manager.generateGenes()
    genePoolSize = len(manager.genePool)
    end = time.time()
    print("\n\nELAPSED TIME: ", end - start)
    manager.stats()

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

    ga_instance = pygad.GA(num_generations=30,
                           num_parents_mating=2,
                           fitness_func=fitness,
                           num_genes=genesInSolution,
                           initial_population=population_vector,
                           crossover_type="uniform",
                           crossover_probability=0.35,
                           mutation_type="random",
                           mutation_probability=0.25,
                           mutation_by_replacement=True,
                           random_mutation_min_val=0,
                           random_mutation_max_val=genePoolSize - 1,
                           on_generation=callback_generation)

    ga_instance.run()
    solution, solution_fitness, solution_idx = ga_instance.best_solution()
    ga_instance.plot_fitness()

    # solution, solution_fitness, solution_idx = ga_instance.best_solution()
    # print("Parameters of the best solution : {solution}".format(solution=solution))
    # print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
    # print("Index of the best solution : {solution_idx}".format(solution_idx=solution_idx))

    # overridenMaze = Maze(12, True)
    # print("OVERRIDEN MAZE:\n")
    # overridenMaze.overrideFormGenes(12, 3, manager.genePool)
    # overridenMaze.toString()
    # for mz in manager.mazes:
    #     mz.toString()

    # print(solver.solveMaze(overridenMaze))
    # for temp in manager.genePool:
    #     temp.toString()

    # solver = Solver()
    #
    # # i = 0
    # # while i < 2:
    # maze = Maze(12, doorStatus)
    #
    # player =      [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
    #                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                [0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0]]
    #
    # elevation =   [[4, 1, 3, 3, 5, 1, 5, 5, 1, 3, 1, 1],
    #                [6, 4, 3, 4, 4, 1, 5, 1, 3, 6, 3, 6],
    #                 [2, 3, 1, 6, 5, 6, 5, 3, 3, 3, 6, 4],
    #                 [5, 2, 5, 3, 5, 1, 4, 3, 6, 2, 2, 4],
    #                 [2, 1, 3, 6, 1, 1, 6, 4, 2, 6, 2, 5],
    #                 [6, 1, 3, 3, 1, 3, 4, 2, 3, 1, 5, 4],
    #                 [6, 2, 2, 5, 1, 4, 6, 5, 4, 3, 2, 6],
    #                 [4, 6, 5, 1, 6, 1, 3, 3, 1, 5, 4, 6],
    #                 [4, 1, 1, 4, 2, 1, 5, 1, 5, 5, 1, 6],
    #                 [1, 2, 6, 3, 1, 5, 4, 3, 6, 4, 6, 2],
    #                 [4, 2, 6, 3, 2, 1, 6, 3, 5, 5, 2, 6],
    #                 [3, 2, 1, 1, 2, 5, 6, 4, 3, 4, 1, 6]]
    #
    # doors =       [[0, 1, 0, 0, 0, 0, 3, 0, 0, 0, 2, 0],
    #                [0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 1],
    #                [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    #                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    #                [3, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0],
    #                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                [1, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 3]]
    #
    # keys =        [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
    #                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0]]
    #
    # maze.override(player, elevation, doors, keys, True, [False, False, False])
    # maze.toString()
    #
    # # print("\n\n\nRED KEY: " + str(maze.getKeyPos(1)))
    # path = astar(maze, maze.startingPoint, maze.endingPoint)
    # print("SOLVER RETURN VALUE: ", Solver.solveMaze(solver, maze))
    #
    # print("\n\nPATH")
    # print(path)
    # if path is not None:
    #     print("\nPATH VALUES")
    #     temp = []
    #     for pos in path:
    #         temp.append(maze.elevation[pos[0]][pos[1]])
    #     print(temp)
    #     print("\nMOVES REQUIRED")
    #     print(len(path) - 1)
    #     print("\n")
    # i += 1

    # print("\n\nSOLVER TOTAL")
    # print(solver.stats())
