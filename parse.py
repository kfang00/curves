from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
	 circle: add a circle to the edge matrix - 
	         takes 4 arguments (cx, cy, cz, r)
	 hermite: add a hermite curve to the edge matrix -
	          takes 8 arguments (x0, y0, x1, y1, rx0, ry0, rx1, ry1)
	 bezier: add a bezier curve to the edge matrix -
	         takes 8 arguments (x0, y0, x1, y1, x2, y2, x3, y3)
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         move: create a translation matrix,
               then multiply the transform matrix by the translation matrix -
               takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing
See the file script for an example of the file format
"""
ARG_COMMANDS = [ 'line', 'scale', 'move', 'rotate', 'save' ]

def parse_file( fname, edges, transform, screen, color ):
    f = open(fname,'r')
    s = f.readlines()
    f.close()
    #print(s)
    idx = 0
    while idx < len(s):
        s[idx]= s[idx].strip('\n')
        if (s[idx] == 'line'):
            hold = s[idx + 1].split()
            add_edge(edges, int(hold[0]), int(hold[1]), int(hold[2]), int(hold[3]), int(hold[4]), int(hold[5]) )
            idx += 1
        elif (s[idx] == 'scale'):
            hold = s[idx + 1].split()
            sc = make_scale(int(hold[0]), int(hold[1]), int(hold[2]))
            matrix_mult( sc, transform )
            idx += 1
        elif (s[idx] == 'ident'):
            ident(transform)
        elif (s[idx] == 'move'):
            hold = s[idx + 1].split()
            tr = make_translate(int(hold[0]), int(hold[1]), int(hold[2]))
            matrix_mult( tr, transform )
            idx += 1
        elif (s[idx] == 'rotate'):
            hold = s[idx + 1].split()
            r = 0
            if hold[0] == 'x':
                r = make_rotX(int(hold[1]))
            elif hold[0] == 'y':
                r = make_rotY(int(hold[1]))
            else:
                r = make_rotZ(int(hold[1]))
            matrix_mult(r, transform)
        elif (s[idx] == 'circle'):
            hold = s[idx + 1].split()
            add_circle(edges, int(hold[0]), int(hold[1]), int(hold[2]), int(hold[3]), 0.001 )
            idx += 1
        elif (s[idx] == 'hermite'):
            hold = s[idx + 1].split()
            add_curve( edges, hold[0], hold[1], hold[2], hold[3], hold[4], hold[5], hold[6], hold[7], 0.001, 'hermite' )
            idx += 1
        elif (s[idx] == 'bezier'):
            hold = s[idx + 1].split()
            add_curve( edges, int(hold[0]), int(hold[1]), int(hold[2]), int(hold[3]), int(hold[4]), int(hold[5]), int(hold[6]), int(hold[7]), 0.001, 'bezier' )
            idx += 1 
        elif (s[idx] == 'apply'):
            matrix_mult( transform, edges )
        elif (s[idx] == 'display'):
            clear_screen(screen)
            draw_lines(edges, screen, color )
            display(screen)
        elif (s[idx] == 'save'):
            clear_screen(screen)
            draw_lines(edges, screen, color )
            save_extension(screen, s[idx + 1])
        idx += 1