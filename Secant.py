# Python3 Program to find root of an  
# equations using secant method  
  
# function takes value of x  
# and returns f(x)  
def f(x):   
    # profit function 
    f = 3*pow(x, 2) -9* x - 6;  
    return f;  
  
def secant(x1, x2, E): 
    #xm=desired value of the function:0 when x=root of the function
    #n=iteration
    n = 0; x0 = 0; c = 0;
    #checking the applicability of intermediate value theorum tp find the root
    if (f(x1) * f(x2) < 0): 
        while True:     
            # Value at which secant line intersects 0  
            x0 = x1-((f(x1)*(x1-x2))/ (f(x1)-f(x2)))

            # check if x0 is root of  equation 
            c = f(x1) * f(x0);  

           
            # update the value of interval
            x1 = x2;  
            x2 = x0; 
            
              
            #if the difference beween the values of the function in two consecutive 
            #iterations is less that the tolerance then terminate                           
            if(abs(x2 - x1) < E): 
                break;
            
            #if the value of the function is less than the tolerance level then terminate
            if (abs(x2) < E):
                break

                
              
            # if x0 is the root of equation  
            # then break the loop  
            if (c == 0):  
                break; 
  
            # update number of iterations  
            n += 1;  
 
            #maximum iterations    
            if n>500:
                break
          
        print("Root of the given equation =",  
                               round(x0, 6));  
        print("No. of iterations = ", n);  
          
    else: 
        print("Can not find a root in ", 
                   "the given inteval");  
  
# Driver code  
  
# initializing the values  
x1 = 0
x2 = 4 
E = 10e-5 
secant(x1, x2, E); 
