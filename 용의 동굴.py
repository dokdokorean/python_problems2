import random
import time
def displayIntro():
     print('You are in a land full of dragons.In front fo you.')
     print('yousee two caves.in onw cave, the dragon is friendly')
     print('and will share his treadure with you. The dother dragon')
     print('is greedy and hungry, and will eat you on sight.')
     print()
def chooseCave():
    cave=''
    while cave != '1' and cave !='2':
           print('which cave will you go into?(1 or 2)')
           cave= input()

    return cave

def checkCave(chosenCave):
    print('you apporach the cave...')
    time.sleep(2)
    print('it is dark and spooky...')
    time. sleep(2)
    print(' A large dragon jumps ouy in fornt of you! He opens his jaw and...')
    print()
    time.sleep(2)

    friendlyCave= random.randint(1,2)
    if chosenCave== str(friendlyCave):
        print('Gives you his treasure!')
    else:
        print('Gobbles you down in one bite!')

playagain='yes'
while playagain == 'yes'or playagain== 'y':
     displayIntro()
     cavenumber = chooseCave()
     checkCave(cavenumber)
     print('Do you want to play again?( yes or no)')
     playagain=input()
           
if playagain=='no' or playagain=='n':
    print('Thanks for playing!')
    
