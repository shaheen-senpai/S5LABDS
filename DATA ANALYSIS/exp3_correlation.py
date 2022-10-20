#credits senpai
#correlation b/w nominal
#Chi-square
nominal = input("Enter the nominal values\n").strip().split()
attributes = input("Enter the attributes in the contingency table\n").strip().split()
r,c = len(nominal),len(attributes)
dof =(r-1)*(c-1) #degree of freedom
chi = 0
l=[] #data

for i in range (r):
	a=[]
	for j in range (c):
		print("enter freq of ",nominal[i],attributes[j]) #inputing data
		a.append(int(input()))
	l.append(a)
	
total_nominal = [ sum(x) for x in l ]
total_attributes = []
for i in range(c):
	s=0
	for j in range(r):
		s+=l[j][i]
	total_attributes.append(s)
		
print("contingency table\n","\t",end=" ")
for i in range(c): print(attributes[i],end="  ")
print("total")
for i in range(r):
	print(nominal[i],end="\t")
	for j in range(c):                  #printing contingency table
		print(l[i][j],end="  ")
	print(total_nominal[i])
print("total",end="    ")
for i in total_attributes: print(i,end="  ")
print(sum(total_nominal))

for i in range(c):           #chi-square calculation
	for j in range(r):
		ex = (total_attributes[i]*total_nominal[j])/sum(total_nominal)
		#print(total_attributes[i],total_nominal[j],sum(total_nominal))
		#print(l[j][i],"data")
		chi +=( (l[j][i]-ex)**2 )/ ex

print("calculated value of chi-square = ",chi)
print("degree of freedom = ",dof)
x=int(input("enter table value"))
if(chi>x):print("dependent")
else:print("independent")
##############################################################################################
#correlation b/w numeric
#correlation coeifficient

a=[] #1st Attribute
b=[] #2nd Attribute
for i in (input("enter values of attribute A ").strip().split()):
    a.append(float(i))
for i in (input("enter values of attribute b ").strip().split()):
    b.append(float(i))
if(len(a)!=len(b)): 
    print("no of samples miss-match")
    exit(0)
mean_A = float(sum(a)/len(a))
mean_B = float(sum(b)/len(b))
asum,bsum,num,denom=0,0,0,0

#calculating correlation coefficient R
for i in range(len(a)):
    asum += a[i]-mean_A
    bsum += b[i]-mean_B
    denom += float(float( float( asum**2) * float(bsum**2) )**0.5)
    num += float((asum)*(bsum))
print("R = ",float(num/denom))
