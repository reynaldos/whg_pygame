import pygame

RED = (255,0,0)
GREEN = (177,240,163)
BLUE = (0,0,255)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
PURPLE_BG = (183,175,250)

PLAYER_WIDTH = 20
PLAYER_VEL = 5

ENEMY_WIDTH = 10
ENEMY_VEL = 10

COIN_WIDTH = 4

pygame.init()
FONT = pygame.font.Font('freesansbold.ttf', 32)

# player class
class Player(pygame.Rect):
    def __init__(self, deaths = 0):
        self.x = -1
        self.y = -1
        self.width = PLAYER_WIDTH
        self.height = PLAYER_WIDTH
        self.vel = PLAYER_VEL
        self.color = RED
        self.deaths = deaths



    # player moves vel according to list of keys preseed
    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 100 + self.width:
            self.x -= self.vel
        if keys[pygame.K_RIGHT] and self.x < 630:
            self.x += self.vel
        if keys[pygame.K_DOWN] and self.y < 420:
            self.y += self.vel
        if keys[pygame.K_UP] and self.y > 150 + self.height:
            self.y -= self.vel

    # outline and shape get drawn to screen
    def draw(self, screen):
        self.mask = pygame.draw.rect(screen, (0,0,0), (self.x-2, self.y-2, self.width+4, self.height+4))
        return pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))


    # player gets reset at lastCP
    def reset(self):
        CP = self.lastCP
        self.x = (CP.x + CP.width/2) - self.width/2
        self.y = (CP.y + CP.height/2) - self.height/2

    
    def updateLastCP():
        pass



# checkpoint class
class CheckPoint(pygame.Rect):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = GREEN
        self.lastCP = -1
        self.capturedCoins = list()

    def draw(self, screen):
        return pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    
    def checkForCoins(self):
        pass



# enemy class
class Enemy():
    def __init__(self, x, y, right = True):
        self.x = x
        self.y = y
        self.width = ENEMY_WIDTH
        self.height = ENEMY_WIDTH
        self.vel = ENEMY_VEL
        self.color = BLUE
        self.right = right

    def draw(self, screen):
        self.mask = pygame.draw.circle(screen, (0,0,0), (self.x, self.y), self.width+2, self.height+2)
        return pygame.draw.circle(screen, self.color, (self.x, self.y), self.width, self.height)

    # back and forth movement
    def move(self, bound_x1, bound_x2):
        if self.x < bound_x1 or self.x > bound_x2:
            self.right = not self.right

        if self.right:
            self.x += self.vel
        else:
            self.x -= self.vel


# coin class
class Coin():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = COIN_WIDTH
        self.height = COIN_WIDTH
        self.color = YELLOW
       
    def draw(self, screen):
        self.mask = pygame.draw.circle(screen, (0,0,0), (self.x, self.y), self.width+2, self.height+2)
        return pygame.draw.circle(screen, self.color, (self.x, self.y), self.width, self.height)


# level class
class Level:
    def __init__(self, x, y, lvlImg, cpList, coinList, enemyList, player):
        self.x = x
        self.y = y
        self.lvlImg = lvlImg
        self.checkPoints = cpList
        self.startCP = cpList[0] # start cp is first cp in cpList
        self.endCP = cpList[len(cpList)-1] # end cp is last cp in cpList
        self.coinList = coinList
        self.enemyList = enemyList
        self.player = player
        self.player.lastCP = self.startCP
        self.player.reset()
        

    # draws level on screen
    def draw(self, screen):
        screen.fill(PURPLE_BG)
        screen.blit(self.lvlImg, (self.x, self.y))

        for cp in self.checkPoints:
            cp.draw(screen)

        for enemy in self.enemyList:
            enemy.draw(screen)

        self.player.draw(screen)

        deathCounter = FONT.render("Deaths: " + str(self.player.deaths), True, WHITE)
        screen.blit(deathCounter, (300,50))
    
        pygame.display.update()


    # level game logic
    def update(self,keys):
        self.player.move(keys)

        if self.player.mask.colliderect(self.endCP):
            print("Finished")

        for enemy in self.enemyList:
            enemy.move(250,550)

            if enemy.mask.collidelist([self.player.mask]) != -1:
                self.player.reset()  # better respawn logic needed
                self.player.deaths += 1
     
        
        # fail_sound.play()
            

        