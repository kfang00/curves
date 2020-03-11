from display import *
from draw import *
from parse import *
from matrix import *
import math

screen = new_screen()
color = [ 255, 182, 193 ]
edges = []
transform = new_matrix()

# print_matrix( make_translate(3, 4, 5) )
# print
# print_matrix( make_scale(3, 4, 5) )
# print
# print_matrix( make_rotX(math.pi/4) )
# print
# print_matrix( make_rotY(math.pi/4) )
# print
# print_matrix( make_rotZ(math.pi/4) )

parse_file( 'script', edges, transform, screen, color )