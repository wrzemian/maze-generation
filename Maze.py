import random


class Maze:
    doorArr = [False, False, False]

    def __init__(self, size=12, hasDoors=False):
        self.keys = None
        self.doors = None
        self.elevation = None
        self.player = None
        self.startingPoint = None
        self.endingPoint = None
        self.size = size
        self.hasDoors = hasDoors

        self.initPlayer()
        self.initElevation()
        if hasDoors:
            self.redKey = []
            self.greenKey = []
            self.blueKey = []
            self.initDoors()
            self.initKeys()

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

        doorNumber = random.randint(1, 3)
        if doorNumber != 0:
            for i in range(doorNumber):
                self.doorArr[i] = True

        for i in range(doorNumber + 1):
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
                        self.keys[x][y] = i+1
                        if i == 0:
                            self.redKey.append(x)
                            self.redKey.append(y)
                        if i == 1:
                            self.greenKey.append(x)
                            self.greenKey.append(y)
                        if i == 2:
                            self.blueKey.append(x)
                            self.blueKey.append(y)
                        break

    def toString(self):
        print("PLAYER")
        print('\n'.join(' '.join(str(x) for x in row) for row in self.player))
        print("\nELEVATION")
        print('\n'.join(' '.join(str(x) for x in row) for row in self.elevation))
        if self.hasDoors:
            print("\nDOOR TYPES\n")
            print(self.doorArr)
            print("\nDOORS")
            print('\n'.join(' '.join(str(x) for x in row) for row in self.doors))
            print("\nKEYS")
            print('\n'.join(' '.join(str(x) for x in row) for row in self.keys))
            print("\nRED KEY")
            print(self.redKey)
            print("\nGREEN KEY")
            print(self.greenKey)
            print("\nBLUE KEY")
            print(self.blueKey)
