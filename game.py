import pygame

from library import CheckPoint, Level, Player, Enemy
import os

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
FPS = 25


# level 1 set up
# //////////////////////////////////////////////////

# lvl1 img
lvl1_img = pygame.image.load(os.path.join('assets', 'level1.png'))
lvl1_img = pygame.transform.scale(lvl1_img, (550,290))

# lvl1 player
lvl1_player = Player(150, 390)

# lvl1 enemies
lvl1_e1 = Enemy(250, 200)
lvl1_e2 = Enemy(250, 250)
lvl1_e3 = Enemy(500, 250)
lvl1_e4 = Enemy(500, 300)
lvl1_eList = [lvl1_e1, lvl1_e2, lvl1_e3, lvl1_e4]

# lvl1 checkpoints
lvl1_cp1 = CheckPoint(113,359,100,70)
lvl1_cp2 = CheckPoint(540,160,100,70)
lvl1_cpList = [lvl1_cp1, lvl1_cp2]

# lvl1 build
lvl1 = Level(100,150, lvl1_img, lvl1_cpList, [], lvl1_eList, lvl1_player)



running = True
clock = pygame.time.Clock()
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys_pressed = pygame.key.get_pressed()

    lvl1.draw(SCREEN)
    lvl1.update(keys_pressed)
    


pygame.quit()








# fail_sound = pygame.mixer.Sound('crash.wav')
# music = pygame.mixer.music.load('music.wav')
# pygame.mixer.music.play(-1)


# def update():
#     keys = pygame.key.get_pressed()
#     player.move(keys)
#     enemy.move(250,500)
#     enemy2.move(250,500)
#     enemy3.move(250,500)
#     enemy4.move(250,500)
    
#     if player.draw(SCREEN).collidelist([enemy.draw(SCREEN), enemy2.draw(SCREEN), enemy3.draw(SCREEN), enemy4.draw(SCREEN)]) != -1:
#         # fail_sound.play()
#         player.reset()
#         player.deaths += 1
#     if player.draw(SCREEN).collidelist([endCP.draw(SCREEN)]) != -1:
#         print("Finished")


# def draw():
#     SCREEN.fill((183,175,250))
#     SCREEN.blit(levelImage, (100,150))
#     startCP.draw(SCREEN)
#     endCP.draw(SCREEN)
#     player.draw(SCREEN)
#     enemy.draw(SCREEN)
#     enemy2.draw(SCREEN)
#     enemy3.draw(SCREEN)
#     enemy4.draw(SCREEN)

#     deathCounter = font.render("Deaths: " + str(player.deaths), True, (255,255,255))
#     SCREEN.blit(deathCounter, (300,50))
    
#     pygame.display.update()


