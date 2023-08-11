import pygmae
BLACK=(0,0,0)
pad_width=480
pad_height=640
fighter_width=36
fighter_height=38
def drawObject(obj,x,y):
    global gmaepad
    gamepad.blit(obj,(x,y,))
def runGame():
    global gamepad,clock,fighter
    x=pad_width*0.45
    y=pad_height*0.9
    x_change=0
    ongame=False
    while not ongame:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                ongame=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT
                x_change-=5
            elif event.key==pygame.K_RIGHT:
                x_change+=5
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event,key==pygame.K_RIGHT:
                    x_change=0
        gameapd.fill(BLACK)
        x+=x_change
        if x<0:
            x=0
        elif x>pad_width-fighter_width:
            x=pad_width-fighter_width
        draw object(fighter,x,y)
        pygame.display.update
        
                
