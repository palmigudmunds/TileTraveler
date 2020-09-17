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