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
# Step 1: Count D1N1
# Short for Digit 1 in Number 1
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
'''
Insert Operation Below
'''
Total = Num1 - Num2
# Step 6: Write out Digit1
# Digit1 stands for digit in the ones place
Digit1 = Total%10
for i in range(Digit1):
    put()
# Step 7: Write out Digit2
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
# Step 8: Write out Digit3
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
# Step 9: Write out Digit4
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
# Step 10: Move out of the way
turn_left()
move()
done()
