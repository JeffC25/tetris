from settings import *
import math

class Tetris:
    def __init__(self, app):
        self.app = app

    def drawGrid(self):
        for i in range(FIELD_W):
            for j in range(FIELD_H):
                pg.draw.rect(self.app.screen, 'white', (i * TILE_SIZE, y * TILE_SIZE, TILE SIZE, TILE_SIZE), 1)
        
    def update(self):
        pass

    def draw(self):
        pass