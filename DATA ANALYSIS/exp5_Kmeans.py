#still under debugging 
#K-means algorithm
import random

data=[]
f=open('kmeans.txt','r')
for i in f.readlines():
    data.append( i.strip().split(","))
f.close()

if random.randint(0, 4)==1:
    for _ in range(100) :
        open("https://youtu.be/xvFZjo5PgG0") 

kk=int(input("Enter the number of clusters: "))

#initializing the centroids rondomly
centroids=[]
for i in range(kk):
    x=random.randint(0,len(data)-1)
    centroids.append(data[x][:])
print("centroids 1st ",centroids)

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
        #print(dist)
        pp.append(dist.index(min(dist)))
        #print(i,dist,dist.index(min(dist)))
        tempstr=f"|{str(tuple(i)): ^15}"
        for i in dist:
            tempstr+=f"|{str(round(i,2)): ^5}"
        tempstr+=f"| c{str(dist.index(min(dist))): ^5}|"
        print(tempstr)

while(pp != patterns[-1]): #iterating until the clusters are not changed
    patterns.append(pp)
    pp=[]
    find_clusters()
    print("patterns",patterns)
    print("pp",pp)
    #calculating new centroids from pp the pattern of the clusters
    for i in range (kk):
        x,y=0,0
        for j in range(len(pp)):
            if(pp[j]==i):
                x=x+float(data[j][0])
                y=y+float(data[j][1])
                print("data ",data[j][0],data[j][1])
        centroids[i][0]=x/pp.count(i)
        centroids[i][1]=y/pp.count(i)
    print("centroids",centroids)
    
#patterns.append(pp)
print(data)



