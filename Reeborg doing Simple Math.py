think(0)
'''
Title: Reeborg doing simple math
Author: John Yu
Date: March 14, 2018
'''
# --- Subroutines --- #
def turn_right():
    repeat 3:
        turn_left()
def turn_around():
    repeat 2:
        turn_left()
def go_to_next_placeholder():
    turn_left()
    move()
    repeat 3:
        turn_left()
    build_wall()
# --- Code Starts Here --- #
move()
# Step 1.00: Count D1N1
# Short for Digit 1 in Number 1
D1N1 = 0
while object_here():
    take()
    D1N1 += 1
for i in range(D1N1):
    put()
turn_right()
move()
# Step 1.25: Count D2N1
# D2N1 is short for Digit 2 in Number 1
# Decimal is due to this step being an 
# iteration of step 1.00
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
# Step 1.50: Count D1N2
# D1N2 is short for Digit 1 in Number 2
D1N2 = 0
while object_here():
    take()
    D1N2 += 1
for i in range(D1N2):
    put()
turn_right()
move()
# Step 1.75: Count D2N2
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
# Step 2: Calculate the total
Num1 = (10 * D2N1) + D1N1
Num2 = (10 * D2N2) + D1N2
'''
Insert Operation Below ( "+" , "-" , "*" )
'''
Total = Num1 * Num2
# Step 3.00: Write out Digit1
# Digit1 stands for digit in the ones place
Digit1 = Total%10
for i in range(Digit1):
    put()
# Step 3.25: Write out Digit2
# Digit2 stands for digit in the tens place
go_to_next_placeholder()
Pseudo_Digit2 = Total%100
Digit2 = 0
while Pseudo_Digit2 > 0:
    Pseudo_Digit2 += -10
    Digit2 += 1
if Pseudo_Digit2 < 0:
    Digit2 += -1
else:
    pass
for i in range(Digit2):
    put()
# Step 3.50: Write out Digit3
# Digit3 stands for digit in the hundreds place
go_to_next_placeholder()
Pseudo_Digit3 = Total%1000
Digit3 = 0
while Pseudo_Digit3 > 0:
    Pseudo_Digit3 += -100
    Digit3 += 1
if Pseudo_Digit3 < 0:
    Digit3 += -1
else:
    pass
for i in range(Digit3):
    put()
# Step 3.75: Write out Digit4
# Digit4 stands for digit in the thousands place
go_to_next_placeholder()
Pseudo_Digit4 = Total%10000
Digit4 = 0
while Pseudo_Digit4 > 0:
    Pseudo_Digit4 += -1000
    Digit4 += 1
if Pseudo_Digit4 < 0:
    Digit4 += -1
else:
    pass
for i in range(Digit4):
    put()
# Step 4: Move out of the way
turn_left()
move()
done()
