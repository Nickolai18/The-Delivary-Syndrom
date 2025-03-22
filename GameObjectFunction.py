from GameObject import GameObject


class GameObjectFunction(GameObject):
    def __init__(self, name, symbol, position, isIterable, func):
        super().__init__(name, symbol, position, isIterable)
        self.func = func
