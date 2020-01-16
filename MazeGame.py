import pygame
import random



dead = False

class Player(object):
    
    def __init__(self):
        self.rect = pygame.Rect(32, 32, 16, 16)

        self.xmov=0
        self.ymov=0

    
    def pos(self):
        '''
        als WASD word ingedrukt beweeg in bij behorende richting
        '''
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_s]:
            self.move(0,2)
        if keys[pygame.K_d]:
            self.move(2,0)
        if keys[pygame.K_a]:
            self.move(-2,0)
        if keys[pygame.K_w]:
            self.move(0,-2)

                

    def move(self, dx, dy):
        
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)
    
    def move_single_axis(self, dx, dy):
        

        self.rect.x += dx
        self.rect.y += dy

        for wall in walls:
            '''
            als speler collide met muur
            tegenhouden en terug duwen
            '''    
            if self.rect.colliderect(wall.rect):
                if dx > 0: 
                    self.rect.right = wall.rect.left
                if dx < 0: 
                    self.rect.left = wall.rect.right
                if dy > 0: 
                    self.rect.bottom = wall.rect.top
                
                if dy < 0: # 
                    self.rect.top = wall.rect.bottom
        
        for lava in lava_blocks:
            '''
            als speler lava raakt eidig spel
            '''
            if self.rect.colliderect(lava.rect):
                exit()
            

            
        
    
player = Player()

class Wall(object):
    
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

class Lava(object):
    def __init__(self, pos):
        lava_blocks.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)




pygame.init()



pygame.display.set_caption("Get to the red square!")
screen = pygame.display.set_mode((640, 240))  #Zet scherm grootte
image = pygame.image.load("Tiles.png")



level1 = [
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "WLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLW",
    "WLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLW",
    "WLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLW",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W                                       W",
    "W                                       W",
    "WS                                     EW",
    "W                                       W",
    "W                                       W",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "WLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLW",
    "WLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLW",
    "WLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLW",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
]
level2 = [
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    
    "LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL",
    "LLLLLLLLLLLLLLLLLLLLLLWWWWWWWWWWWWWLLLLLL",
    "LLLLLLLLLLLLLLLLLLLLLLW           WLLLLLL",
    "LLLLLLLLLLLLLLLLLLLLLLW           WLLLLLL",
    "WWWWWWWWWLWWWWWWWWWWWWW  WWWWWW   WWWWWWW",
    "W        L      L           L           W",
    "WS       L      L     L     L          EW",
    "W        L            L     L           W",
    "WWWWW   WWWW   WWWWWWWWWWWWWWWWWWWWWWWWWW",
    "LLLLW          WLLLLLLLLLLLLLLLLLLLLLLLLL",
    "LLLLW          WLLLLLLLLLLLLLLLLLLLLLLLLL",
    "LLLLWWWWWWWWWWWWLLLLLLLLLLLLLLLLLLLLLLLLL",
    "LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",   
]
level3 = [
    
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "WS       L              L               W",
    "W               L               L       W",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW       W",
    "W            L                          W",
    "W                 LLL                   W",
    "W        L                      L       W",
    "W        WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W                LLLLLLLLLLLLLLLLLLLLLLLW",
    "W                                       W",
    "WLLLLLLLLLLLLLL                         W",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW       W",
    "WLLLL       L      L      L             W",
    "WE       L      L      L      L         W",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
]
level4 = [
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "WS      L             W            WLLLLL",
    "W       L      L         LLLL      WLLLLL",
    "W       L      L      W            WLLLLL",
    "W              L      W            WLLLLL",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW  WWWWWW",
    "W             L             W           W",
    "W        L                  L           W",
    "W        L          L                   W",
    "WLL   LLWWWWWWWWWWWWWWWWWWWWW           W",
    "W         L        L        L           W",
    "WLLLL          L       L    WWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWWWWWW    WLLLLLLLLLLLL",
    "WE                          WLLLLLLLLLLLL",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
]
level5 = [
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL",
    "LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL",
    "WWWWWWLWWWWLWWWWLWWWWLWWWWWWWWWLWWWWWWWWW",
    "W     L    L    L    L    L    L         W",
    "W     L         L    L    L    L         W",
    "W     L    L    L    L    L    L         W",
    "WS    L    L    L         L             EW",
    "W          L    L    L    L    L         W",
    "W     L    L         L    L    L         W",
    "W     L    L    L    L         L         W",
    "WWWWWWLWWWWLWWWWLWWWWLWWWWLWWWWLWWWWWWWWWW",
    "LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL",
    "LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
]

levels = [level1,level2,level3,level4,level5]
currentLevel = 0

def load_level(level):
    '''
    voor elke S,W,E,L maak bij behorend blok
    '''
    global end_rect, walls, lava_blocks
    lava_blocks = []
    walls = [] 
    x = 0
    y = 0
    for row in level:
        for col in row:
            if col == "W":
                Wall((x, y))
            elif col == "E":
                end_rect = pygame.Rect(x, y, 16, 16)
            elif col == "S":
                player.rect = pygame.Rect(x, y, 16, 16)
            elif col == "L":
                Lava((x, y))

                
            x += 16
        y += 16
        x = 0
    


clock = pygame.time.Clock()







load_level(levels[currentLevel])

running = True
while running:
    

    if player.rect.colliderect(end_rect):
        '''
        als speler collide met eindpunt
        speel geluid en ga naar volgend level
        '''   
        print('Level',currentLevel + 1,'gehaald')
        pygame.mixer.music.load('LevelUp.wav')
        pygame.mixer.music.play(0)
        currentLevel += 1
        
        load_level(levels[currentLevel])
        screen.fill((0, 0, 0))

    clock.tick(60)
    player.pos()
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False
    
    
    # Teken het scherm
    screen.blit(image, [0, 0])
    for wall in walls:
        pygame.draw.rect(screen, (0), wall.rect)
    pygame.draw.rect(screen, (255, 200, 0), end_rect)
    pygame.draw.rect(screen,(255, 0.4, 0.5), player.rect)
    for lava in lava_blocks:
        pygame.draw.rect(screen,(200, 100, 0.5), lava.rect)
    pygame.display.update()

pygame.QUIT