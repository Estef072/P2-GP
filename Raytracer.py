from gl import Raytracer, V3
from texture import *
from figures import *
from lights import *

width = 200
height =200

# Materiales

brick = Material(diffuse = (0.8, 0.3, 0.3), spec = 16)
stone = Material(diffuse = (0.4, 0.4, 0.4), spec = 8)
grass = Material(diffuse = (0.3, 1.0, 0.3), spec = 64)
marble = Material(spec = 64, texture = Texture("descarga.bmp"), matType= REFLECTIVE)
mirror = Material(diffuse = (0.9, 0.9, 0.9), spec = 64, matType = REFLECTIVE)
glass = Material(diffuse = (0.9, 0.9, 0.9), spec = 64, ior = 1.5, matType = TRANSPARENT)
skyBluediamond = Material(diffuse = (0.002, 0.8, 0.85), spec = 66, matType = REFLECTIVE)
RUBY = Material(diffuse = (0.888, 0.0, 0.0), spec = 75, matType = REFLECTIVE)
perla = Material(diffuse= (0.854,0.850 , 0.843), spec = 100, matType = REFLECTIVE)
verdeEsmeralda = Material(diffuse = (0.0, 0.8, 0.0), spec = 95, matType = TRANSPARENT)
oro = Material(diffuse = (0.67, 0.63, 0.2), spec = 100, matType = REFLECTIVE )
magenta = Material(diffuse = (1, 0, 1), spec = 64, matType = REFLECTIVE )
oroCuadro = Material(diffuse = (0.67, 0.63, 0.2) )
verdeMusgo = Material(diffuse = (0, 1, 0), spec = 64, ior = 1.5, matType = TRANSPARENT)
verdisss = Material(diffuse = (0.5, 1, 0), spec = 32, matType=REFLECTIVE)
suelo= Material(diffuse = (0.5, 0.5, 0.5))
negriss = Material(diffuse = (0.3, 0.3, 0.3))

rtx = Raytracer(width, height)



rtx.envMap = Texture("cuarto.bmp")
rtx.lights.append( AmbientLight(intensity = 0.5 ))
rtx.lights.append( DirectionalLight(direction = (0,0,-1), intensity = 0.5 ))
rtx.lights.append( PointLight(point=(-1,-1,0)))




rtx.scene.append( AABB((3,0,-10), (0.1,6,10), verdisss) )
rtx.scene.append( AABB((-3,0,-10), (0.1,6,10), verdisss) )
rtx.scene.append( AABB((0,3,-10), (6,0.1,10), suelo) )
rtx.scene.append( AABB((0,-3,-10), (6,0.1,10), suelo) )

rtx.scene.append( Sphere(V3(-3,3,-10), 1, magenta)  )
rtx.scene.append( Sphere(V3(0,3,-10), 1, perla )  )
rtx.scene.append( Sphere(V3(3,3,-10), 1, skyBluediamond)  )


rtx.scene.append( Sphere(V3(-.1,1.5,-10), .15, oro))
rtx.scene.append( AABB(position = (-.1,.9,-10), size = (.4,.4,.4), material = oro))
rtx.scene.append( AABB(position = (-.1,.2,-10), size = (.7,.7,.7), material = oro))
rtx.scene.append( AABB(position = (-.1,-.9,-10), size = (1.3,1.3,1.3), material = oro))


rtx.scene.append( Triangulo((-17,-1,-50), vector1=(-1, 1, -50) , vector2=(-2, -4, -50),material=oro ) )
rtx.scene.append( Triangulo((17,-1,-50), vector1=(1, 1, -50) , vector2=(2, -4, -50),material=oro ) )

rtx.scene.append( Sphere(V3(-3,-3,-10), 1, stone))
rtx.scene.append( Sphere(V3(0,-3,-10), 1, oro)  )
rtx.scene.append( Sphere(V3(3,-3,-10), 1, RUBY))

rtx.glRender()

rtx.glFinish("output2.bmp")
