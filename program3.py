n=int(input("Enter Number: "));
t=2*n;
a=[];
j=t-1
if(n%2==0):
    for i in range(1,j,2):
        a.append(i);
else:
    for i in range(1,t,2):
        a.append(i);
print(a);