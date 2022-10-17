from gl import Raytracer, V3
from texture import *
from figures import *
from lights import *


width = 512
height = 512
# Materiales

brick = Material(diffuse = (0.8, 0.3, 0.3), spec = 16)
stone = Material(diffuse = (0.4, 0.4, 0.4), spec = 8)
grass = Material(diffuse = (0.3, 1.0, 0.3), spec = 64)
marble = Material(spec = 64, texture = Texture("descarga.bmp"), matType= REFLECTIVE)
mirror = Material(diffuse = (0.9, 0.9, 0.9), spec = 64, matType = REFLECTIVE)
glass = Material(diffuse = (0.9, 0.9, 0.9), spec = 64, ior = 1.5, matType = TRANSPARENT)
materialOP1 = Material(diffuse = (0.0546, 0.472, 0.0664), spec=32, matType=OPAQUE)
diamond = Material(diffuse = (0.0, 0.8, 0.8), spec = 64, matType = REFLECTIVE)
RUBY = Material(diffuse = (0.8, 0.0, 0.0), spec = 64, matType = REFLECTIVE)

rtx = Raytracer(width, height)


rtx.envMap = Texture("parkingLot.bmp")

rtx.lights.append( AmbientLight(intensity = 0.1 ))
#rtx.lights.append( DirectionalLight(direction = (0,0,-1), intensity = 0.5 ))
rtx.scene.append( Triangulo((-1.5,1,-7), (1.5,1,-7), (0,3,-7), stone) )
rtx.scene.append( Triangulo((1.5,1,-7), (2,2,-7), (0,3,-7), mirror) )

rtx.scene.append( Triangulo((-1.5,-1,-7), (1.5,-1,-7), (0,1,-7), stone) )
rtx.scene.append( Triangulo((1.5,-1,-7), (2,0,-7), (0,1,-7), mirror) )

rtx.scene.append( Triangulo((-1.5,-3,-7), (1.5,-3,-7), (0,-1,-7), brick) )
rtx.scene.append( Triangulo((1.5,-3,-7), (2,-2,-7), (0,-1,-7), stone) )


rtx.glRender()

rtx.glFinish("output.bmp")