import pygame

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# checkpoint class
class CheckPoint:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = GREEN

    def draw(self, screen):
        return pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))


# player class
class Player:
    def __init__(self, x, y, width, height, vel=5, deaths = 0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
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
        pygame.draw.rect(screen, (0,0,0), (self.x-2, self.y-2, self.width+4, self.height+4))
        return pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))


    # player gets reset at lastCP
    def reset(self, CP: CheckPoint):
        self.x = CP.x
        self.y = CP.y


# enemy class
class Enemy:
    def __init__(self, x, y, width, height, vel=5, right = True):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.color = BLUE
        self.right = right

    def draw(self, screen):
        pygame.draw.circle(screen, (0,0,0), (self.x, self.y), self.width+2, self.height+2)
        return pygame.draw.circle(screen, self.color, (self.x, self.y), self.width, self.height)

    # back and forth movement
    def move(self, bound_x1, bound_x2):
        if self.x < bound_x1 or self.x > bound_x2:
            self.right = not self.right
        if self.right:
            self.x += self.vel
        else:
            self.x -= self.vel