import pygame
import random

velocity = 200


def decreaseVelocity():
    global velocity
    num = random.randint(5, 25)
    velocity += num
    print(f"les balls sont plus RAPIDES : +{num}px/s")


class Balld(pygame.sprite.Sprite):
    def __init__(self, W, H, HW, HH, y_fond, joueur):
        super().__init__()
        self.W = W
        self.H = H
        self.HW = HW
        self.HH = HH
        self.y_fond = y_fond
        self.dimension_x = 60
        self.dimension_y = 20
        self.joueur = joueur
        self.velocity = velocity
        self.image = pygame.image.load("assets/ball/balld.png").convert_alpha()
        self.num21 = 10
        self.image = pygame.transform.scale(self.image, (self.dimension_x, self.dimension_y))
        self.rect = self.image.get_rect()
        self.rect.x = self.W + self.num21
        self.rect.y = random.randint(0 + self.y_fond, self.H-self.dimension_y)

    def collide(self):
        if pygame.sprite.spritecollide(self, pygame.sprite.Group(self.joueur), False, pygame.sprite.collide_mask):
            # print("collide !")
            return True
        else:
            return False

    def gravite(self, dt):
        self.rect.x -= int(self.velocity * dt)

    def verif(self):
        if self.rect.x <= - self.dimension_x:
            return True
        else:
            return False


class Ballg(Balld):
    def __init__(self, W, H, HW, HH, y_fond, joueur):
        super().__init__(W, H, HW, HH, y_fond, joueur)
        self.image = pygame.image.load("assets/ball/ballg.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.dimension_x, self.dimension_y))
        self.rect = self.image.get_rect()
        self.rect.x = - self.dimension_x - self.num21
        self.rect.y = random.randint(0 + self.y_fond, self.H-self.dimension_y)

    def gravite(self, dt):
        self.rect.x += int(self.velocity * dt)

    def verif(self):
        if self.rect.x >= self.W:
            return True
        else:
            return False


class Ballb(Balld):
    def __init__(self, W, H, HW, HH, y_fond, joueur):
        super().__init__(W, H, HW, HH, y_fond, joueur)
        self.image = pygame.image.load("assets/ball/ballb.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.dimension_y, self.dimension_x))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, self.W-self.dimension_y)
        self.rect.y = self.H + self.num21

    def gravite(self, dt):
        self.rect.y -= int(self.velocity * dt)

    def verif(self):
        if self.rect.y <= self.y_fond - self.dimension_x:
            return True
        else:
            return False


class Ballh(Balld):
    def __init__(self, W, H, HW, HH, y_fond, joueur):
        super().__init__(W, H, HW, HH, y_fond, joueur)
        self.image = pygame.image.load("assets/ball/ballh.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.dimension_y, self.dimension_x))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, self.W-self.dimension_y)
        self.rect.y = y_fond - self.dimension_x - self.num21

    def gravite(self, dt):
        self.rect.y += int(self.velocity * dt)

    def verif(self):
        if self.rect.y >= self.H:
            return True
        else:
            return False
