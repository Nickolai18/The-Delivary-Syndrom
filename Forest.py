from GameObjectFunction import GameObjectFunction
from GameObjectPlayer import GameObjectPlayer
from GameMap import GameMap


def moveToBaseMap():
    from BaseMap import baseMap
    baseMap()


def mainForest():
    mapObject = [
        GameObjectPlayer('Player', chr(214), [6, 11], 0),
        GameObjectFunction('DoorCollect', '|', [6, 12], 1, moveToBaseMap)
    ]

    m = GameMap([], 13)
    m.render(mapObject)
    m.viewMap()
    while True:
        print("Input a - left")
        print("Input d - right")
        print("Input w - up")
        print("Input s - down")
        doorNearby = mapObject[0].doorIsNearby(mapObject)
        if doorNearby:
            print("Input e - attack")
        move = str(input())
        if move == 'e':
            print('OK')
            for item in mapObject:
                pos = item.getPosition()
                x = pos[0]
                y = pos[1]
                if pos == doorNearby:
                    item.func()
        else:
            m.update(move, mapObject[0].getPosition())