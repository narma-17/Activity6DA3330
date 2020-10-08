# Python Code to find approximation 
# of a ordinary differential equation 
# using euler method. 

#first order derivative function to find the value at time t
def func( t, V ): 
    return (3*(18-V)) 
    #return (t+V**2)
      
# Function for euler formula 
def euler( t0, V, h, t ): 

    # Iterating till the point at which we 
    # need approximation 
    while t0 < t: 
        # iteratively calculate V and t for each incremntal step
        V = V + h * func(t0+(h/2), V+(h/2)*func(t0,V)) 
        t0 = t0 + h 
  
    # Printing approximation 
    print("Approximate solution at t = ", t, " is ", "%.6f"% V) 
      
# Driver Code 
# Initial Values 
t0 = 0
V = 14
h = 0.1
t=1

euler( t0, V, h, t )











