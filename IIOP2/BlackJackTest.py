__author__ = 'itnxw'

import SimpleGUICS2Pygame .simpleguics2pygame as simplegui
import random
TILE_WIDTH = 50
TILE_HEIGHT = 100

class Tile :



    def __init__( self, num,exp,loc):
        self.number = num
        self.exposed = exp
        self.location =loc

    def get_num(self):
        return self.number


    def expose_tile(self):
        self.exposed = True

    # hide the tile
    def hide_tile(self):
        self.exposed = False

    def is_exposed (self):
        return  self.exposed



    def __str__(self):
        return ('Tile' + str(self.number) + 'is exposed' + str(self.exposed) + str(self.location[0]) )

    # draw method for tiles
    def draw_tile(self, canvas):
        loc = self.location
        if self.exposed:
            text_location = [loc[0] + 0.2 * TILE_WIDTH, loc[1] - 0.3 * TILE_HEIGHT]
            canvas.draw_text(str(self.number), text_location, TILE_WIDTH, "White")
        else:
            tile_corners = (loc, [loc[0] + TILE_WIDTH, loc[1]], [loc[0] + TILE_WIDTH, loc[1] - TILE_HEIGHT], [loc[0], loc[1] - TILE_HEIGHT])
            canvas.draw_polygon(tile_corners, 1, "Red", "Green")

    #mouse_click event handler
    def is_selected(self,pos):
        inside_hor = self.location[0] <= pos[0] < self.location[0] + TILE_WIDTH
        inside_vert = self.location[1] - TILE_HEIGHT <= pos[1] <= self.location[1]
        return  inside_hor and inside_vert

  # draw handler
def draw(canvas):

    tile1.draw_tile(canvas)
    tile2.draw_tile(canvas)

def click(position):
    if tile1.is_selected(position):
        tile1.hide_tile()
    if tile2.is_selected(position):
        tile2.expose_tile()


frame = simplegui.create_frame('BlacJack' , 2*TILE_WIDTH,TILE_HEIGHT)
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)

tile1 = Tile(3,True, [0,TILE_WIDTH ])
tile2 = Tile(5,False,[TILE_WIDTH,TILE_HEIGHT])

frame.start()
my_tile = Tile(1,True,[0,0])
my_tile.get_num()
my_tile.is_exposed()

print my_tile
