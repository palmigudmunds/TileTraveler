# Git Repo: https://github.com/palmigudmunds/TileTraveler

x = 1
y = 1

def moveUp(y):
    y += 1
    return y

def moveDown(y):
    y -= 1
    return y

def moveLeft(x):
    x -= 1
    return x

def moveRight(x):
    x += 1
    return x

def north(user_input,x,y):
    if user_input == 'n' or user_input == 'N':
        y = moveUp(y)
        return True,x,y
    else:
        return False,x,y
        
def south(user_input,x,y):
    if user_input == 's' or user_input == 'S':
        y = moveDown(y)
        return True,x,y
    else:
        return False,x,y

def east(user_input,x,y):
    if user_input == 'e' or user_input == 'E':
        x = moveRight(x)
        return True,x,y
    else:
        return False,x,y

def west(user_input,x,y):
    if user_input == 'w' or user_input == 'W':
        x = moveLeft(x)
        return True,x,y
    else:
        return False,x,y
gameNotOver = True

while gameNotOver:

    if x==1 and y==1:
        print("You can travel: (N)orth.")
        user_input = input("Direction: ")
        valid,new_x,new_y = north(user_input,x,y)
        if valid == False:
            print("Not a valid direction!")
        else:
            x=new_x
            y=new_y

    elif x==1 and y==2:
        print("You can travel: (N)orth or (E)ast or (S)outh.")
        user_input = input("Direction: ")
        if user_input == 's' or user_input == 'S':
            valid,new_x,new_y = south(user_input,x,y)
        elif user_input == 'n' or user_input == 'N':
            valid,new_x,new_y = north(user_input,x,y)
        elif user_input == 'e' or user_input == 'E':
            valid,new_x,new_y = east(user_input,x,y)
        else:
            valid = False
        if valid == False:
            print("Not a valid direction!")
        else:
            x=new_x
            y=new_y       
        
    elif x==2 and y==2:
        print("You can travel: (S)outh or (W)est.")
        user_input = input("Direction: ")
        if user_input == 's' or user_input == 'S':
            valid,new_x,new_y = south(user_input,x,y)
        elif user_input == 'w' or user_input == 'W':
            valid,new_x,new_y = west(user_input,x,y)
        else:
            valid = False
        if valid == False:
            print("Not a valid direction!")
        else:
            x=new_x
            y=new_y

    elif x==2 and y==1:
        print("You can travel: (N)orth.")
        user_input = input("Direction: ")
        if user_input == 'n' or user_input == 'N':
            valid,new_x,new_y = north(user_input,x,y)
        else:
            valid = False
        if valid == False:
            print("Not a valid direction!")
        else:
            x=new_x
            y=new_y

    elif x==1 and y==3:
        print("You can travel: (E)ast or (S)outh.")
        user_input = input("Direction: ")
        if user_input == 's' or user_input == 'S':
            valid,new_x,new_y = south(user_input,x,y)
        elif user_input == 'e' or user_input == 'E':
            valid,new_x,new_y = east(user_input,x,y)
        else:
            valid = False
        if valid == False:
            print("Not a valid direction!")
        else:
            x=new_x
            y=new_y

    elif x==2 and y==3:
        print("You can travel: (E)ast or (W)est.")
        user_input = input("Direction: ")
        if user_input == 'e' or user_input == 'E':
            valid,new_x,new_y = east(user_input,x,y)
        elif user_input == 'w' or user_input == 'W':
            valid,new_x,new_y = west(user_input,x,y)
        else:
            valid = False
        if valid == False:
            print("Not a valid direction!")
        else:
            x=new_x
            y=new_y

    elif x==3 and y==3:
        print("You can travel: (S)outh or (W)est.")
        user_input = input("Direction: ")
        if user_input == 's' or user_input == 'S':
            valid,new_x,new_y = south(user_input,x,y)
        elif user_input == 'w' or user_input == 'W':
            valid,new_x,new_y = west(user_input,x,y)
        else:
            valid = False
        if valid == False:
            print("Not a valid direction!")
        else:
            x=new_x
            y=new_y

    elif x==3 and y==2:
        print("You can travel: (N)orth or (S)outh.")
        user_input = input("Direction: ")
        if user_input == 'n' or user_input == 'N':
            valid,new_x,new_y = north(user_input,x,y)
        elif user_input == 's' or user_input == 'S':
            valid,new_x,new_y = south(user_input,x,y)
        else:
            valid = False
        if valid == False:
            print("Not a valid direction!")
        else:
            x=new_x
            y=new_y

    elif x==3 and y==1:
        print("Victory!")
        gameNotOver = False