n=int(input("Enter the number of tuples of numerical"))
r1=int(input("Enter the number of tuples of data set of nominal attrribute(rows) "))
c1=int(input("Enter the number of attribute of data set of nominal attrribute(columns) "))
defchisqr=int(input("Enter the value of default chi square"))
a=[[] for _ in range(n)];
b=[]
meana,meanb,r,suma,sumb=0,0,0,0,0
print("Enter the numerical")
for i in range(n):
	a[i]=list(map(int,input().split()))
	meana+=a[i][0]
	meanb+=a[i][1]
meana/=n;meanb/=n;
for i in range(n):
	suma+=(a[i][0]-meana)**2
	sumb+=(a[i][1]-meanb)**2
	r+=(a[i][0]-meana)*(a[i][1]-meanb)
suma=(suma/n)**0.5
sumb=(sumb/n)**0.5
print("Correlation:",r/(n*suma*sumb))
print("EnTer the nominal")
for i in range(r1):
    b.append(list(map(int,input().split())))
totalsum=0
chisqr=0
column=[0 for _ in range(c1)]
row=[0 for _ in range(r1)]
for j,i in enumerate(b):
    totalsum+=sum(i)
    row[j]=sum(i)
for i in range(c1):
    for j in range(r1):
        column[i]+=b[j][i]
for i in range(r1):
    for j in range(c1):
        chisqr+=((b[i][j]-((row[i]*column[j])/totalsum))**2)/((row[i]*column[j])/totalsum)
print("Chi Square:",chisqr)
if chisqr<=defchisqr:
    print("Independent")
else:
    print("Dependent")
