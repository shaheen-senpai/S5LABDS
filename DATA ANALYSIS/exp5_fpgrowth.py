#FP-Growth Algorithm

def union(lst1, lst2):    #list join operation
    final_list = list(set(lst1) | set(lst2))
    final_list.sort()     #lexiographical order
    return final_list

def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

f=open("fpgrowth.txt","r")
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

#creating L1 and priority set for fp growth tree 
c = []
for x in items:
    count=0
    for i in range(1,ii):
        if(x in data[keys[i]] ):
            count+=1
    c.append([x,count])

c.sort(key=lambda x:x[1],reverse=True) #sorting L1 to create the priority set
prio=[i[0] for i in c]
#print(c,prio)

for i in range(1,ii):
    data[keys[i]].sort(key=lambda x:prio.index(x)) #sorts data according to prio
for i in data: print(i,data[i])

#creating fp tree class
class Node:
    def __init__(self):
        self.child = {}
        self.count = 0
        self.parent = None
        self.name = None
        self.link = None

root = Node()
start = root
root.name = 'root'

for i in range(1,ii): #inserting data into fp tree
    current = root
    for j in data[keys[i]]:
        if j in current.child:
            current = current.child[j]
            current.count += 1
            current.parent = root
            root = current         
        else:
            current.child[j] = Node()
            current = current.child[j]
            current.name = j
            current.count += 1
            current.parent = root
            root = current
    root = start

#traversing fp tree
def traverse(root,lvl):
    if root == None:
        return
    for i in range(0,lvl):
        print("\t",end="")
    print(root.name,root.count)
    for i in root.child:
        traverse(root.child[i],lvl+1)

traverse(start,0)

#creating conditional pattern base
cpb = {}
def cond_pattern_base(root,i):
    if root == None:
        return
    if root.name == i:
        if i in cpb:
            cpb[i].append([])
        else:
            cpb[i]=[[]]
        cpb[i][-1].append(root.count)
        traverse=root
        while traverse.parent.name != 'root':
            cpb[i][-1].append(traverse.parent.name)
            traverse = traverse.parent
    for j in root.child:
        cond_pattern_base(root.child[j],i)

for i in prio:
    cond_pattern_base(start,i)

for i in cpb:
    print(i,cpb[i])
    
#creating conditional fp tree
for i in cpb:
    root = Node()
    st = root
    root.name = i
    for j in cpb[i]:
        current = root
        for k in j[1::1]:
            if k in current.child:
                current = current.child[k]
                current.count += j[0]
                current.parent = root
                root = current
            else:
                current.child[k] = Node()
                current = current.child[k]
                current.name = k
                current.count += j[0]
                current.parent = root
                root = current
        root = st
    traverse(root,0)
    
    

            
            
        
