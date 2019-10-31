import pygame
import sys
import data
import random
from clases import Player, Bg, Stone, Lives, Enemy


def rnd(x):
    return x > random.randint(1, 100)


pygame.init()

sc = pygame.display.set_mode(data.SIZE)
clock = pygame.time.Clock()

running = True

all_objects = pygame.sprite.Group()

lv = Lives(5)
pl = Player(lv)
bg = Bg()
st = Stone(random.randint(500, 810))
enn = Enemy(random.randint(700, 910))

score = 0
all_objects.add(bg)
all_objects.add(pl)
all_objects.add(st)
all_objects.add(lv)
all_objects.add(enn)

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F1:
                print("lol")
                all_objects = pygame.sprite.Group()

                lv = Lives(5)
                pl = Player(lv)
                bg = Bg()
                st = Stone(random.randint(500, 810))
                enn = Enemy(random.randint(700, 910))

                all_objects.add(bg)
                all_objects.add(pl)
                all_objects.add(st)
                all_objects.add(lv)
                all_objects.add(enn)
                data.DEATH = False
                score = 0

    all_objects.update()
    all_objects.draw(sc)

    if pygame.sprite.collide_mask(pl, st) and not data.DESTROYED:
        if pl.attacking:
            data.DESTROYED = True
        else:
            data.BAR = True
    else:
        data.BAR = False

    if pygame.sprite.collide_mask(pl, enn) and not data.DESTROYED:
        if pl.attacking:
            enn.death = True
            print("destroing volf")
        else:
            data.BAR = True
    else:
        data.BAR = False

    if data.DEATH:

        font = pygame.font.SysFont("comicsansms", 48)
        text1 = font.render(f"GAME OVER. Score {int(score)}", True, (0, 0, 0))
        text2 = font.render("Press F1 to restart", True, (0, 0, 0))
        sc.blit(text1,
                (320 - text1.get_width() // 2, 240 - text1.get_height() // 2 - 40))
        sc.blit(text2,
                (320 - text2.get_width() // 2, 240 - text2.get_height() // 2 + 40))

    else:
        score += clock.get_time()/1000
        font = pygame.font.SysFont("comicsansms", 28)
        tt = font.render(str(int(score)), True, (0, 0, 0))
        sc.blit(tt,
                (600 - tt.get_width() // 2, 60 - tt.get_height() // 2 - 40))




    pygame.display.flip()

pygame.quit()
