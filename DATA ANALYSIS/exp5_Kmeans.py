#K-means algorithm
#Credits senpai
import random

data=[]
f=open('k_means.txt','r')
for i in f.readlines():
    data.append( i.strip().split(","))
f.close()

kk=int(input("Enter the number of clusters: "))

#initializing the centroids rondomly
centroids=[]
print("1st centroids ",end="")
while(len(centroids)<kk):
    x=random.randint(0,len(data)-1)
    if(data[x] not in centroids): 
        centroids.append(data[x][:])
        print(tuple(data[x]),end=" ")
print()

#calculating the distance between the centroids and the data points using euclidean distance
def distance(x,y):
    dist=0
    for i in range(len(x)):
        dist=dist+(float(x[i])-float(y[i]))**2
    return dist**0.5 

patterns=[["##"]]
pp=[]

def find_clusters(): #finding the clusters
    for i in data:
        dist=[]
        for j in centroids:
            dist.append(distance(i,j))
        pp.append(dist.index(min(dist)))

        tempstr=f"|{str(tuple(i)): ^15}"
        for i in dist:
            tempstr+=f"|{str(round(i,2)): ^6}"
        tempstr+=f"| c{str(1+dist.index(min(dist))): <3}|"  #printing data using format
        print(tempstr)
    print()

while(pp != patterns[-1]): #iterating until the clusters are not changed
    patterns.append(pp)
    pp=[]
    find_clusters()
    #print("current patterns ",pp)
    #calculating new centroids from pp the pattern of the clusters
    strcent=""
    for i in range (kk):
        x,y=0,0
        for j in range(len(pp)):
            if(pp[j]==i):
                x=x+float(data[j][0])
                y=y+float(data[j][1])
        centroids[i][0]=x/pp.count(i)
        centroids[i][1]=y/pp.count(i)
        strcent+="('" + str(round(centroids[i][0],2)) + "', '" + str(round(centroids[i][1],2)) + "') " #rounding of the decimal points
    if(pp != patterns[-1]): print("New centroids",strcent)
        
if random.randint(0, 3)==1:
    for _ in range(100) :
        open("https://youtu.be/xvFZjo5PgG0") # ̿' ̿'\̵͇̿̿\з=(◕_◕)=ε/̵͇̿̿/'̿'̿ ̿

print("\nAll centroid patterns obtained")    
for i in range(2,len(patterns)):
    for j in patterns[i]:
        print("c",j+1," ",end="")
    print()
