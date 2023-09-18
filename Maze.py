import random

class Maze:

    def __init__(self, size=12, hasDoors=False):
        self.keys = None
        self.doors = None
        self.elevation = None
        self.player = None

        self.startingPoint = None
        self.endingPoint = None
        self.size = size
        self.hasDoors = hasDoors
        self.keysArr = [[], [], []]

    def randomize(self):
        self.keys = None
        self.doors = None
        self.elevation = None
        self.player = None
        self.startingPoint = None
        self.endingPoint = None
        self.keysArr = [[], [], []]

        self.initPlayer()
        self.initElevation()
        if self.hasDoors:
            self.initKeys()
            self.initDoors()

    def findInArray(self, where, what):
        outcome = []
        for i in range(self.size):
            for j in range(self.size):
                if where[i][j] == what:
                    outcome.append([i, j])
        return outcome

    def elevationAt(self, x, y):
        return self.elevation[x][y]

    def findKeys(self):
        for i in range(3):
            self.keysArr[i] = self.findInArray(self.keys, i+1)

    def overrideFormGenes(self, mazeSize, geneSize, genes):
        self.size = mazeSize
        self.player = [[0 for _ in range(mazeSize)] for _ in range(mazeSize)]
        self.elevation = [[0 for _ in range(mazeSize)] for _ in range(mazeSize)]
        self.doors = [[0 for _ in range(mazeSize)] for _ in range(mazeSize)]
        self.keys = [[0 for _ in range(mazeSize)] for _ in range(mazeSize)]
        block = [0, 0]

        for geneNR in range(len(genes)):
            for i in range(int(geneSize)):
                for j in range(int(geneSize)):
                    self.player[i + block[0]][j + block[1]] = genes[geneNR].player[i][j]
                    self.elevation[i + block[0]][j + block[1]] = genes[geneNR].elevation[i][j]
                    if genes[geneNR].hasDoors:
                        self.doors[i + block[0]][j + block[1]] = genes[geneNR].doors[i][j]
                        self.keys[i + block[0]][j + block[1]] = genes[geneNR].keys[i][j]
                        if genes[geneNR].keys[i][j] == 1:
                            self.keysArr[0].append(genes[geneNR].keys[i][j])
                        if genes[geneNR].keys[i][j] == 2:
                            self.keysArr[1].append(genes[geneNR].keys[i][j])
                        if genes[geneNR].keys[i][j] == 3:
                            self.keysArr[2].append(genes[geneNR].keys[i][j])
            block[0] += geneSize
            if block[0] >= mazeSize:
                block[0] = 0
                block[1] += geneSize
                if block[1] >= mazeSize:
                    block[1] = 0
        self.startingPoint = self.findInArray(self.player, 1)
        self.endingPoint = self.findInArray(self.player, 2)

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

    def initKeys(self):
        self.keys = [[0 for _ in range(self.size)] for _ in range(self.size)]

        for i in range(3):
            keyNumber = random.randint(0, self.size - 1)
            counter = 0
            while counter < keyNumber:
                x = random.randint(0, self.size - 1)
                y = random.randint(0, self.size - 1)
                if self.keys[x][y] == 0 and self.player[x][y] == 0:
                    self.keys[x][y] = i + 1
                    if i == 0:
                        self.keysArr[0].append([x, y])
                        counter += 1
                    if i == 1:
                        self.keysArr[1].append([x, y])
                        counter += 1
                    if i == 2:
                        self.keysArr[2].append([x, y])
                        counter += 1

    def initDoors(self):
        self.doors = [[0 for _ in range(self.size)] for _ in range(self.size)]

        for i in range(3):
            if self.keysArr[0]:
                for x in range(random.randint(1, self.size)):
                    while True:
                        x = random.randint(0, self.size - 1)
                        y = random.randint(0, self.size - 1)
                        if self.doors[x][y] == 0 and self.player[x][y] == 0 and self.keys[x][y] == 0:
                            self.doors[x][y] = i + 1
                            break

    def visualize(self, rich=False):
        if self.player:
            print("PLAYER")
            print('\n'.join(' '.join(str(x) for x in row) for row in self.player))
        if self.elevation:
            print("\nELEVATION")
            print('\n'.join(' '.join(str(x) for x in row) for row in self.elevation))
        if rich:
            print("\nSTART")
            print(self.startingPoint)
            print("\nEND")
            print(self.endingPoint)
        if self.hasDoors:
            if self.doors:
                print("\nDOORS")
                print('\n'.join(' '.join(str(x) for x in row) for row in self.doors))
            if self.keys:
                print("\nKEYS")
                print('\n'.join(' '.join(str(x) for x in row) for row in self.keys))
            if rich:
                print("\nRED KEYS")
                print(self.keysArr[0])
                print("\nGREEN KEYS")
                print(self.keysArr[1])
                print("\nBLUE KEYS")
                print(self.keysArr[2])


        print("\n\n")