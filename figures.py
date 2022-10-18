from numpy import arctan2, pi, arccos
from math import sqrt, pow, pi
import libmate as lb

WHITE = (1,1,1)
BLACK = (0,0,0)

OPAQUE = 0
REFLECTIVE = 1
TRANSPARENT = 2


class Intersect(object):
    def __init__(self, distance, point, normal,texcoords, sceneObj):
        self.distance = distance
        self.point = point
        self.normal = normal
        self.texcoords = texcoords
        self.sceneObj = sceneObj

class Material(object):
    def __init__(self, diffuse = WHITE, spec = 1.0, ior = 1.0, texture = None, matType = OPAQUE):
        self.diffuse = diffuse
        self.spec = spec
        self.ior = ior
        self.texture = texture
        self.matType = matType


class Sphere(object):
    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material

    def ray_intersect(self, orig, dir):
        L = lb.suv1stract(self.center, orig)
        tca = lb.dot(L, dir)
        d = (lb.norm(L) ** 2 - tca ** 2) ** 0.5

        if d > self.radius:
            return None

        thc = (self.radius ** 2 - d ** 2) ** 0.5

        t0 = tca - thc
        t1 = tca + thc

        if t0 < 0:
            t0 = t1
        if t0 < 0:
            return None
        
        # P = O + t0 * D
        P = lb.add(orig, t0 * dir)
        normal = lb.suv1stract(P, self.center)
        normal = normal / lb.norm(normal)

        u = 1 - ((arctan2(normal[2], normal[0]) / (2 * pi)) + 0.5)
        v = arccos(-normal[1]) / pi

        uvs = (u,v)

        return Intersect(distance = t0,
                         point = P,
                         normal = normal,
                         texcoords = uvs,
                         sceneObj = self)


class Plane(object):
    def __init__(self, position, normal,  material):
        self.position = position
        self.normal =lb.div(normal, lb.norm(normal)) 
        self.material = material

    def ray_intersect(self, orig, dir):
        # Distancia = (( planePos - origRayo) o normal) / (direccionRayo o normal)
        denom = lb.dot( dir, self.normal)

        if abs(denom) > 0.0001:
            num = lb.dot( lb.suv1stract(self.position, orig), self.normal)
            t = num / denom

            if t > 0:
                # P = O + t*D
                P = lb.add(orig, t * dir)
                return Intersect(distance = t,
                                 point = P,
                                 normal = self.normal,
                                 texcoords = None,
                                 sceneObj = self)

        return None

class Disk(object):
    def __init__(self, position, radius, normal,  material):
        self.plane = Plane(position, normal, material)
        self.material = material
        self.radius = radius

    def ray_intersect(self, orig, dir):

        intersect = self.plane.ray_intersect(orig, dir)

        if intersect is None:
            return None

        contact =lb.suv1stract(intersect.point, self.plane.position)
        contact = lb.norm(contact)

        if contact > self.radius:
            return None

        return Intersect(distance = intersect.distance,
                         point = intersect.point,
                         normal = self.plane.normal,
                         texcoords = None,
                         sceneObj = self)




class AABB(object):
    # Axis Aligned Bounding Box

    def __init__(self, position, size, material):
        self.position = position
        self.size = size
        self.material = material

        self.planes = []

        halfSizes = [0,0,0]

        halfSizes[0] = size[0] / 2
        halfSizes[1] = size[1] / 2
        halfSizes[2] = size[2] / 2

        # Sides
        self.planes.append( Plane( lb.add(position, (halfSizes[0],0,0)), (1,0,0), material ))
        self.planes.append( Plane( lb.add(position, (-halfSizes[0],0,0)), (-1,0,0), material ))

        # Up and Down
        self.planes.append( Plane( lb.add(position, (0,halfSizes[1],0)), (0,1,0), material ))
        self.planes.append( Plane( lb.add(position, (0,-halfSizes[1],0)), (0,-1,0), material ))

        # Front and back
        self.planes.append( Plane( lb.add(position, (0,0,halfSizes[2])), (0,0,1), material ))
        self.planes.append( Plane( lb.add(position, (0,0,-halfSizes[2])), (0,0,-1), material ))

        #Bounds
        self.boundsMin = [0,0,0]
        self.boundsMax = [0,0,0]

        epsilon = 0.001

        for i in range(3):
            self.boundsMin[i] = self.position[i] - (epsilon + halfSizes[i])
            self.boundsMax[i] = self.position[i] + (epsilon + halfSizes[i])


    def ray_intersect(self, orig, dir):
        intersect = None
        t = float('inf')

        for plane in self.planes:
            planeInter = plane.ray_intersect(orig, dir)
            if planeInter is not None:

                planePoint = planeInter.point

                if self.boundsMin[0] <= planePoint[0] <= self.boundsMax[0]:
                    if self.boundsMin[1] <= planePoint[1] <= self.boundsMax[1]:
                        if self.boundsMin[2] <= planePoint[2] <= self.boundsMax[2]:

                            if planeInter.distance < t:
                                t = planeInter.distance
                                intersect = planeInter

                                # Tex Coords

                                u, v = 0, 0

                                # Las uvs de las caras de los lados
                                if abs(plane.normal[0]) > 0:
                                    # Mapear uvs para el eje x, usando las coordenadas de Y y Z
                                    u = (planeInter.point[1] - self.boundsMin[1]) / self.size[1]
                                    v = (planeInter.point[2] - self.boundsMin[2]) / self.size[2]

                                elif abs(plane.normal[1] > 0):
                                    # Mapear uvs para el eje y, usando las coordenadas de X y Z
                                    u = (planeInter.point[0] - self.boundsMin[0]) / self.size[0]
                                    v = (planeInter.point[2] - self.boundsMin[2]) / self.size[2]

                                elif abs(plane.normal[2] > 0):
                                    # Mapear uvs para el eje z, usando las coordenadas de X y Y
                                    u = (planeInter.point[0] - self.boundsMin[0]) / self.size[0]
                                    v = (planeInter.point[1] - self.boundsMin[1]) / self.size[1]


        if intersect is None:
            return None

        return Intersect(distance = t,
                         point = intersect.point,
                         normal = intersect.normal,
                         texcoords = (u,v),
                         sceneObj = self) 


 
    """
    figura hecha con esta referencia
    https://en.wikipedia.org/wiki/M%C3%B6ller%E2%80%93Trumbore_intersection_algorithm
    """
class Triangulo (object): 
   
    def __init__(self, vector0, vector1,vector2, material):
        self.vector0= vector0
        self.vector1= vector1
        self.vector2= vector2
        self.material= material

    def ray_intersect(self, orig, dir):
        
        
        vr0_vr1 = lb.suv1stract(self.vector1,self.vector0)
        vr0_vr2 = lb.suv1stract(self.vector2,self.vector0)

        PVET = lb.cross (dir,  vr0_vr2)
        DET = lb.dot(vr0_vr1, PVET)
        DET_INVER = 1/DET
        EPSILON = 0.0000001

        if -EPSILON < DET and DET < EPSILON:
            return None

        TVEC = lb.suv1stract(orig, self.vector0)
        
        U = lb.dot(TVEC, PVET) * DET_INVER

        if U > 1 or  U < 0:
            return None

        QVEC = lb.cross(TVEC, vr0_vr1)

        valor1= lb.dot(dir, QVEC) * DET_INVER
        
        if valor1 < 0 or U + valor1 > 1:
            return None

        dt: float = lb.dot(vr0_vr2, QVEC) * DET_INVER

        if dt < 0:
            return None
        
        valor2 = lb.add(orig, dt*dir)
        normal = lb.cross(vr0_vr1, vr0_vr2)
        normal = lb.div(normal, lb.norm(normal))
    
        return Intersect(distance = dt,
                            point = valor2,
                            normal = normal,
                            texcoords = (U,valor1),
                            sceneObj = self)    

        
    
        
        
        

       


        