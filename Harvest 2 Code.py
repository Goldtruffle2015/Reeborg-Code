think(0)
set_max_nb_steps(10000)
'''
"Title: Harvest 2 Code"
"Author: John Yu"
"Date: March 9, 2018"
'''
# --- Subroutines ---#
def turn_right():
    repeat 3:
        turn_left()
# --- Variables ---#
carrotNum = 0
# --- Code Starts Here ---#
while carrotNum < 1 or not carrots_in_column == 0:
    #Get to standard orientation
    if is_facing_north():
        if front_is_clear():
            #Reset carrots_in_column
            carrots_in_column = 0
            #Search Columns
            while front_is_clear():
                if object_here():
                    take()
                    carrotNum += 1
                    carrots_in_column += 1
                else:
                    move()
        #Turn around and go back down
        else:
            turn_right()
            move()
            turn_right()
            while front_is_clear():
                move()
    #turn until facing north
    else:
        turn_left()
done()
