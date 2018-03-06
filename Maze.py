from random import randint
from library import*
think(10)

while not at_goal():
    

    walls =""

    if wall_in_front():
        walls += "1"
    turn(1)
    if wall_in_front():
        walls += "2"
    turn(1)
    if wall_in_front():
        walls += "3"
    turn(1)
    if wall_in_front():
        walls += "4"
    turn(1)

    #print(walls)

    if len(walls) == 4:
        print("FUCK")
        done()
    elif len(walls) == 3:
        if not "1" in walls:
            turnAndBuild(0)
        elif not "2" in walls:
            turnAndBuild(1)
        elif not "4" in walls:
            turnAndBuild(3)
        elif not "3" in walls:
            turnAndBuild(2) 
        else:
            print("something went wrong")
    elif len(walls) == 2:
        if not "1" in walls:
            move()
        elif not "2" in walls:
            turn(1)
            move()
        elif not "4" in walls:
            turn(3)
            move()
        else:
            turn(2)
            move()
    elif len(walls) == 1:
        if not "1" in walls:
            move()
        elif not "2" in walls:
            turn(1)
            move()
        elif not "4" in walls:
            turn(3)
            move()
        else:
            turn(2)
            move()
    elif len(walls) == 0:
        rand = randint(1,3)
        if rand == 3:
            turn(3)
            move()
        else:
            turn(rand - 1)
            move()
            





################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
def turn(amt):
    for x in range (0,amt):
        turn_left()

def turnAndBuild(amt):
    turn(amt)
    move()
    turn(2)
    build_wall()
    turn(2)