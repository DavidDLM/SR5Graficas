from gl import Renderer, _color_, V2, V3
from textures import Texture
from obj import Obj

from shaders import greyScale

#################################

width = 1300
height = 866
depth = -10
black = _color_(0, 0, 0)
white = _color_(1, 1, 1)

rend = Renderer(width, height)

rend.glClearBackground()

#################################
rend.active_shader = greyScale
rend.active_texture = Texture("models/yellowTX.bmp")
rend.glLoadModel("models/Trumpet.obj",
                 translate=V3(2, -2.5, -13),
                 scale=V3(13, 13, 13),
                 rotate=V3(0, 180, 10))
#################################

rend.write("SR5.bmp")
