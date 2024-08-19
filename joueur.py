import pygame
import random


class Joueur(pygame.sprite.Sprite):
    def __init__(self, W, H, HW, HH, y_fond):
        super().__init__()
        self.W = W
        self.H = H
        self.HW = HW
        self.HH = HH
        self.y_fond = y_fond
        self.dimension = 45
        self.image = pygame.image.load('assets/personnage.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.dimension, self.dimension))
        self.rect = self.image.get_rect()
        self.default_X = HW - self.dimension / 2
        self.default_y = (H-y_fond)/2 - self.dimension / 2 + y_fond
        self.rect.x = self.default_X
        self.rect.y = self.default_y
        self.velocity = 250
        self.minVelocity = 150
        self.health = 10

    def right(self, dt):
        self.rect.x += int(self.velocity * dt)

    def left(self, dt):
        self.rect.x -= int(self.velocity * dt)

    def low(self, dt):
        self.rect.y += int(self.velocity * dt)

    def high(self, dt):
        self.rect.y -= int(self.velocity * dt)

    def verif(self):
        if self.rect.x > self.W - self.dimension:
            self.rect.x = self.W - self.dimension
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.y > self.H - self.dimension:
            self.rect.y = self.H - self.dimension
        if self.rect.y < self.y_fond:
            self.rect.y = self.y_fond

    def decreaseVelocity(self):
        num = random.randint(-25, -5)
        self.velocity += num
        if self.velocity < self.minVelocity:
            self.velocity = self.minVelocity
