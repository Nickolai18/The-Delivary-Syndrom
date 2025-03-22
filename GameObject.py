class GameObject:
    def __init__(self, name, symbol, position, isIterable):
        self.name = name
        self.symbol = symbol
        self.position = position
        self.isIterable = isIterable

    def getPosition(self):
        return self.position

    def getIterable(self):
        return self.isIterable

    def getSymbol(self):
        return self.symbol


# def isTrue(item):
#     print(item)
#
# ВАЖНАЯ ХРЕНЬ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# class GameObjectFunction(GameObject):
#     def __init__(self, name, symbol, position, isIterable, func):
#         super().__init__(name, symbol, position, isIterable)
#         self.func = func
#
#     def call(self, arg):
#         self.func(arg)
#
#
# wef = GameObjectFunction('DoorCollect', '|', [9, 6], 1, isTrue)
#
# print(wef.getPosition())
# wef.func('KO')
