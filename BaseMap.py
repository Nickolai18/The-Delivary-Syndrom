from GameObjectFunction import GameObjectFunction
from GameObjectPlayer import GameObjectPlayer
from GameMap import GameMap
from GameObject import GameObject


def moveToLake():
    from Lake import mainLake
    mainLake()


def moveToForest():
    from Forest import mainForest
    mainForest()


def moveToRoad():
    from Road import mainRoad
    mainRoad()


def baseMap():
    mapObject = [
        # Главный персонаж
        GameObjectPlayer('Player', chr(214), [1, 7], 0),
        # Интерактивные объекты
        GameObjectFunction('DoorBattle', '|', [7, 14], 1, moveToLake),
        GameObjectFunction('DoorBattle', '|', [7, 0], 1, moveToForest),
        GameObjectFunction('DoorCollect', '--', [14, 7], 1, moveToRoad),
        # NPC
        GameObject('Road', chr(9823), [5, 11], 0),
        GameObject('Road', chr(9823), [2, 11], 0),
        GameObject('Road', chr(9823), [1, 10], 0),
        GameObject('Road', chr(9823), [4, 4], 0),
        GameObject('Road', chr(9823), [5, 5], 0),
        GameObject('Road', chr(9823), [4, 2], 0),
        GameObject('Road', chr(9813), [9, 10], 0),
        # Объекты карты
        # Дорога по горизонтале
        # GameObject('Road', chr(8214), [5, 7], 0),
        # GameObject('Road', chr(8214), [6, 7], 0),
        # GameObject('Road', chr(8214), [8, 7], 0),
        # GameObject('Road', chr(8214), [9, 7], 0),
        # GameObject('Road', chr(8214), [10, 7], 0),
        # GameObject('Road', chr(8214), [11, 7], 0),
        # GameObject('Road', chr(8214), [12, 7], 0),
        # GameObject('Road', chr(8214), [13, 7], 0),
        # # Дорога по вертикале
        # GameObject('Road', '=', [7, 1], 0),
        # GameObject('Road', '=', [7, 2], 0),
        # GameObject('Road', '=', [7, 3], 0),
        # GameObject('Road', '=', [7, 4], 0),
        # GameObject('Road', '=', [7, 5], 0),
        # GameObject('Road', '=', [7, 6], 0),
        # GameObject('Road', '=', [7, 7], 0),
        # GameObject('Road', '=', [7, 8], 0),
        # GameObject('Road', '=', [7, 9], 0),
        # GameObject('Road', '=', [7, 10], 0),
        # GameObject('Road', '=', [7, 11], 0),
        # GameObject('Road', '=', [7, 12], 0),
        # GameObject('Road', '=', [7, 13], 0),
        # Дома
        GameObject('Road', chr(9978), [1, 1], 0),
        GameObject('Road', chr(9978), [3, 2], 0),
        GameObject('Road', chr(9978), [2, 3], 0),
        GameObject('Road', chr(9978), [5, 4], 0),
        GameObject('Road', chr(9978), [4, 5], 0),
        GameObject('Road', chr(9978), [1, 11], 0),
        GameObject('Road', chr(9978), [5, 12], 0),
        GameObject('Road', chr(9978), [2, 10], 0),
        GameObject('Road', chr(9962), [10, 10], 0),
        # Забор
        GameObject('Road', '|', [11, 11], 0),
        GameObject('Road', '|', [12, 11], 0),
        GameObject('Road', '|', [13, 11], 0),
        GameObject('Road', '|', [10, 11], 0),
        GameObject('Road', '-', [10, 13], 0),
        # Трава
        GameObject('Road', chr(9618), [11, 12], 0),
        GameObject('Road', chr(9618), [12, 12], 0),
        GameObject('Road', chr(9618), [13, 12], 0),
        GameObject('Road', chr(9618), [11, 13], 0),
        GameObject('Road', chr(9618), [12, 13], 0),
        GameObject('Road', chr(9618), [13, 13], 0),

    ]
    m = GameMap([], 15)
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

baseMap()
