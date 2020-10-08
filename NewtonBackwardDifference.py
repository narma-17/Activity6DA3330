#Newton's backward differentiation Algorithm
#calculation of p*p+1*.....p+i required in the formula
def p_cal(p, n): 
    temp = p; 
    for i in range(1, n): 
        temp = temp * (p + i); 
    return temp;

# calculating factorial of given number n 
def fact(n): 
    f = 1; 
    for i in range(2, n + 1): 
        f *= i; 
    return f; 
  
def newton_backward(pred_x,x,y):

    n=len(y)
    #create empty table of size n*n
    table = [[0 for i in range(n)] 
            for j in range(n)];
    #adding input y values to first column
    for i in range(n):
        table[i][0] = y[i]; 

    
    # Calculating the backward differences
    for i in range(1, n): 
        for j in range(n-1,i-1,-1):
            table[j][i] = table[j][i - 1] - table[j-1][i - 1]; 
      
    # Displaying the backward difference 
    import pprint
    print('Backward Differentiation table: ')
    pprint.pprint(table)
    print()

      
    # applying the newton bachward difference formula 
    sum = table[n-1][0]; 
    u = (pred_x - x[n-1]) / (x[n-1] - x[n-2]); 
    for i in range(1,n): 
        sum = sum + (p_cal(u, i) * table[n-1][i]) / fact(i);
    print("\nValue at", pred_x,  
      "is", round(sum, 6))
    return (sum) 


#Driver Code
x = [ 70,80,90,100,110 ]
y=[30,35,47,58,70]
pred_x=95

pred=newton_backward(pred_x,x,y)


























