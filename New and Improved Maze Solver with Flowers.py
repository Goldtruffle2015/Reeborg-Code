'''
"Title: New and Improved Maze Solver with flowers"
"Author: John Yu
"Date: March 9, 2018"
'''
think(0)
set_max_nb_steps(10000)
# variables
def turn_right():
    repeat 3:
        turn_left()
def turn_around():
    repeat 2:
        turn_left()
Reeborg_Turned_Right = False 
# CODE STARTS HERE
if at_goal():
    turn_around()
    move()
    while not at_goal():
        while object_here():
            take()
        if right_is_clear():
            turn_right()
            move()
        elif front_is_clear():
            move()
        else:
            turn_left()
else:
    while not at_goal():
        while object_here():
            take()
        walls = 0
        repeat 4:
            if wall_in_front():
                walls += 1
                turn_left()
            else:
                turn_left()
        if walls == 4:
            done()
        else:
            if walls == 3:
                while not front_is_clear():
                    turn_left()
                move()
                turn_around()
                build_wall()
                turn_around()
            else:
                if Reeborg_Turned_Right == False:
                    rightNum = 0
                else:
                    pass
                if right_is_clear():
                    turn_right()
                    rightNum += 1
                    Reeborg_Turned_Right = True
                    move()
                    if rightNum > 4:
                        turn_left()
                    else:
                        pass
                else:
                    Reeborg_Turned_Right = False
                    if front_is_clear():
                        move()
                    else:
                        turn_left()