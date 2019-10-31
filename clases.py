import pygame
import sys
import data
import random

wr = [pygame.image.load(data.resource_path('files/w1.png')), pygame.image.load(data.resource_path('files/w2.png')), pygame.image.load(data.resource_path('files/w3.png')),
      pygame.image.load(data.resource_path('files/w4.png')), pygame.image.load(data.resource_path('files/w5.png'))]
il = [pygame.image.load(data.resource_path('files/s1.png')), pygame.image.load(data.resource_path('files/s2.png')), pygame.image.load(data.resource_path('files/s3.png')),
      pygame.image.load(data.resource_path('files/s2.png'))]
at = [pygame.image.load(data.resource_path('files/a1.png')), pygame.image.load(data.resource_path('files/a2.png')), pygame.image.load(data.resource_path('files/a3.png')),
      pygame.image.load(data.resource_path('files/a4.png'))]
jp = [pygame.image.load(data.resource_path('files/j1.png')), pygame.image.load(data.resource_path('files/j2.png')), pygame.image.load(data.resource_path('files/j3.png')),
      pygame.image.load(data.resource_path('files/j4.png'))]

df = [pygame.image.load(data.resource_path('files/d1.png')), pygame.image.load(data.resource_path('files/d2.png')), pygame.image.load(data.resource_path('files/d3.png')),
      pygame.image.load(data.resource_path('files/d4.png'))]

st = [pygame.image.load(data.resource_path('files/stone2.png')), pygame.image.load(data.resource_path('files/stone3.png'))]

hh = [pygame.image.load(data.resource_path('files/h1.png')), pygame.image.load(data.resource_path('files/h2.png')), pygame.image.load(data.resource_path('files/h3.png')),
      pygame.image.load(data.resource_path('files/h2.png')), pygame.image.load(data.resource_path('files/h1.png'))]

vw = [pygame.image.load(data.resource_path('files/v1.png')), pygame.image.load(data.resource_path('files/v2.png')), pygame.image.load(data.resource_path('files/v3.png')),
      pygame.image.load(data.resource_path('files/v4.png')), pygame.image.load(data.resource_path('files/v5.png')), pygame.image.load(data.resource_path('files/v6.png'))]

vd = [pygame.image.load(data.resource_path('files/vd1.png')), pygame.image.load(data.resource_path('files/vd2.png')), pygame.image.load(data.resource_path('files/vd3.png')),
      pygame.image.load(data.resource_path('files/vd4.png')), pygame.image.load(data.resource_path('files/vd5.png')), pygame.image.load(data.resource_path('files/vd6.png'))]

class Player(pygame.sprite.Sprite):
    def __init__(self, lv):
        super(Player, self).__init__()

        self.anim = 0
        self.image = pygame.image.load(data.resource_path('files/s1.png'))
        self.rect = self.image.get_rect()

        self.rect.centerx = data.SIZE[0] / 2
        self.rect.bottom = data.SIZE[1] - 40
        self.al = 0
        self.ai = 0
        self.aa = 0
        self.aj = 0
        self.ad = 0
        self.ar = 49
        self.live = lv
        self.is_jump = False
        self.attacking = False
        self.hh = False
        self.jump_count = 10

    def update(self):

        if data.DEATH:
            return
        keys = pygame.key.get_pressed()

        if data.BAR and not data.DESTROYED:
            self.live.ch()
            if self.live.lives > 1:
                self.hh = True

        if self.hh:
            self.image = hh[self.aa // 5]
            self.aa += 1
            if self.aa > 24:
                self.aa = 0
                self.hh = False
            return

        if self.live.lives < 1:
            self.image = df[self.ad // 10]
            self.ad += 1
            if self.ad > 39:
                self.ad = 39
                data.DEATH = True

            return

        # if data.BJ:
        #     print("bj pl")
        #     if self.jump_count >= -10:
        #         if self.jump_count < 0:
        #             self.image = jp[2]
        #             self.rect.bottom += (self.jump_count ** 2) / 3
        #         else:
        #             self.image = jp[1]
        #             self.rect.bottom -= (self.jump_count ** 2) / 3
        #         self.jump_count -= 0.5
        #     else:
        #         self.rect.bottom = data.SIZE[1] - 40
        #         self.is_jump = False
        #         data.BJ = False
        #         self.jump_count = 10
        #     return

        if self.is_jump:
            if self.jump_count >= -10:
                if self.jump_count < 0:
                    self.image = jp[2]
                    self.rect.bottom += (self.jump_count ** 2) / 3
                else:
                    self.image = jp[1]
                    self.rect.bottom -= (self.jump_count ** 2) / 3
                self.jump_count -= 0.7
            else:
                self.rect.bottom = data.SIZE[1] - 40
                self.is_jump = False
                self.jump_count = 10
            return

        if self.attacking:
            self.image = at[self.aa // 10]
            self.aa += 1
            if self.aa > 39:
                self.aa = 0
                self.attacking = False
            return

        if keys[pygame.K_LEFT]:
            self.image = wr[self.ar // 10]
            self.ar -= 1
            # self.rect.centerx += 0
            if self.ar < 1:
                self.ar = 49

        elif (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and keys[pygame.K_RIGHT]:
            if data.BAR:
                data.BJ = True
            else:
                self.is_jump = True


        elif keys[pygame.K_RIGHT]:
            self.image = wr[self.al // 10]
            self.al += 1
            # self.rect.centerx += 0
            if self.al > 49:
                self.al = 0

        elif keys[pygame.K_d]:
            self.live.lives = 0

        elif keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            if data.BAR:
                data.BJ = True
            else:
                self.is_jump = True


        elif keys[pygame.K_a]:
            self.attacking = True




        else:
            self.image = il[self.ai // 20]
            self.ai += 1
            if self.ai > 79:
                self.ai = 0


class Bg(pygame.sprite.Sprite):
    def __init__(self):
        super(Bg, self).__init__()
        self.image = pygame.image.load(data.resource_path('files/bg.jpg'))

        self.rect = self.image.get_rect()

        self.speed = 2

        self.rect.left = -640
        self.rect.top = 0
        self.score = 0

    def update(self):

        if data.DEATH:

            return

        # if data.BJ:
        #     print("bj bg")
        #     self.rect.left -= self.speed * 3
        #     return

        if data.BAR:
            self.rect.left += self.speed * 30
            if self.rect.left > -320:
                self.rect.left -= 960

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and keys[pygame.K_RIGHT]:
            self.rect.left -= self.speed * data.JK
            if self.rect.left < -1280:
                self.rect.left += 960

        elif keys[pygame.K_RIGHT]:
            self.rect.left -= self.speed
            if self.rect.left < -1280:
                self.rect.left += 960


        elif keys[pygame.K_LEFT]:
            self.rect.left += self.speed
            if self.rect.left > -320:
                self.rect.left -= 960



        else:
            pass


class Stone(pygame.sprite.Sprite):
    def __init__(self, x):
        super(Stone, self).__init__()
        self.image = pygame.image.load(data.resource_path('files/stone.png'))

        self.rect = self.image.get_rect()
        self.speed = 2
        self.rect.left = x
        self.rect.bottom = data.SIZE[1] - 20
        self.ai = 0

    def update(self):
        if data.DEATH:
            return

        # if data.BJ:
        #     print("bj st")
        #     self.rect.left -= self.speed * 3
        #     return

        if data.BAR:
            self.rect.left += self.speed * 30
            return

        if data.DESTROYED:
            self.image = st[self.ai // 10]
            self.rect.top += 1
            # print(self.rect.top)
            if self.ai < 19:
                self.ai += 1
            if self.rect.top > data.SIZE[1]:
                data.DESTROYED = False

        if self.rect.right < 0:
            self.image = pygame.image.load(data.resource_path('files/stone.png'))
            self.rect = self.image.get_rect()
            self.rect.left = random.randint(1000, 3000)
            self.rect.bottom = data.SIZE[1] - 20

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and keys[pygame.K_RIGHT]:
            self.rect.left -= self.speed * data.JK

        elif keys[pygame.K_RIGHT]:
            self.rect.left -= self.speed


        elif keys[pygame.K_LEFT]:
            self.rect.left += self.speed

        else:
            pass


class Lives(pygame.sprite.Sprite):
    def __init__(self, x):
        super(Lives, self).__init__()
        self.image = pygame.image.load(data.resource_path('files/lives.png'))
        self.lives = x
        self.rect = self.image.get_rect()
        self.rect.width = 90
        self.rect.left = 20
        self.rect.top = 20
        self.ai = 0

    def ch(self, k=-1):
        self.lives += k

    def update(self):
        self.image = self.image.subsurface(pygame.Rect((0, 0), (30 * self.lives, 26)))


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x):
        super(Enemy, self).__init__()
        self.image = pygame.image.load(data.resource_path('files/v1.png'))

        self.rect = self.image.get_rect()
        self.speed = 2
        self.es = 1
        self.death = False
        self.rect.left = x
        self.rect.bottom = data.SIZE[1] - 40
        self.ai = 0
        self.ad = 0

    def update(self):



        if data.DEATH:
            return

        if self.death and self.rect.right > 0:
            self.image = vd[self.ad // 10]
            self.rect.top += 0.3
            # print(self.rect.top)
            if self.ad < 59:
                self.ad += 1





        if self.rect.right < 0:
            self.ad = 0
            self.death = False
            self.image = pygame.image.load(data.resource_path('files/v1.png'))
            self.rect = self.image.get_rect()
            self.rect.left = random.randint(2000, 4000)
            self.rect.bottom = data.SIZE[1] - 40


        # if data.BJ:
        #     print("bj st")
        #     self.rect.left -= self.speed * 3
        #     return

        if data.BAR:
            self.rect.left += self.es * 60
            return

        if not self.death:
            self.rect.left -= self.es
            self.image = vw[self.ai // 10]
            self.ai += 1
            if self.ai > 59:
                self.ai = 0




        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and keys[pygame.K_RIGHT]:
            self.rect.left -= self.speed * data.JK

        elif keys[pygame.K_RIGHT]:
            self.rect.left -= self.speed


        elif keys[pygame.K_LEFT]:
            self.rect.left += self.speed

        else:
            pass
