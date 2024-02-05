from math import factorial
from Astar import astar
import itertools
import gc

def solve_maze(maze):
    path = []
    key_arr = []
    cache = {}

    def is_nested(input_list):
        if isinstance(input_list, list):
            if any(isinstance(item, list) for item in input_list):
                return True
            else:
                return False
        else:
            return False

    def checkRoute(start, end, path):
        if is_nested(start):
            start = start[0]
        if is_nested(end):
            end = end[0]

        cache_key = (tuple(start), tuple(end))

        if cache_key in cache:
            cached_path = cache[cache_key]
            path.extend(cached_path)
            return True

        temp = astar(maze, start, end, path)
        if temp is not None:
            path.extend(temp)
            cache[cache_key] = temp
            return True
        else:
            return False

    def createKeyArr():
        for arr in maze.keysArr:
            for key in arr:
                key_arr.append(key)

    def logic(remainingKeys, start, end, path, depth=0):
        start = list(start)
        end = list(end)
        if checkRoute(start, maze.endingPoint, path):
            raise ValueError('\n\nREACHED EXIT')

        if not remainingKeys:
            return

        total_permutations = factorial(len(remainingKeys))
        checked_permutations = 0

        for keys in itertools.permutations(remainingKeys):
            if depth == 0:
                checked_permutations += 1
                print(checked_permutations, "/", total_permutations, "klucze:", keys)

            new_keys = list(keys)[1:]
            if new_keys is not None:
                if checkRoute(start, keys[0], path):
                    if not new_keys:
                        if checkRoute(keys[0], maze.endingPoint, path):
                            raise ValueError('\n\nREACHED EXIT')
                    for otherKey in new_keys:
                        logic(new_keys, keys[0], otherKey, path, depth + 1)

    if not maze.startingPoint:
        return False
    if len(maze.startingPoint) > 2:
        return False

    if not maze.endingPoint:
        return False
    if len(maze.endingPoint) > 2:
        return False

    createKeyArr()
    # print("START:", maze.startingPoint, "END:", maze.endingPoint)
    try:
        if maze.hasDoors:
            logic(key_arr, maze.startingPoint, maze.endingPoint, path)
        else:
            if checkRoute(maze.startingPoint, maze.endingPoint, path):
                raise ValueError('\n\nREACHED EXIT')
    except ValueError as e:
        # print(e)
        print("STEPS: ", len(path))
        # print(path)
        return len(path)-1
    else:
        # print("NO ROUTE")
        return False