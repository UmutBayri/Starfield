import random

import pygame as pg
import numpy as np

width = 1000
height = 600

window = pg.display.set_mode((width, height))

stars = []

class Star:
    def __init__(self, surface) -> None:
        self.surface = surface
        self.x = width / 2
        self.y = height / 2 
        self.max_speed = 5
        self.min_speed = 0.1
        self.target = (
            random.choice(
                random.choice([np.linspace(self.min_speed, self.max_speed, 50), np.linspace(-self.max_speed,-self.min_speed, 50)])
            ),
            random.choice(
                random.choice([np.linspace(self.min_speed, self.max_speed, 50), np.linspace(-self.max_speed, -self.min_speed, 50)])
            )
        )
        self.direction = random.choice([-1, 1])
        self.add()

    def draw(self):
        pg.draw.circle(self.surface, "white", (self.x, self.y), 3, 5)

    def move(self):
        self.x += self.target[0] * self.direction
        self.y += self.target[1] * self.direction

    def add(self):
        stars.append(self)

clock = pg.time.Clock()


running = True
while running:
    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = not running

    window.fill("black")

    for i in range(1):
        Star(window)

    for star in stars:
        star.move()
        star.draw()

    pg.display.update()
