import numpy
import pygad

from Maze import Maze
from Astar import astar
from Solver import Solver
from Manager import Manager
import time
batchSize = 2000
solver = Solver()
manager = Manager(batchSize, 12, False, 3)


def fitness(ga_instance, solution, solution_idx):
    fitMaze = Maze(12, False)
    genes = [manager.genePool[int(i)] for i in numpy.round(solution).astype(int)]
    fitMaze.overrideFormGenes(12, 3, genes)
    status = solver.solveMaze(fitMaze)
    if status is not False:
        return status
    else:
        result = 0
        result += fitMaze.checkElevation()
        # result += fitMaze.checkMultipleThingsOnTile()
        result += fitMaze.checkDoors()
        result += fitMaze.checkKeys()
        # result += fitMaze.checkPlayerDoorAmount()

        if result == 0:
            return -0.1
        else:
            return result


if __name__ == '__main__':
    start = time.time()

    manager.generateShards()
    end = time.time()
    print("\n\nELAPSED TIME: ", end - start)
    manager.stats()
    # print("STARTING MAZE:\n")
    # print(manager.mazes[0].toString())
    # for gene in manager.genePool:
    #     print(gene.toString())

    num_solutions = 1200
    population_vector = numpy.zeros(shape=(num_solutions, 16))
    for solution_idx in range(num_solutions):
        initialPop = numpy.random.randint(0, batchSize * 16, size=16)
        initialPop = initialPop.astype(numpy.uint8)
        population_vector[solution_idx, :] = initialPop

    ga_instance = pygad.GA(num_generations=30,
                           num_parents_mating=2,
                           fitness_func=fitness,
                           num_genes=16,
                           initial_population=population_vector)

    ga_instance.run()
    ga_instance.plot_result()
    solution, solution_fitness, solution_idx = ga_instance.best_solution()
    # print("Parameters of the best solution : {solution}".format(solution=solution))
    print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
    # print("Index of the best solution : {solution_idx}".format(solution_idx=solution_idx))

    # maze = Maze(12, False)
    # print("OVERRIDEN MAZE:\n")
    # maze.overrideFormGenes(12, 3, manager.genePool)
    # maze.toString()
    # for mz in manager.mazes:
    #     mz.toString()
    # for temp in manager.shards:
    #     temp.toString()

    # solver = Solver()
    #
    # # i = 0
    # # while i < 2:
    # maze = Maze(4, False)
    #
    # player =      [[0, 2, 0, 0, 0],
    #                [0, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 1]]
    #
    # elevation =   [[2, 2, 2, 2, 2],
    #                [2, 2, 2, 2, 2],
    #                [2, 2, 2, 2, 2],
    #                [2, 2, 2, 2, 2],
    #                [2, 2, 2, 2, 2]]
    #
    # doors =       [[0, 0, 0, 0, 0],
    #                [0, 1, 1, 1, 1],
    #                [1, 0, 3, 3, 3],
    #                [1, 3, 0, 2, 2],
    #                [1, 3, 2, 0, 0]]
    #
    # keys =        [[0, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 0],
    #                [0, 1, 0, 0, 0],
    #                [0, 0, 3, 0, 0],
    #                [0, 0, 0, 2, 0]]
    #
    # maze.override(player, elevation, doors, keys, False, [False, False, False])
    # maze.toString()
    #
    # # print("\n\n\nRED KEY: " + str(maze.getKeyPos(1)))
    # # path = astar(maze, maze.startingPoint, maze.endingPoint)
    # Solver.solveMaze(solver, maze)

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
