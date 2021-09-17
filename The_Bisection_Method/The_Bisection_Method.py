def F(x):
    return pow(x,3)-x-1;

a=1;
b=2;
E=1e-2;
x=(a+b)/2
k=0

while abs(F(x))>E:
    if ((F(a)*F(x))<0):
        b=x
    else:
        a=x
  
    k+=1
    x=(a+b)/2
    
    

print ("x = ", x)
print ("step is equal ", k)


    