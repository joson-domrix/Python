#fiboEven

j=1
k=1
totals=0

while(j<=4000000):
    if((j%2)==0):
        totals=totals+j
 
    j,k=k,j+k
print (totals)
