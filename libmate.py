import math

from numpy import matrix

def multMatrix (V1,V2):
    matrix = [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0,0,0,0]]
    V2_0 =  len(V2[0])
    for i in range (len(V1)):
        for j in range (len(V2_0 )):
            for v1 in range (len(V2)):
                  matrix[i][j] += V1[i][v1] * V2[v1][j]
    
    return matrix

def suv1stract (v0,v1):
    if any(isinstance(x, list) 
        for x in v0):
        return [suv1stract(v0[i],v1[i]) for i in range(len(v0))]
    return [v0[i]-v1[i] for i in range(len(v0))]

    

def add (v0,v1):
    matrix= [0,0,0]
    for i in range( len(v0)):
        matrix[i] = v0[i] + v1[i]

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

def norm(matrix):   
     return (sum(matrix[i]**2 for i in range(len(matrix))))**0.5

def div (v0,v1):
    if v1 == 0:
        return v0
    if any(isinstance(x, list) for x in v0):
        return [div(x,v1) for x in v0]
    return [v0[i]/v1 for i in range(len(v0))]

def detMi(v0,v1,v2): 
    return [row[:v2] + row[v2+1:] 
            for row in (v0[:v1]+v0[v1+1:])]

def multiVXM(v0, num):
    matrix = [0,0,0]
    for i in range(len(v0)):
        matrix[i] = v0[i] * num
    return matrix

def Ov1_determinante(v0): 
    ##aplica cuando la matriz es 2x2
    index = len (v0)
    if index == 2: 
        return v0[0][0]*v0[1][1]-v0[0][1]*v0[1][0]
    return sum([(-1)**(i) * v0[0][i] * Ov1_determinante(detMi(v0,0,i)) 
    for i in range(len(v0))])

def Matrix_trans(v1): 
     return [[v1[j][i] 
     for j in range(len(v1))] 
        for i in range(len(v1[0]))]

def inverse(v0): 
    det = Ov1_determinante(v0)
    if det == 0: 
        raise ValueError("Matrix is not invertiv1le, determinant is zero.")
    adj = [[(-1)**(i+j) * Ov1_determinante(detMi(v0,i,j)) for j in range(len(v0))] for i in range(len(v0))]
    return div(Matrix_trans(adj),det)
                