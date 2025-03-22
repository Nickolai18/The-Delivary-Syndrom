class GameMap:
    def __init__(self, map, size):
        self.map = map
        self.size = size

    def render(self, objectMassive):
        for i in range(self.size):
            self.map.append([])
            for j in range(self.size):
                isThere = False
                symbol = 0
                for item in objectMassive:
                    pos = item.getPosition()
                    x = pos[0]
                    y = pos[1]
                    if i == x and j == y:
                        isThere = True
                        symbol = item.getSymbol()
                if isThere:
                    self.map[i].append(symbol)
                elif i == 0 or i == (self.size - 1):
                    self.map[i].append('#')
                elif j == 0 or j == (self.size - 1):
                    self.map[i].append('#')
                else:
                    self.map[i].append(' ')

    def update(self, move, pos):

        match move:
            case 'a':
                if self.map[pos[0]][pos[1] - 1] == "#" or self.map[pos[0]][pos[1] - 1] == "e" or self.map[pos[0]][
                    pos[1] - 1] == "|":
                    print("Ты не можешь двигаться в ту сторону")
                    self.viewMap()
                else:
                    self.map[pos[0]][pos[1] - 1], self.map[pos[0]][pos[1]] = self.map[pos[0]][pos[1]], self.map[pos[0]][
                        pos[1] - 1]
                    pos[1] = pos[1] - 1
                    self.viewMap()
            case 'd':
                if self.map[pos[0]][pos[1] + 1] == "#" or self.map[pos[0]][pos[1] + 1] == "e" or self.map[pos[0]][
                    pos[1] + 1] == "|":
                    print("Ты не можешь двигаться в ту сторону")
                    self.viewMap()
                else:
                    self.map[pos[0]][pos[1] + 1], self.map[pos[0]][pos[1]] = self.map[pos[0]][pos[1]], self.map[pos[0]][
                        pos[1] + 1]
                    pos[1] = pos[1] + 1
                    self.viewMap()
            case 'w':
                if self.map[pos[0] - 1][pos[1]] == "#" or self.map[pos[0] - 1][pos[1]] == "e" or self.map[pos[0] - 1][
                    pos[1]] == "|":
                    print("Ты не можешь двигаться в ту сторону")
                    self.viewMap()
                else:
                    self.map[pos[0] - 1][pos[1]], self.map[pos[0]][pos[1]] = self.map[pos[0]][pos[1]], \
                        self.map[pos[0] - 1][pos[1]]
                    pos[0] = pos[0] - 1
                    self.viewMap()
            case 's':
                if self.map[pos[0] + 1][pos[1]] == "#" or self.map[pos[0] + 1][pos[1]] == "e" or self.map[pos[0] + 1][
                    pos[1]] == "|":
                    print("Ты не можешь двигаться в ту сторону")
                    self.viewMap()
                else:
                    self.map[pos[0] + 1][pos[1]], self.map[pos[0]][pos[1]] = self.map[pos[0]][pos[1]], \
                        self.map[pos[0] + 1][pos[1]]
                    pos[0] = pos[0] + 1
                    self.viewMap()


    def viewMap(self):
        for i in range(self.size):
            print(self.map[i])


# m = GameMap([], 7)
# m.render(mapObject)
# m.viewMap()
# m.update('s', mapObject[0].getPosition())
# print(mapObject[0].getPosition())
# m.update('a', mapObject[0].getPosition())
# print(mapObject[0].getPosition())
# m.update('a', mapObject[0].getPosition())
# print(mapObject[0].getPosition())
# m.update('a', mapObject[0].getPosition())
# print(mapObject[0].getPosition())
# m.update('a', mapObject[0].getPosition())
# print(mapObject[0].getPosition())
