from gl import Raytracer, V3
from texture import *
from figures import *
from lights import *

width =  1024
height =  1054
# Materiales

brick = Material(diffuse = (0.8, 0.3, 0.3), spec = 16)
stone = Material(diffuse = (0.4, 0.4, 0.4), spec = 8)
grass = Material(diffuse = (0.3, 1.0, 0.3), spec = 64)
marble = Material(spec = 64, texture = Texture("descarga.bmp"), matType= REFLECTIVE)
mirror = Material(diffuse = (0.9, 0.9, 0.9), spec = 64, matType = REFLECTIVE)
glass = Material(diffuse = (0.9, 0.9, 0.9), spec = 64, ior = 1.5, matType = TRANSPARENT)
materialOP1 = Material(diffuse = (0.0546, 0.472, 0.0664), spec=32, matType=OPAQUE)
skyBluediamond = Material(diffuse = (0.002, 0.8, 0.85), spec = 66, matType = REFLECTIVE)
RUBY = Material(diffuse = (0.8, 0.0, 0.0), spec = 64, matType = REFLECTIVE)
porcelana = Material(diffuse= (0.854,0.850 , 0.843), spec = 100, matType = OPAQUE)


rtx = Raytracer(width, height)


rtx.envMap = Texture("parkingLot.bmp")

rtx.lights.append( AmbientLight(intensity = 0.1 ))
rtx.lights.append( DirectionalLight(direction = (0,0,-1), intensity = 0.5 ))
rtx.scene.append( Triangulo(vector0=(-1.5,1,-7), vector1=(1.5,1,-7), vector2=(0,3,-7),material=skyBluediamond ) )
##rtx.scene.append(Plane(position = (0,20,0), normal = (0,-1,0), material = diamond))

rtx.scene.append( Sphere(V3(0,-1,-10), 1, material = skyBluediamond )  )
rtx.scene.append( Sphere(V3(0,-1,-10), 1,  material = brick )  )
rtx.scene.append( Sphere(V3(3,-1,-10), 1,  material =stone)  )


rtx.glRender()

rtx.glFinish("output.bmp")
