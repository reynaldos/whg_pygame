import pygame

from library import CheckPoint, Player, Enemy
import os

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))




# fail_sound = pygame.mixer.Sound('crash.wav')
# music = pygame.mixer.music.load('music.wav')
# pygame.mixer.music.play(-1)

player = Player(150, 390, 10, 10)
enemy = Enemy(250, 200, 5, 5, 15)
enemy2 = Enemy(250, 250, 5, 5, 15)
enemy3 = Enemy(500, 250, 5, 5, 15)
enemy4 = Enemy(500, 300, 5, 5, 15)

levelImage = pygame.image.load(os.path.join('assets', 'level1.png'))
levelImage = pygame.transform.scale(levelImage, (550,290))

fieldStart = CheckPoint(113,359,100,70)
fieldFinish = CheckPoint(540,160,100,70)

font = pygame.font.Font('freesansbold.ttf', 32)

def update():
    keys = pygame.key.get_pressed()
    player.move(keys)
    enemy.move(250,500)
    enemy2.move(250,500)
    enemy3.move(250,500)
    enemy4.move(250,500)
    
    if player.draw(SCREEN).collidelist([enemy.draw(SCREEN), enemy2.draw(SCREEN), enemy3.draw(SCREEN), enemy4.draw(SCREEN)]) != -1:
        # fail_sound.play()
        player.reset()
        player.deaths += 1
    if player.draw(SCREEN).collidelist([fieldFinish.draw(SCREEN)]) != -1:
        print("Finished")

def draw():
    SCREEN.fill((183,175,250))
    SCREEN.blit(levelImage, (100,150))
    fieldStart.draw(SCREEN)
    fieldFinish.draw(SCREEN)
    player.draw(SCREEN)
    enemy.draw(SCREEN)
    enemy2.draw(SCREEN)
    enemy3.draw(SCREEN)
    enemy4.draw(SCREEN)

    deathCounter = font.render("Deaths: " + str(player.deaths), True, (255,255,255))
    SCREEN.blit(deathCounter, (300,50))
    
    pygame.display.update()



running = True
while running:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    update()
    
    draw()

    

pygame.quit()
