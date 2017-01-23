import shapes
import artifacts
import os

def circle_room():
    circle_artifact = artifacts.create_circle()
    circ = shapes.Circle()
    
    os.system('cls')
    print('\n', circle_artifact, '\n\nInside the circle room. Created a',
          circ.type, 'with', circ.points, 'points\n')

def square_room():
    square_artifact = artifacts.create_square()
    sqr = shapes.Square()
    
    os.system('cls')
    print('\n', square_artifact, '\n\nInside the square room. Created a',
          sqr.type, 'with', sqr.points, 'points\n')

def triangle_room():
    triangle_artifact = artifacts.create_triangle()
    tri = shapes.Triangle()
    
    os.system('cls')
    print('\n', triangle_artifact, '\n\nInside the triangle room. Created a',
          tri.type, 'with', tri.points, 'points\n')