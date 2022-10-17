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
skyBluediamond = Material(diffuse = (0.002, 0.8, 0.85), spec = 66, matType = REFLECTIVE)
RUBY = Material(diffuse = (0.8, 0.0, 0.0), spec = 66, matType = REFLECTIVE)
porcelaniush = Material(diffuse= (0.854,0.850 , 0.843), spec = 100, matType = REFLECTIVE)
verdeEsmeralda = Material(diffuse = (0.0, 0.8, 0.0), spec = 95, matType = REFLECTIVE)
oro = Material(diffuse = (0.67, 0.63, 0.2), spec = 100, matType = REFLECTIVE )

rojis = Material(diffuse = (0.8, 0.3, 0.3), spec = 64,ior = 1.5,matType = TRANSPARENT)
verdis = Material(diffuse = (0.1, 0.8, 0.0), spec = 64,ior = 1.5,matType = TRANSPARENT)
gisini = Material(diffuse = (0.4, 0.4, 0.4), spec = 64,ior = 1.5,matType = TRANSPARENT)
rtx = Raytracer(width, height)




rtx.envMap = Texture("parkingLot.bmp")

rtx.lights.append( AmbientLight(intensity = 0.1 ))
rtx.lights.append( DirectionalLight(direction = (0,0,-1), intensity = 0.5 ))
rtx.lights.append( PointLight(point = (-1,-1,0) ))

rtx.scene.append( Plane(position = (0,-10,0), normal = (0,1,0), material = gisini ))
rtx.scene.append( Plane(position = (0,10,0), normal = (0,-1,0), material = gisini ))
rtx.scene.append( Plane(position = (-10,0,0), normal = (1,0,0), material = rojis  ))
rtx.scene.append( Plane(position = (10,0,0), normal = (-1,0,0), material = verdis ))

# rtx.scene.append( Sphere(V3(-3,3,-10), 1, verdeEsmeralda)  )
# rtx.scene.append( Sphere(V3(0,3,-10), 1, porcelaniush)  )
# rtx.scene.append( Sphere(V3(3,3,-10), 1, skyBluediamond)  )

# ##rtx.scene.append( Triangulo(vector0=(-3.5,1,-7), vector1=(1.5,-1,-7), vector2=(0,1,1),material=skyBluediamond ) )

# rtx.scene.append( AABB(position = (3,-1,-10), size = (2.5,2.5,2.5), material = oro))
# ##rtx.scene.append( Triangulo(vector0=(-1.5,1.5,-7), vector1=(3,1.5,-7), vector2=(0,3,-7),material=verdeEsmeralda ) )


# rtx.scene.append( Sphere(V3(-3,-3,-10), 1, stone)  )
# rtx.scene.append( Sphere(V3(0,-3,-10), 1, oro)  )
# rtx.scene.append( Sphere(V3(3,-3,-10), 1, RUBY)  )

rtx.glRender()

rtx.glFinish("output.bmp")
