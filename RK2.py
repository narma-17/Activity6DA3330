#The derivative function
def dydx(x, y): 
    return (3*(18-y))  
  
#function for Runge-Kutta Method
def rungeKutta(x0, y0, x, h): 
    # Count number of iterations using step size or 
    # step height h 
    n = (int)((x - x0)/h)   
    y = y0 
    # Iterate for number of iterations
    for i in range(1, n + 1): 
        "Apply Runge Kutta Formulas to find next value of y"
        k1 = h * dydx(x0, y)# change based on derivative at starting point
        k2 = h * dydx(x0 + 0.5 * h, y + 0.5 * k1)#midpoint step to cancel lower
        #order error terms
       
        # Update next value of y 
        y = y+k2
  
        # Update next value of x 
        x0 = x0 + h 
    return y 
  
# Driver method 
x0 = 0
y0 = 14
x = 1
h = 0.1
print ('The value of the stock at time 1 is:', rungeKutta(x0, y0, x, h) )





