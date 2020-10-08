# Python program to implement Runge Kutta method 
#The derivative function
def dydx(x, y): 
    #return (3*(18-y))  
    return (x+y**2)

# Finds value of y for a given x using step size h 
# and initial value y0 at x0. 
def rungeKutta(x0, y0, x, h): 
    # Count number of iterations using step size or 
    # step height h 
    n = int(((x - x0)/h)) 
    y = y0 
    
    # Iterate for number of iterations 
    for i in range(1, n + 1): 
        
        # The Runge-Kutta Formulas for calculating the change in y for 
        #change in x of h
        k1 = h * dydx(x0, y) 
        k2 = h * dydx(x0 + 0.5 * h, y + 0.5 * k1) 
        k3 = h * dydx(x0 + 0.5 * h, y + 0.5 * k2) 
        k4 = h * dydx(x0 + h, y + k3) 
  
        # Update next value of y 
        y = y + k1/6 + k2/3 + k3/3 + k4/6 
  
        # Update next value of x 
        x0 = x0 + h 
    return y 
  
# Driver method 
x0 = 0
y0 = 0
x = 0.3
h = 0.005

print ('The value of the stock at time 1 is:', rungeKutta(x0, y0, x, h) )





