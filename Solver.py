from Astar import astar
import itertools


class Solver:
    def __init__(self):
        self.totalSteps = []
        self.finishedMazes = []
        self.failedMazes = []
        self.steps = 0

    def solveMaze(self, maze):
        self.steps = 0
        keyArr = []

        def checkRoute(start, end, path):
            print("\n" + str(start) + " -> " + str(end))
            temp = astar(maze, start, end)
            print("TEMP: ", temp)
            if temp is not None:
                path += temp[1:]
                print("PATH: ", path)
                return True
            else:
                return False

        def createKeyArr():
            for i in range(maze.doorNumber):
                keyArr.append(i + 1)

        def logic(remainingKeys, start, end, path, depth=0):
            print(depth, "===============================================")
            print(depth, "1st checkroute")
            if checkRoute(start, maze.endingPoint, path):
                return True

            # print("start: ", start, "end:", end, "remainingKeys", remainingKeys)
            permutations = list(itertools.permutations(remainingKeys))
            # print("permutations:", permutations)
            for keys in permutations:
                # print(">>>")
                # print("permutations:", permutations)
                # print("keys:", keys)
                # print("<<<")
                new_keys = list(keys)[1:]
                # print("new keys:", new_keys)

                print(depth, "2nd checkroute, new keys: ", new_keys)
                if checkRoute(start, maze.getKeyPos(keys[0]), path):
                    maze.openDoors(keys[0])
                    # print("status: ", maze.doorsStatus)
                    # print("2ND CHECKORUTE PASSED")
                    if new_keys == []:
                        print(depth, "3rd checkroute")
                        if checkRoute(maze.getKeyPos(keys[0]), maze.endingPoint, path):
                            raise ValueError('reached exit')

                    for otherKey in new_keys:
                        print("DUPA")
                        # print("key: ", otherKey, "keyPos:", maze.getKeyPos(otherKey))
                        logic(new_keys, maze.getKeyPos(keys[0]), maze.getKeyPos(otherKey), path, depth + 1)
                # else:
                # print("2ND CHECKROUTE FAILED!!!!")

        createKeyArr()
        path = []
        try:
            logic(keyArr, maze.startingPoint, maze.endingPoint, path)
        except ValueError as e:
            print(e)
        print("\n\nSTEPS")
        print(len(path))

    def stats(self):
        for i in range(len(self.usingDoors)):
            if self.usingDoors[i]:
                self.allMazes[i].toString(True)

        return sum(self.totalSteps)
