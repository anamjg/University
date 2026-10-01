# CALCULATOR FUNCTIONS:

from shutil import ExecError


def add(x: float, y: float):
    return x + y

def div(x:float, y:float):
    if y == 0:
        raise ZeroDivisionError('Division is invalid since denominator is 0')    
    return x/y

def fac(x:int):
    if x < 0:
        raise ValueError(f"Invalid value for factorial calculation, try again with a positive number.")
    elif x == 0:
        return 1
    elif type(x) == float:
        raise ValueError(f'Invalid type of x, got {type(x)} expected int.')
    a = 1
    for n in range(1, x+1):
        a = a*n
    return a

def sinus(x, N=20):
    s = 0
    for n in range(N):
        s += ((-1)**n*x**(2*n+1))/fac(2*n+1)
    return s

def square_root(y:float, x0: float = 1): 
    '''
    We have the sequence:
        x_n = f_y(x_(n-1)) = 1/2 * (y/x_(n_1)+x_(n_1))
    
    This sequence can we also write as:
        x_(n+1) = f_y(x_n) = 1/2 * (y/x_n + x_n)
    
    If we write with common denominator then we have:
        x_(n+1) = ((x_n)^2 + y)/2*x_n
        
    To calculate √y we notice that: 
        1. x * y/x = y = √y * √y
        2. If x < √y, then y/x > √y
        3. If x > √y, then y/x < √y
    '''
    
    if y == 0:
        return 0
   
    s = y/2.0
    s2 = s+x0
    while s != s2:
        n = y/s
        s2 = s
        s = (s+n)/2
    return s

    