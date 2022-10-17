#credits senpai
f=open("data.txt","r")
data={}
ii,p=0,0

for i in f.readlines():
    print(i)
    l=i.strip().split()
    data[ii]=l
    ii+=1
#n denotes nominal attribute
#o denotes numeric attribute
s=len(data[1])
d_mat1 = [[-1 for _ in range(ii-1)] for _ in range(ii-1)] #nominal dissimilarity matrix
d_mat2 = [[0 for _ in range(ii-1)] for _ in range(ii-1)]  #numeric dissimilarity matrix

m,ind = 0,0
for i in range (1,ii):
    for j in range (i+1,ii):
        while(ind<s):
            if(data[0][ind]=='n'):
                p+=1
            if(data[i][ind]==data[j][ind] and data[0][ind]=='n'):     #simple matching
                m+=1
            if(data[0][ind]=='o'):
                if(data[i][ind]!=data[j][ind]):                     #euclidean distance
                    d_mat2[j-1][i-1]+=(float(data[i][ind])-float(data[j][ind]))**2    
            ind+=1
        d_mat2[j-1][i-1]**=0.5
        d_mat1[j-1][i-1]=(p-m)/p
        m,ind,p=0,0,0
        
print("dissimilarity matrix of nominal attributes")
for i in range (ii-1):
    for j in range (ii-1):
        if(d_mat1[i][j] != -1): print(d_mat1[i][j],end=" ")
        elif(i==j): print("0",end=" ")
        else: print(" ",end=" ")
    print()

print("dissimilarity matrix of numeric attributes")
for i in range (ii-1):
    for j in range (ii-1):
        if(d_mat2[i][j] != 0): print(round(d_mat2[i][j],2),end=" ")
        elif(i==j): print("0",end=" ")
        else: print(" ",end=" ")
    print()

choice = int(input("press 1 to print simmilarity or 0 to EXIT\n"))
while(choice):
    type = input("enter numeric or nominal \n")
    if(type=='nominal'):
        i=int(input("enter ith object "))
        j=int(input("enter jth object "))
        if(d_mat1[i-1][j-1]==-1):
            print(1-d_mat1[j-1][i-1])
        else:
            print(1-d_mat1[i-1][j-1])

    if(type=='numeric'):
        i=int(input("enter ith object "))
        j=int(input("enter jth object "))
        if(d_mat2[i-1][j-1]==0):
            print(1-d_mat2[j-1][i-1])
        else:
            print(1-d_mat2[i-1][j-1])
    choice = int(input("press 1 to print simmilarity or 0 to EXIT\n"))

    
#sample text file:
#data.txt
#n n    o  o
#1 joel 10 20
#2 joe  15 20
#1 joel 16 30

