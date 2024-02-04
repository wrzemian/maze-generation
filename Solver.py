from math import factorial
from Astar import astar
import itertools


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

        # print("start: ", start, "end:", end, "remainingKeys", remainingKeys)
        for keys in itertools.permutations(remainingKeys):
            if depth == 0:
                checked_permutations += 1
                print(f"  {checked_permutations / total_permutations * 100:.2f}%, klucze:", keys)

            new_keys = list(keys)[1:]
            # print("keys:", keys)
            # print("new keys:", new_keys)
            if new_keys is not None:
                # print(depth, "2nd checkroute, to key: ", keys[0])
                # print("0TH: ", path)
                if checkRoute(start, keys[0], path):
                    # print("2ND: ", path)
                    # print("2ND CHECKORUTE PASSED")
                    if not new_keys:
                        # print(depth, "3rd checkroute")
                        if checkRoute(keys[0], maze.endingPoint, path):
                            # print("3RD: ", path)
                            raise ValueError('\n\nREACHED EXIT')

                    for otherKey in new_keys:
                        # print("key: ", otherKey)
                        logic(new_keys, keys[0], otherKey, path, depth + 1)

    if not maze.startingPoint:
        # print("NO STARTING POINT")
        return False
    if len(maze.startingPoint) > 2:
        # print("MORE THAN ONE STARTING POINT")
        return False

    if not maze.endingPoint:
        # print("NO END")
        return False
    if len(maze.endingPoint) > 2:
        # print("MORE THAN ONE END")
        return False

    createKeyArr()
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
        print("NO ROUTE")
        return False