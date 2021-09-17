def F(x):
    return pow(x,3)-x-1;

def X(a,b):
    return (a+b)/2

a=1;
b=2;
E=1e-2;
x=X(a,b)
k=0

while abs(F(x))>E:
    if ((F(a)*F(x))<0):
        b=x
    else:
        a=x
  
    k+=1
    x=X(a,b)

    
    
    

print ("x = ", x)
print ("step is equal ", k)


    