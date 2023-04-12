from settings import *
import math
from tetromino import Tetromino

class Tetris:
    def __init__(self, app):
        self.app = app
        self.spriteGroup = pg.sprite.Group()
        self.tetromino = Tetromino(self)

    def drawGrid(self):
        for i in range(FIELD_W):
            for j in range(FIELD_H):
                pg.draw.rect(self.app.screen, 'white', 
                    (i * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)
        
    def update(self):
        self.tetromino.update()
        self.spriteGroup.update()

    def draw(self):
        self.drawGrid()
        self.spriteGroup.draw(self.app.screen)