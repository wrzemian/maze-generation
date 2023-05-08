import random


class Maze:

    def __init__(self, size=12, hasDoors=False, dummy=False):
        self.keys = None
        self.doors = None
        self.elevation = None
        self.player = None
        self.startingPoint = None
        self.endingPoint = None
        self.doorNumber = None
        self.size = size
        self.hasDoors = hasDoors
        self.doorArr = [False, False, False]

        if not dummy:
            self.initPlayer()
            self.initElevation()
        if hasDoors:
            self.redKey = []
            self.greenKey = []
            self.blueKey = []
            self.doorsCoords = []
            self.doorsStatus = [False, False, False]
            if not dummy:
                self.initDoors()
                self.initKeys()

    def findInArray(self, where, what):
        outcome = []
        for i in range(self.size):
            for j in range(self.size):
                if where[i][j] == what:
                    outcome.append(i)
                    outcome.append(j)
                    return outcome

    def override(self, player, elevation, doors, keys, hasDoors=False, doorArr=[False, False, False]):
        self.size = len(player[0])
        self.hasDoors = hasDoors
        self.player = player
        self.elevation = elevation
        self.doors = doors
        self.keys = keys
        self.startingPoint = self.findInArray(self.player, 1)
        self.endingPoint = self.findInArray(self.player, 2)
        self.doorArr = doorArr

        if hasDoors:
            self.doorsCoords.append([0, 0])
            self.doorsCoords.append([0, 0])
            self.doorsCoords.append([0, 0])
            if self.doorArr[0]:
                self.doorNumber = 1
                self.redKey = self.findInArray(self.keys, 1)
                self.doorsCoords[0] = self.redKey
            else:
                self.redKey = []
                self.doorsCoords[0] = []

            if self.doorArr[1]:
                self.doorNumber = 2
                self.greenKey = self.findInArray(self.keys, 2)
                self.doorsCoords[1] = self.greenKey
            else:
                self.greenKey = []
                self.doorsCoords[1] = []

            if self.doorArr[2]:
                self.doorNumber = 3
                self.blueKey = self.findInArray(self.keys, 3)
                self.doorsCoords[2] = self.blueKey
            else:
                self.blueKey = []
                self.doorsCoords[2] = []

    def initPlayer(self):
        self.player = [[0 for _ in range(self.size)] for _ in range(self.size)]
        self.startingPoint = []
        self.startingPoint.append(random.randint(0, self.size - 1))
        self.startingPoint.append(random.randint(0, self.size - 1))
        self.player[self.startingPoint[0]][self.startingPoint[1]] = 1

        self.endingPoint = []
        self.endingPoint.append(random.randint(0, self.size - 1))
        self.endingPoint.append(random.randint(0, self.size - 1))
        while True:
            if self.player[self.endingPoint[0]][self.endingPoint[1]] != 1:
                self.player[self.endingPoint[0]][self.endingPoint[1]] = 2
                break
            else:
                self.endingPoint[0] = random.randint(0, self.size - 1)
                self.endingPoint[1] = random.randint(0, self.size - 1)

    def initElevation(self):
        self.elevation = [[random.randint(1, 6) for _ in range(self.size)] for _ in range(self.size)]

    def initDoors(self):
        self.doors = [[0 for _ in range(self.size)] for _ in range(self.size)]

        self.doorNumber = random.randint(1, 3)
        if self.doorNumber != 0:
            for i in range(self.doorNumber):
                self.doorArr[i] = True

        for i in range(self.doorNumber + 1):
            for x in range(random.randint(1, self.size)):
                while True:
                    x = random.randint(0, self.size - 1)
                    y = random.randint(0, self.size - 1)
                    if self.doors[x][y] == 0 and self.player[x][y] == 0:
                        self.doors[x][y] = i
                        break

    def initKeys(self):
        self.keys = [[0 for _ in range(self.size)] for _ in range(self.size)]

        for i in range(len(self.doorArr)):
            if self.doorArr[i]:
                while True:
                    x = random.randint(0, self.size - 1)
                    y = random.randint(0, self.size - 1)
                    if self.keys[x][y] == 0 and self.player[x][y] == 0 and self.doors[x][y] == 0:
                        self.keys[x][y] = i + 1
                        if i == 0:
                            self.redKey.append(x)
                            self.redKey.append(y)
                            self.doorsCoords.append(self.redKey)
                        if i == 1:
                            self.greenKey.append(x)
                            self.greenKey.append(y)
                            self.doorsCoords.append(self.greenKey)
                        if i == 2:
                            self.blueKey.append(x)
                            self.blueKey.append(y)
                            self.doorsCoords.append(self.blueKey)
                        break

    def getKeyPos(self, number):
        return self.doorsCoords[number - 1]

    def openDoors(self, number):
        self.doorsStatus[number - 1] = True

    def toString(self, rich=False):
        print("PLAYER")
        print('\n'.join(' '.join(str(x) for x in row) for row in self.player))
        print("\nELEVATION")
        print('\n'.join(' '.join(str(x) for x in row) for row in self.elevation))
        if self.hasDoors:
            if rich:
                print("\nDOOR TYPES")
                print(self.doorArr)
                print("\nDOOR NUMBER")
                print(self.doorNumber)
            print("\nDOORS")
            print('\n'.join(' '.join(str(x) for x in row) for row in self.doors))
            print("\nKEYS")
            print('\n'.join(' '.join(str(x) for x in row) for row in self.keys))
            if rich:
                print("\nSTART")
                print(self.startingPoint)
                print("\nEND")
                print(self.endingPoint)
                print("\nRED KEY")
                print(self.redKey)
                print("\nGREEN KEY")
                print(self.greenKey)
                print("\nBLUE KEY")
                print(self.blueKey)
        print("\n\n")
