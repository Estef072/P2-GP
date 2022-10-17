import math

def multMatrix (V1,V2):
    matrix = [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0,0,0,0]]
    V2_0 =  len(V2[0])
    for i in range (len(V1)):
        for j in range (len(V2_0 )):
            for a in range (len(V2)):
                  matrix[i][j] += V1[i][a] * V2[a][j]
    
    return matrix

def substract (v0,v1):
    matrix= [0,0,0]
    posi = len(v0)
    for i in range( posi):
        matrix[i] = posi[i] - v1[i]

    return matrix

def add (v0,v1):
    matrix= [0,0,0]
    posi = len(v0)
    for i in range( posi):
        matrix[i] = posi[i] + v1[i]

    return matrix


def dot (v0,v1):
    result = 0
    for i in range(len(v0)):
        result = result + v0[i]*v1[i]
    return result


def cross(v0, v1):
    result =    [v0[1]*v1[2] - v0[2]*v1[1],
                v0[2]*v1[0] - v0[0]*v1[2],
                v0[0]*v1[1] - v0[1]*v1[0]]
    return result

def norm(lista):   
    valor1 = math.sqrt((lista[0] ** 2) + (lista[1] ** 2) + (lista[2] ** 2))  
    return valor1

def div 