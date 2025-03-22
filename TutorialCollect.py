from GameObject import GameObject
from GameMap import GameMap
from GameObjectFunction import GameObjectFunction
from GameObjectPlayer import GameObjectPlayer


def moveToRoomTutorial():
    from Tutorial import mainTutorial
    mainTutorial()


def mainTutorialDoorToCollect():
    mapObject = [
        GameObjectPlayer('Player', chr(214), [3, 1], 0),
        GameObjectFunction('DoorToTutorial', '|', [3, 0], 1, moveToRoomTutorial),
        GameObject('TrainingEnemy', chr(9813), [2, 4], 1),
        GameObject('TrainingEnemy', chr(9813), [2, 5], 1),
        GameObject('TrainingEnemy', chr(9813), [3, 4], 1),
        GameObject('TrainingEnemy', chr(9813), [3, 5], 1),
        GameObject('TrainingEnemy', chr(9813), [4, 4], 1),
        GameObject('TrainingEnemy', chr(9813), [4, 5], 1)
    ]

    m = GameMap([], 7)
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
            for item in mapObject:
                pos = item.getPosition()
                x = pos[0]
                y = pos[1]
                if pos == doorNearby:
                    item.func()
        else:
            m.update(move, mapObject[0].getPosition())
