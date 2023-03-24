import random


class Maze:
    size = 12
    player = 0
    elevation = 0
    doors = 0
    keys = 0
    isDoors = False
    doorArr = [False, False, False]

    def initPlayer(self):
        self.player = [[0 for x in range(self.size)] for y in range(self.size)]
        self.player[random.randint(0, self.size-1)][random.randint(0, self.size-1)] = 1

        while True:
            x = random.randint(0, self.size-1)
            y = random.randint(0, self.size-1)
            if self.player[x][y] != 1:
                self.player[x][y] = 2
                break

    def initElevation(self):
        self.elevation = [[random.randint(1, 6) for x in range(self.size)] for y in range(self.size)]

    def initDoors(self):
        self.doors = [[0 for x in range(self.size)] for y in range(self.size)]

        doorNumber = random.randint(0, 3)
        if doorNumber != 0:
            for i in range(doorNumber):
                self.doorArr[i] = True

        for i in range(doorNumber+1):
            while True:
                x = random.randint(0, self.size-1)
                y = random.randint(0, self.size-1)
                if self.doors[x][y] == 0:
                    self.doors[x][y] = i
                    break

