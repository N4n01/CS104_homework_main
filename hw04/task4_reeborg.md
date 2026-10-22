For Hurdle 3 and Hurdle 4:

def turn_right() :
    for i in range(3) :
        turn_left()

def jump() :
    count = 0
    turn_left()
    while wall_on_right():
        move()
        count += 1
    turn_right()
    move()
    turn_right()
    for i in range(count) :
        move()
    turn_left()
    
while not at_goal() :
    if wall_in_front() :
        jump()
    else :
        move()

For Maze :
def turn_right() :
    for i in range(3) :
        turn_left()
#Get the reeborg right next to a wall and face away from the wall        
while front_is_clear() and not at_goal(): 
    move()    
turn_left() 

#Keep on tracing the walls until reach destination
while not at_goal(): 
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()