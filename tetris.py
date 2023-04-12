from settings import *
import math
from tetromino import Tetromino

class Tetris:
    def __init__(self, app):
        self.app = app
        self.tetromino = Tetromino(self)

    def drawGrid(self):
        for i in range(FIELD_W):
            for j in range(FIELD_H):
                pg.draw.rect(self.app.screen, 'white', 
                    (i * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)
        
    def update(self):
        self.tetromino.update()

    def draw(self):
        self.drawGrid()