# Python3 code to implement Trapezoidal rule 
  
# A sample function whose definite  
# integral's approximate value is  
# computed using Trapezoidal rule 

#if function not given
def trapezoidal_l(x,y):
    h=x[1]-x[0]#computing interval size
    s=0
    for i in range(len(y)-1):#calculating area of each trapezoid of height h
        s+=h/2*(y[i]+y[i+1])
    print (s)
    return s

#Driver Code
pt=[3.1,4.4,6.4,6.6,5.9,5.6,5.1,4.9,4.6]
t=[1,2,3,4,5,6,7,8,9]
integral=trapezoidal_l(t,pt)



#if function is given
def y( x ): 
      
    # Declaring the function  
    # f(x) = 1/(1+x*x) 
    return (1 / (1 + x * x)) 
      
# Function to evalute the value of integral 
def trapezoidal (a, b, n): 
      
    # Grid spacing 
    h = (b - a) / n 
      
    # Computing sum of first and last terms 
    # in above formula 
    s = (y(a) + y(b)) 
  
    # Adding middle terms in above formula 
    i = 1
    while i < n: 
        s += 2 * y(a + i * h) 
        i += 1
          
    # h/2 indicates (b-a)/2n.  
    # Multiplying h/2 with s. 
    return ((h / 2) * s) 
