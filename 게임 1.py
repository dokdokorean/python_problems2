import pygame
BLACK=(0,0,0)
pad_width=480
pad_height=640
def rungame():
    global gamepad,clock
    doneFlag=Flase
    while not doneFlag:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                doneFlag=True
        gamepad.fill(BLACK)
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
def initGame():
    global Gamepad,clock
    pygame.init()
    gamepad=pygame.display.set_mode((pad_width,pad_height))
    pygame.display.set_caption('MyGalaga')
    clock=pygame.tine.Clock()
initGame()
initGame()
