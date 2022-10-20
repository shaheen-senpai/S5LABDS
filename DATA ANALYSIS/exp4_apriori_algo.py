#Apriori Algorithm

def union(lst1, lst2):    #list join operation
    final_list = list(set(lst1) | set(lst2))
    final_list.sort()     #lexiographical order
    return final_list

f=open("apriori.txt","r")
data={}
items=[]
min_support=0
ii=0

for i in f.readlines():
    print(i)
    l=i.strip().split()
    data[l[0]]=l[1::1]
    ii+=1   #size of dictionary containing transactions
keys=list(data.keys())  #transaction Id's

for i in range(1,ii): items = union(items,data[keys[i]]) #ii = 9
min_support = int(input("Enter the minimum support "))

c = {}
for x in items:
    count=0
    for i in range(1,ii):
        if(x in data[keys[i]] ):
            count+=1
    c[x]=count

while(len(c)>0):

    for i in c:
        if(c[i] < min_support): c.pop(i)  #pruned
    
    break

        
print(data)
print(items)
print(c)


