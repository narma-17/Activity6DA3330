#Newton's backward differentiation Algorithm

#calculation of value-x[i] required in the formula
def x_cal(pred_x, x,i): 
    temp = 1; 
    for j in range(i): 
        temp = temp * (pred_x-x[j]); 
    return temp;

#Function to compute approximation
def newton_divided(pred_x,x,y):

    n=len(y)
    #create empty table of size n*n
    table = [[0 for i in range(n)] 
            for j in range(n)];
    #adding input y values to first column
    for i in range(n):
        table[i][0] = y[i]; 

    
    # Calculating the divided differences
    for i in range(1, n): 
        for j in range(n-i):
            table[j][i] = (table[j+1][i - 1] - table[j][i - 1])/(x[j+i]-x[j]); 
      
    # Displaying the divided difference table 
    import pprint
    table_print = [[0 for i in range(n)] 
            for j in range(n)];
    for i in range(n): 
        for j in range(n):
            table_print[j][i]=round(table[j][i],5)
    print('Divided Differentiation table: ')
    pprint.pprint(table_print)
    print()

      
    # applying the newton's divided difference formula 
    sum = table[0][0];  
    for i in range(1,n): 
        sum = sum + (x_cal(pred_x,x,i) * table[0][i]);
    print("\nValue at", pred_x,  
      "is", round(sum, 6))
    return (sum) 


#Driver Code
x = [ 70,80,90,100,+110 ]
y=[30,35,47,58,70]
pred_x=95
    


pred=newton_divided(pred_x,x,y)
