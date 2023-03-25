import random


class Maze:
    size = 12
    player = []
    elevation = []
    doors = []
    keys = []
    isDoors = False
    doorArr = [False, False, False]

    def __init__(self, size, isDoors):
        print("starting constructor")
        self.size = size
        self.isDoors = isDoors
        self.initPlayer()
        self.initElevation()
        if isDoors:
            self.initDoors()
            self.initKeys()

    def initPlayer(self):
        print("initing player")
        self.player = [[0 for x in range(self.size)] for y in range(self.size)]
        self.player[random.randint(0, self.size - 1)][random.randint(0, self.size - 1)] = 1

        while True:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            if self.player[x][y] != 1:
                self.player[x][y] = 2
                break
        print("finished initing player")

    def initElevation(self):
        self.elevation = [[random.randint(1, 6) for x in range(self.size)] for y in range(self.size)]

    def initDoors(self):
        self.doors = [[0 for x in range(self.size)] for y in range(self.size)]

        doorNumber = random.randint(0, 3)
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
        self.keys = [[0 for x in range(self.size)] for y in range(self.size)]

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
        if self.isDoors:
            # print(self.doorArr)
            print("\nDOORS")
            print('\n'.join(' '.join(str(x) for x in row) for row in self.doors))
            print("\nKEYS")
            print('\n'.join(' '.join(str(x) for x in row) for row in self.keys))
