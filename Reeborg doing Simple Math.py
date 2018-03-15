think(0)
"Title: Reeborg doing simple math"
"Author: John Yu"
"Date: March 14, 2018"
# --- Subroutines --- #
def turn_right():
    repeat 3:
        turn_left()
def turn_around():
    repeat 2:
        turn_left()
# --- Code Starts Here --- #
move()
# Short for Digit 1 in Number 1
# Step 1: Count D1N1
D1N1 = 0
while object_here():
    take()
    D1N1 += 1
for i in range(D1N1):
    put()
turn_right()
move()
# Step 2: Count D2N1
# D2N1 is short for Digit 2 in Number 1
D2N1 = 0
while object_here():
    take()
    D2N1 += 1
for i in range(D2N1):
    put()
turn_around()
move()
turn_right()
move()
# Step 3: Count D1N2
# D1N2 is short for Digit 1 in Number 2
D1N2 = 0
while object_here():
    take()
    D1N2 += 1
for i in range(D1N2):
    put()
turn_right()
move()
# Step 4: Count D2N2
# D2N2 is short for Digit 2 in Number 2
D2N2 = 0
while object_here():
    take()
    D2N2 += 1
for i in range(D2N2):
    put()
turn_around()
move()
turn_right()
move()
turn_around()
build_wall()
# Step 5: Calculate the total
Num1 = (10 * D2N1) + D1N1
Num2 = (10 * D2N2) + D1N2
###--- Operation below is changeable ---###
Total = Num2 + Num1
# Step 6: Write out D1
# D1 stands for digit in the ones place
D1 = (((Total%1000)%100)%10)
for i in range(D1):
    put()
turn_left()
move()
turn_right()
build_wall()
# Step 7: Write out D2
# D2 stands for digit in the tens place