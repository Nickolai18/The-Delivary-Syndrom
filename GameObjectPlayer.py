from GameObject import GameObject


class GameObjectPlayer(GameObject):
    def doorIsNearby(self, objectMassive):
        posPlayer = objectMassive[0].getPosition()
        for item in objectMassive:
            pos = item.getPosition()
            x = pos[0]
            y = pos[1]
            if item.getSymbol() == '|' or item.getSymbol() == '--':
                if x == (posPlayer[0] + 1) or x == (posPlayer[0] - 1) or y == (posPlayer[1] + 1) or y == (posPlayer[1] - 1):
                    return pos
