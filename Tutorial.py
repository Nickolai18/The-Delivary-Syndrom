from GameObjectFunction import GameObjectFunction
from GameObjectPlayer import GameObjectPlayer
from GameObject import GameObject
from GameMap import GameMap
from TutorialBAttle import mainTutorialDoorToBattle
from TutorialCollect import mainTutorialDoorToCollect
from BaseMap import baseMap


def moveToRoomOfBattle():
    mainTutorialDoorToBattle()


def moveToRoomOfCollect():
    mainTutorialDoorToCollect()


def moveToBaseMap():
    baseMap()


def mainTutorial():
    mapObject = [
        GameObjectPlayer('Player', chr(214), [3, 3], 0),
        GameObjectFunction('DoorBattle', '|', [3, 0], 1, moveToRoomOfBattle),
        GameObjectFunction('DoorBattle', '--', [6, 3], 1, moveToBaseMap),
        GameObjectFunction('DoorCollect', '|', [3, 6], 1, moveToRoomOfCollect)
    ]


    m = GameMap([],7)
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


mainTutorial()

