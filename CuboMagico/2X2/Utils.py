"""
To do:
    cube          [X]
    show cube     [X]
    rotate cube   [X]
    solve cube    []
"""
import numpy as np


def create_cube(up='W', color_up='\033[1;97m', front='G', color_front='\033[1;32m',
                down='Y', color_down='\033[1;93m', back='B', color_back='\033[1;34m',
                left='O', color_left='\033[1;38;5;208m', right='R', color_right='\033[1;31m'):

    return ([
            [f'{color_up}1{up}', f'{color_up}2{up}',
             f'{color_up}3{up}', f'{color_up}4{up}'],

            [f'{color_front}1{front}', f'{color_front}2{front}',
             f'{color_front}3{front}', f'{color_front}4{front}'],

            [f'{color_down}1{down}', f'{color_down}2{down}',
             f'{color_down}3{down}', f'{color_down}4{down}'],

            [f'{color_back}1{back}', f'{color_back}2{back}',
             f'{color_back}3{back}', f'{color_back}4{back}'],

            [f'{color_left}1{left}', f'{color_left}2{left}',
             f'{color_left}3{left}', f'{color_left}4{left}'],

            [f'{color_right}1{right}', f'{color_right}2{right}',
             f'{color_right}3{right}', f'{color_right}4{right}']
            ])


cube = create_cube()


def show_cube(cb, null_color='\033[0m', up=0, front=1, down=2, back=3, left=4, right=5):
    print(
          f'      {cb[up][0]} {cb[up][1]}\n'
          f'      {cb[up][3]} {cb[up][2]}\n'
          f'{cb[left][0]} {cb[left][1]} {cb[front][0]} {cb[front][1]} {cb[right][0]} {cb[right][1]}\n'
          f'{cb[left][3]} {cb[left][2]} {cb[front][3]} {cb[front][2]} {cb[right][3]} {cb[right][2]}\n'
          f'      {cb[down][0]} {cb[down][1]}\n'
          f'      {cb[down][3]} {cb[down][2]}\n'
          f'      {cb[back][0]} {cb[back][1]}\n'
          f'      {cb[back][3]} {cb[back][2]}\n'
          f'{null_color}'
    )


def rotate(com, cb=np.array(cube), cube_is_shown=True, show_command=True):
    match com:
        case "R":
            cb[5][0], cb[5][1], cb[5][2], cb[5][3] = \
                cb[5][3], cb[5][0], cb[5][1], cb[5][2]

            (cb[1][1], cb[1][2], cb[0][1], cb[0][2],
             cb[3][1], cb[3][2], cb[2][1], cb[2][2]) = \
                (cb[2][1], cb[2][2], cb[1][1], cb[1][2],
                 cb[0][1], cb[0][2], cb[3][1], cb[3][2])

        case "R'":
            cb[5][0], cb[5][1], cb[5][2], cb[5][3] = \
                cb[5][1], cb[5][2], cb[5][3], cb[5][0]

            (cb[1][1], cb[1][2], cb[0][1], cb[0][2],
             cb[3][1], cb[3][2], cb[2][1], cb[2][2]) = \
                (cb[0][1], cb[0][2], cb[3][1], cb[3][2],
                 cb[2][1], cb[2][2], cb[1][1], cb[1][2])

        case "R2":
            cb[5][0], cb[5][1], cb[5][2], cb[5][3] = \
                cb[5][2], cb[5][3], cb[5][0], cb[5][1]

            (cb[1][1], cb[1][2], cb[0][1], cb[0][2],
             cb[3][1], cb[3][2], cb[2][1], cb[2][2]) = \
                (cb[3][1], cb[3][2], cb[2][1], cb[2][2],
                 cb[1][1], cb[1][2], cb[0][1], cb[0][2])

        case "L":
            cb[4][0], cb[4][1], cb[4][2], cb[4][3] = \
                cb[4][3], cb[4][0], cb[4][1], cb[4][2]

            (cb[3][0], cb[3][3], cb[2][0], cb[2][3],
             cb[1][0], cb[1][3], cb[0][0], cb[0][3]) = \
                (cb[2][0], cb[2][3], cb[1][0], cb[1][3],
                 cb[0][0], cb[0][3], cb[3][0], cb[3][3])

        case "L'":
            cb[4][0], cb[4][1], cb[4][2], cb[4][3] = \
                cb[4][1], cb[4][2], cb[4][3], cb[4][0]

            (cb[3][0], cb[3][3], cb[2][0], cb[2][3],
             cb[1][0], cb[1][3], cb[0][0], cb[0][3]) = \
                (cb[0][0], cb[0][3], cb[3][0], cb[3][3],
                 cb[2][0], cb[2][3], cb[1][0], cb[1][3])

        case "L2":
            cb[4][0], cb[4][1], cb[4][2], cb[4][3] = \
                cb[4][2], cb[4][3], cb[4][0], cb[4][1]

            (cb[3][0], cb[3][3], cb[2][0], cb[2][3],
             cb[1][0], cb[1][3], cb[0][0], cb[0][3]) = \
                (cb[1][0], cb[1][3], cb[0][0], cb[0][3],
                 cb[3][0], cb[3][3], cb[2][0], cb[2][3])

        case "U":
            cb[0][0], cb[0][1], cb[0][2], cb[0][3] = \
                cb[0][3], cb[0][0], cb[0][1], cb[0][2]

            (cb[1][0], cb[1][1], cb[5][0], cb[5][1],
             cb[3][2], cb[3][3], cb[4][0], cb[4][1]) = \
                (cb[5][0], cb[5][1], cb[3][2], cb[3][3],
                 cb[4][0], cb[4][1], cb[1][0], cb[1][1])

        case "U'":
            cb[0][0], cb[0][1], cb[0][2], cb[0][3] = \
                cb[0][1], cb[0][2], cb[0][3], cb[0][0]

            (cb[1][0], cb[1][1], cb[5][0], cb[5][1],
             cb[3][2], cb[3][3], cb[4][0], cb[4][1]) = \
                (cb[4][0], cb[4][1], cb[1][0], cb[1][1],
                 cb[5][0], cb[5][1], cb[3][2], cb[3][3])

        case "U2":
            cb[0][0], cb[0][1], cb[0][2], cb[0][3] = \
                cb[0][2], cb[0][3], cb[0][0], cb[0][1]

            (cb[1][0], cb[1][1], cb[5][0], cb[5][1],
             cb[3][2], cb[3][3], cb[4][0], cb[4][1]) = \
                (cb[3][2], cb[3][3], cb[4][0], cb[4][1],
                 cb[1][0], cb[1][1], cb[5][0], cb[5][1])

        case "D":
            cb[2][0], cb[2][1], cb[2][2], cb[2][3] = \
                cb[2][3], cb[2][0], cb[2][1], cb[2][2]

            (cb[3][0], cb[3][1], cb[4][2], cb[4][3],
             cb[1][2], cb[1][3], cb[5][2], cb[5][3]) = \
                (cb[5][2], cb[5][3], cb[3][0], cb[3][1],
                 cb[4][2], cb[4][3], cb[1][2], cb[1][3])

        case "D'":
            cb[2][0], cb[2][1], cb[2][2], cb[2][3] = \
                cb[2][1], cb[2][2], cb[2][3], cb[2][0]

            (cb[3][0], cb[3][1], cb[4][2], cb[4][3],
             cb[1][2], cb[1][3], cb[5][2], cb[5][3]) = \
                (cb[4][2], cb[4][3], cb[1][2], cb[1][3],
                 cb[5][2], cb[5][3], cb[3][0], cb[3][1])

        case "D2":
            cb[2][0], cb[2][1], cb[2][2], cb[2][3] = \
                cb[2][2], cb[2][3], cb[2][0], cb[2][1]

            (cb[3][0], cb[3][1], cb[4][2], cb[4][3],
             cb[1][2], cb[1][3], cb[5][2], cb[5][3]) = \
                (
                cb[1][2], cb[1][3], cb[5][2], cb[5][3],
                cb[3][0], cb[3][1], cb[4][2], cb[4][3])

        case "F":
            cb[1][0], cb[1][1], cb[1][2], cb[1][3] = \
                cb[1][3], cb[1][0], cb[1][1], cb[1][2]

            (cb[0][2], cb[0][3], cb[4][1], cb[4][2],
             cb[2][0], cb[2][1], cb[5][3], cb[5][0]) = \
                (cb[4][1], cb[4][2], cb[2][0], cb[2][1],
                 cb[5][3], cb[5][0], cb[0][2], cb[0][3])

        case "F'":
            cb[1][0], cb[1][1], cb[1][2], cb[1][3] = \
                cb[1][1], cb[1][2], cb[1][3], cb[1][0]

            (cb[0][2], cb[0][3], cb[4][1], cb[4][2],
             cb[2][0], cb[2][1], cb[5][3], cb[5][0]) = \
                (cb[5][3], cb[5][0], cb[0][2], cb[0][3],
                 cb[4][1], cb[4][2], cb[2][0], cb[2][1])

        case "F2":
            cb[1][0], cb[1][1], cb[1][2], cb[1][3] = \
                cb[1][2], cb[1][3], cb[1][0], cb[1][1]

            (cb[0][2], cb[0][3], cb[4][1], cb[4][2],
             cb[2][0], cb[2][1], cb[5][3], cb[5][0]) = \
                (cb[2][0], cb[2][1], cb[5][3], cb[5][0],
                 cb[0][2], cb[0][3], cb[4][1], cb[4][2])

        case "B":
            cb[3][0], cb[3][1], cb[3][2], cb[3][3] = \
                cb[3][3], cb[3][0], cb[3][1], cb[3][2]

            (cb[2][2], cb[2][3], cb[4][3], cb[4][0],
             cb[0][0], cb[0][1], cb[5][1], cb[5][2]) = \
                (cb[4][3], cb[4][0], cb[0][0], cb[0][1],
                 cb[5][1], cb[5][2], cb[2][2], cb[2][3])

        case "B'":
            cb[3][0], cb[3][1], cb[3][2], cb[3][3] = \
                cb[3][1], cb[3][2], cb[3][3], cb[3][0]

            (cb[2][2], cb[2][3], cb[4][3], cb[4][0],
             cb[0][0], cb[0][1], cb[5][1], cb[5][2]) = \
                (cb[5][1], cb[5][2], cb[2][2], cb[2][3],
                 cb[4][3], cb[4][0], cb[0][0], cb[0][1])

        case "B2":
            cb[3][0], cb[3][1], cb[3][2], cb[3][3] = \
                cb[3][2], cb[3][3], cb[3][0], cb[3][1]

            (cb[2][2], cb[2][3], cb[4][3], cb[4][0],
             cb[0][0], cb[0][1], cb[5][1], cb[5][2]) = \
                (cb[0][0], cb[0][1], cb[5][1], cb[5][2],
                 cb[2][2], cb[2][3], cb[4][3], cb[4][0])

    if show_command:
        print(f'Command = {com}')
    if cube_is_shown:
        show_cube(cb)


'''def rotate(com, cb=cube, cube_is_shown=True, show_command=True):

    if com == "R":
        cb[5][0], cb[5][1], cb[5][2], cb[5][3] = \
            cb[5][3], cb[5][0], cb[5][1], cb[5][2]

        (cb[1][1], cb[1][2], cb[0][1], cb[0][2],
            cb[3][1], cb[3][2], cb[2][1], cb[2][2]) = \
            (cb[2][1], cb[2][2], cb[1][1], cb[1][2],
                cb[0][1], cb[0][2], cb[3][1], cb[3][2])

    elif com == "R'":
        cb[5][0], cb[5][1], cb[5][2], cb[5][3] = \
            cb[5][1], cb[5][2], cb[5][3], cb[5][0]

        (cb[1][1], cb[1][2], cb[0][1], cb[0][2],
            cb[3][1], cb[3][2], cb[2][1], cb[2][2]) = \
            (cb[0][1], cb[0][2], cb[3][1], cb[3][2],
                cb[2][1], cb[2][2], cb[1][1], cb[1][2])
        
    elif com == "R2":
        cb[5][0], cb[5][1], cb[5][2], cb[5][3] = \
            cb[5][2], cb[5][3], cb[5][0], cb[5][1]

        (cb[1][1], cb[1][2], cb[0][1], cb[0][2],
            cb[3][1], cb[3][2], cb[2][1], cb[2][2]) = \
            (cb[3][1], cb[3][2], cb[2][1], cb[2][2],
            cb[1][1], cb[1][2], cb[0][1], cb[0][2])

    elif com == "L":
        cb[4][0], cb[4][1], cb[4][2], cb[4][3] = \
            cb[4][3], cb[4][0], cb[4][1], cb[4][2]

        (cb[3][0], cb[3][3], cb[2][0], cb[2][3],
            cb[1][0], cb[1][3], cb[0][0], cb[0][3]) = \
            (cb[2][0], cb[2][3], cb[1][0], cb[1][3],
                cb[0][0], cb[0][3], cb[3][0], cb[3][3])

    elif com == "L'":
        cb[4][0], cb[4][1], cb[4][2], cb[4][3] = \
            cb[4][1], cb[4][2], cb[4][3], cb[4][0]

        (cb[3][0], cb[3][3], cb[2][0], cb[2][3],
            cb[1][0], cb[1][3], cb[0][0], cb[0][3]) = \
            (cb[0][0], cb[0][3], cb[3][0], cb[3][3],
                cb[2][0], cb[2][3], cb[1][0], cb[1][3])
        
    elif com == "L2":
        cb[4][0], cb[4][1], cb[4][2], cb[4][3] = \
            cb[4][2], cb[4][3], cb[4][0], cb[4][1]

        (cb[3][0], cb[3][3], cb[2][0], cb[2][3],
            cb[1][0], cb[1][3], cb[0][0], cb[0][3]) = \
            (cb[1][0], cb[1][3], cb[0][0], cb[0][3],
            cb[3][0], cb[3][3], cb[2][0], cb[2][3]) 

    elif com == "U":
        cb[0][0], cb[0][1], cb[0][2], cb[0][3] = \
            cb[0][3], cb[0][0], cb[0][1], cb[0][2]

        (cb[1][0], cb[1][1], cb[5][0], cb[5][1],
            cb[3][2], cb[3][3], cb[4][0], cb[4][1]) = \
            (cb[5][0], cb[5][1], cb[3][2], cb[3][3],
                cb[4][0], cb[4][1], cb[1][0], cb[1][1])

    elif com == "U'":
        cb[0][0], cb[0][1], cb[0][2], cb[0][3] = \
            cb[0][1], cb[0][2], cb[0][3], cb[0][0]

        (cb[1][0], cb[1][1], cb[5][0], cb[5][1],
            cb[3][2], cb[3][3], cb[4][0], cb[4][1]) = \
            (cb[4][0], cb[4][1], cb[1][0], cb[1][1],
                cb[5][0], cb[5][1], cb[3][2], cb[3][3])
        
    elif com == "U2":
        cb[0][0], cb[0][1], cb[0][2], cb[0][3] = \
            cb[0][2], cb[0][3], cb[0][0], cb[0][1]

        (cb[1][0], cb[1][1], cb[5][0], cb[5][1],
            cb[3][2], cb[3][3], cb[4][0], cb[4][1]) = \
            (cb[3][2], cb[3][3], cb[4][0], cb[4][1],
                cb[1][0], cb[1][1], cb[5][0], cb[5][1])

    elif com == "D":
        cb[2][0], cb[2][1], cb[2][2], cb[2][3] = \
            cb[2][3], cb[2][0], cb[2][1], cb[2][2]

        (cb[3][0], cb[3][1], cb[4][2], cb[4][3],
            cb[1][2], cb[1][3], cb[5][2], cb[5][3]) = \
            (cb[5][2], cb[5][3], cb[3][0], cb[3][1],
                cb[4][2], cb[4][3], cb[1][2], cb[1][3])

    elif com == "D'":
        cb[2][0], cb[2][1], cb[2][2], cb[2][3] = \
            cb[2][1], cb[2][2], cb[2][3], cb[2][0]

        (cb[3][0], cb[3][1], cb[4][2], cb[4][3],
            cb[1][2], cb[1][3], cb[5][2], cb[5][3]) = \
            (cb[4][2], cb[4][3], cb[1][2], cb[1][3],
                cb[5][2], cb[5][3], cb[3][0], cb[3][1])
        
    elif com == "D2":
        cb[2][0], cb[2][1], cb[2][2], cb[2][3] = \
            cb[2][2], cb[2][3], cb[2][0], cb[2][1]

        (cb[3][0], cb[3][1], cb[4][2], cb[4][3],
            cb[1][2], cb[1][3], cb[5][2], cb[5][3]) = \
            (
            cb[1][2], cb[1][3], cb[5][2], cb[5][3],
            cb[3][0], cb[3][1], cb[4][2], cb[4][3])

    elif com == "F":
        cb[1][0], cb[1][1], cb[1][2], cb[1][3] = \
            cb[1][3], cb[1][0], cb[1][1], cb[1][2]

        (cb[0][2], cb[0][3], cb[4][1], cb[4][2],
            cb[2][0], cb[2][1], cb[5][3], cb[5][0]) = \
            (cb[4][1], cb[4][2], cb[2][0], cb[2][1],
                cb[5][3], cb[5][0], cb[0][2], cb[0][3])

    elif com == "F'":
        cb[1][0], cb[1][1], cb[1][2], cb[1][3] = \
            cb[1][1], cb[1][2], cb[1][3], cb[1][0]

        (cb[0][2], cb[0][3], cb[4][1], cb[4][2],
            cb[2][0], cb[2][1], cb[5][3], cb[5][0]) = \
            (cb[5][3], cb[5][0], cb[0][2], cb[0][3],
                cb[4][1], cb[4][2], cb[2][0], cb[2][1])
        
    elif com == "F2":
        cb[1][0], cb[1][1], cb[1][2], cb[1][3] = \
            cb[1][2], cb[1][3], cb[1][0], cb[1][1]

        (cb[0][2], cb[0][3], cb[4][1], cb[4][2],
            cb[2][0], cb[2][1], cb[5][3], cb[5][0]) = \
            (cb[2][0], cb[2][1], cb[5][3], cb[5][0],
                cb[0][2], cb[0][3], cb[4][1], cb[4][2])


    elif com == "B":
        cb[3][0], cb[3][1], cb[3][2], cb[3][3] = \
            cb[3][3], cb[3][0], cb[3][1], cb[3][2]

        (cb[2][2], cb[2][3], cb[4][3], cb[4][0],
            cb[0][0], cb[0][1], cb[5][1], cb[5][2]) = \
            (cb[4][3], cb[4][0], cb[0][0], cb[0][1],
                cb[5][1], cb[5][2], cb[2][2], cb[2][3])

    elif com == "B'":
        cb[3][0], cb[3][1], cb[3][2], cb[3][3] = \
            cb[3][1], cb[3][2], cb[3][3], cb[3][0]

        (cb[2][2], cb[2][3], cb[4][3], cb[4][0],
            cb[0][0], cb[0][1], cb[5][1], cb[5][2]) = \
            (cb[5][1], cb[5][2], cb[2][2], cb[2][3],
                cb[4][3], cb[4][0], cb[0][0], cb[0][1])
        
    elif com == "B2":
        cb[3][0], cb[3][1], cb[3][2], cb[3][3] = \
            cb[3][2], cb[3][3], cb[3][0], cb[3][1]

        (cb[2][2], cb[2][3], cb[4][3], cb[4][0],
            cb[0][0], cb[0][1], cb[5][1], cb[5][2]) = \
            (cb[0][0], cb[0][1], cb[5][1], cb[5][2],
            cb[2][2], cb[2][3], cb[4][3], cb[4][0])

    if show_command:
        print(f'Command = {com}')
    if cube_is_shown:
        show_cube(cb)

'''


def scramble(possible_movements=np.array(["R", "R'", "R2", "L", "L'", "L2", "U", "U'", "U2",
                                          "D", "D'", "D2", "F", "F'", "F2", "B", "B'", "B2"]),
             cb=np.array(cube), cube_is_shown=True, show_command=True):

    sc = np.random.randint(0, len(possible_movements), 15+np.random.randint(0, 2))
    for i in sc:
        rotate(possible_movements[i], cb,  cube_is_shown, show_command)


for movements in ["R", "R'", "R2", "R2", "L", "L'", "L2", "L2", "U", "U'", "U2", "U2",
                  "D", "D'", "D2", "D2", "F", "F'", "F2", "F2", "B", "B'", "B2", "B2"]:
    rotate(movements)

# scramble()
