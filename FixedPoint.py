
def g(x):
    #function to return g(x) for a given x
    return ((3*x+2)**0.5)

def fixedp(g,x0,tol=1e-5,maxiter=100):
     """ Fixed point algorithm """
     #initialize error, iteration number
     e = 1
     itr = 0
    
    # While the value of g(x)-x< tolerance and iterations < maximum continue
     while(e > tol and itr < maxiter):
         #caluclate x iteratively using fixed point equation
          x = g(x0)      
          e = abs(x0-x) # error at the current step
          x0 = x #update x0 
          itr = itr + 1 #update iteration number
          #print results
          print('interation=',itr)
          print('x=',x0)
          print('g(x)=',g(x0))
          print('error=',e)
          print()
     return x
#call function
fixedp(g,0,tol=1e-5,maxiter=100)
