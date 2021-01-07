import random
import time

def displayIntro():
    print('俄罗斯轮盘')
    print()

def chooseCave():
    cave = ''
    while cave!='1'and cave!='2'and cave!='3':
        print('Well, choose a gun and shoot it.(1 or 2 or 3)')
        cave=input()

    return cave

def checkCave(chonsenCave):
    print('You chose a gun...')
    time.sleep(2)
    print('Put it ')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 3)

    if chonsenCave == str(friendlyCave):
        print('Lucky!')
    else:
        print('What a pity,now pay the consequence.')

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print('Do you want to play again?(yes or no)')
    playAgain = input()