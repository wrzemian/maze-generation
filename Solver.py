from Astar import astar
import itertools


def solve_maze(maze):
    path = []
    key_arr = []

    def checkRoute(start, end, path):
        temp = astar(maze, start, end, path)
        if temp is not None:
            path += temp
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

        # print("start: ", start, "end:", end, "remainingKeys", remainingKeys)
        permutations = list(itertools.permutations(remainingKeys))
        # print("permutations:", permutations)
        for keys in permutations:
            new_keys = list(keys)[1:]
            # print("new keys:", new_keys)
            if new_keys is not None:
                # print(depth, "2nd checkroute, to key: ", keys[0])
                if checkRoute(start, keys[0], path):
                    print(path)
                    # print("status: ", maze.doorsStatus)
                    # print("2ND CHECKORUTE PASSED")
                    if not new_keys:
                        # print(depth, "3rd checkroute")
                        if checkRoute(keys[0], maze.endingPoint, path):
                            raise ValueError('\n\nREACHED EXIT')

                    for otherKey in new_keys:
                        # print("DUPA")
                        # print("key: ", otherKey)
                        logic(new_keys, keys[0], otherKey, path, depth + 1)

    if not maze.startingPoint:
        print("NO STARTING POINT")
        return False
    if len(maze.startingPoint) > 2:
        print("MORE THAN ONE STARTING POINT")
        return False

    if not maze.endingPoint:
        print("NO END")
        return False
    if len(maze.endingPoint) > 2:
        print("MORE THAN ONE END")
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
        # print("\n\nSTEPS: ", len(path))
        print(path)
        return len(path)
    else:
        # print("\n\nNO ROUTE")
        return False