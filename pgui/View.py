class View:
    def __init__(self, pygame, screen, width, height):
        self.pg = pygame
        self.screen = screen

        self.width = width
        self.height = height

        print("Hello, world")
    
    def draw(self):
        self.pg.draw.rect(self.screen, (255, 255, 255), 
                 (20, 20, self.width, self.height))