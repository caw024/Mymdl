import mdl
from display import *
from matrix import *
from draw import *

#look at mdl.[y

def run(filename):
    """
    This function runs an mdl script
    """
    p = mdl.parseFile(filename)

    if p:
        (commands, symbols) = p
    else:
        print "Parsing failed."
        return

    view = [0,
            0,
            1];
    ambient = [50,
               50,
               50]
    light = [[0.5,
              0.75,
              1],
             [255,
              255,
              255]]

    color = [0, 0, 0]
    tmp = new_matrix()
    ident( tmp )

    stack = [ [x[:] for x in tmp] ]
    screen = new_screen()
    zbuffer = new_zbuffer()
    tmp = []
    step_3d = 100
    consts = ''
    coords = []
    coords1 = []
    symbols['.white'] = ['constants',
                         {'red': [0.2, 0.5, 0.5],
                          'green': [0.2, 0.5, 0.5],
                          'blue': [0.2, 0.5, 0.5]}]
    commands.append('push')
    commands.append('pop')
    commands.append('move')
    commands.append('scale')
    commands.append('rotate')
    commands.append('sphere')
    commands.append('torus')
    commands.append('box')
    commands.append('line')
    commands.append('constants')
    commands.append('save')
    commands.append('display')
    

    reflect = '.white'

    print symbols
    for command in commands:
        print command
