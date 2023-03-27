import random


class Maze:
    doorArr = [False, False, False]

    def __init__(self, size=12, hasDoors=False):
        self.keys = None
        self.doors = None
        self.elevation = None
        self.player = None
        self.size = size
        self.hasDoors = hasDoors
        self.initPlayer()
        self.initElevation()
        if hasDoors:
            self.initDoors()
            self.initKeys()

    def initPlayer(self):
        self.player = [[0 for _ in range(self.size)] for _ in range(self.size)]
        self.player[random.randint(0, self.size - 1)][random.randint(0, self.size - 1)] = 1

        while True:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            if self.player[x][y] != 1:
                self.player[x][y] = 2
                break

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
                        break

    def toString(self):
        print("PLAYER")
        print('\n'.join(' '.join(str(x) for x in row) for row in self.player))
        print("\nELEVATION")
        print('\n'.join(' '.join(str(x) for x in row) for row in self.elevation))
        if self.hasDoors:
            # print(self.doorArr)
            print("\nDOORS")
            print('\n'.join(' '.join(str(x) for x in row) for row in self.doors))
            print("\nKEYS")
            print('\n'.join(' '.join(str(x) for x in row) for row in self.keys))
