import pygame
import os

width, height = 1000, 700
running = True
background = (120, 120, 120)
Display = pygame.display.set_mode((width, height), pygame.RESIZABLE)
mouseGraphic = pygame.image.load(os.path.join("redcircle.png")).convert_alpha()
cheeseGraphic = pygame.image.load(os.path.join("redcircle.png")).convert_alpha()



class cheese():
    def __init__(self,x, y):
        self.x = x
        self.y = y

    def display(self):
        Display.blit(cheeseGraphic, (self.x, self.y))



class mouse():
    def __init__(self,x, y):
        self.x = x
        self.y = y
        self.speed = 50

    def movement(self, direction):
        if direction == 1:
            self.x += self.speed
        if direction == 2:
            self.x -= self.speed
        if direction == 3:
            self.y += self.speed
        if direction == 1:
            self.y -= self.speed

    def display(self):
        Display.blit(mouseGraphic, (self.x, self.y))

    def eat(self):
        if Mouse.x == Cheese.x and Mouse.y == Cheese.y:
            print("Yes!")
        else:
            print("SCREEEECH")

Mouse = mouse(100,100)
Cheese = cheese(200,200)



while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    pygame.init()
    Display.fill(background)

    Mouse.display()

    #Mouse.movement(1)

    #Mouse.eat()

    pygame.display.flip()