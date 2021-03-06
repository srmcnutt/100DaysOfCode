# 100 days of code day 6 - Steven McNutt 2021
# robot maze
#
# https://reeborg.ca/ maze option.

def turn_right():
    turn_left()
    turn_left()
    turn_left()

# find a wall
while front_is_clear():
    move()
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
