import random

import pygame as pg
import numpy as np

width = 1000
height = 600

window = pg.display.set_mode((width, height))

drops = []


class Drop:
    def __init__(self, surface) -> None:
        self.surface = surface
        self.x = random.randint(0, width)
        self.y = random.randint(-200, 0)
        self.width = random.choice(np.linspace(2, 4, 100))
        self.height = random.randint(20, 30)
        self.speed = random.randint(8, 12)

        self.color = "#C158A8"
        
        self.add()
        
    def add(self):
        drops.append(self)
    
    def draw(self):
        pg.draw.rect(
            self.surface, self.color,
            (self.x, self.y, self.width, self.height)
        )

    def move(self):
        self.y += self.speed

clock = pg.time.Clock()

running = True
while running:
    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = not running
    
    if len(drops) < 400:
        for i in range(4):
            Drop(window)

    window.fill("#D8DACA")
    for drop in drops:
        drop.move()
        drop.draw()
        
        if drop.y > height:
            drop.y = -100

    print(len(drops))
    pg.display.update()