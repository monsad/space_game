import pygame
import random
import math
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800, 600))


pygame.display.set_caption("Space Invaders")

background = pygame.image.load('back.jpg')

mixer.music.load("back.wav")
mixer.music.play(-1)


#gracz
playerImg = pygame.image.load("ufo.png")
playerX = 370
playerY = 480
playerX_change = 0

#monster
monsterImg = []
monsterX = []
monsterY = []
monsterX_change = []
monsterY_change = []
num_of_monster = 6

for i in range(num_of_monster):
    monsterImg.append(pygame.image.load("monster.png"))
    monsterX.append(random.randint(0, 735))
    monsterY.append(random.randint(55, 159))
    monsterX_change.append(4)
    monsterY_change.append(40)

bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = 'ready'







#funkce

def monster(x, y, i):
    screen.blit(monsterImg[i], (x,y))



def player(x, y):
    screen.blit(playerImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(monsterX, monsterY, bulletX, bulletY):
    distance = math.sqrt(math.pow(monsterX-bulletX, 2)) + (math.pow((monsterY-bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False



running = True
while running:
    screen.fill((0, 0, 0))



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is 'ready':
                    bullet_sound = mixer.Sound("shoot.wav")
                    bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(playerX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 1


    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 735:
        playerX = 735

    if bulletY <= 0:
        bulletY = 480
        bullet_state = 'ready'

    if bullet_state is 'fire':
        fire_bullet(playerX, bulletY)
        bulletY -= bulletY_change





    monsterX[i] += monsterX_change[i]
    if monsterX[i] <= 0:
        monsterX_change[i] = 4
        monsterY_change[i] += monsterY_change[i]
    elif monsterX[i] >= 735:
        monsterX_change = -4
        monsterY_change[i] += monsterY_change[i]


    collision = isCollision(monsterX[i], monsterY[i], bulletX, bulletY)
    if collision:
        explosion_sound = mixer.Sound("explosion.wav")
        explosion_sound.play()
        bulletY = 480
        bullet_state = 'ready'

        monsterX[i] = random.randint(0, 735)
        monsterY[i] = random.randint(50, 150)



    monster(monsterX[i], monsterY[i], i)
    player(playerX, playerY)
    pygame.display.update()