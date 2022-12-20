#FP-Growth Algorithm
#credits senpai ;) gimme a thumbs up if it was helpful 👍
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
min_support = int(input("\nEnter the minimum support ")) 

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
print("\n************************* Sorted data according to priority set *************************\n")
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
    if(lvl == 0):
        print(root.name)
    else:
        print(root.name,root.count)
    for i in root.child:
        traverse(root.child[i],lvl+1)

print("\n***************************   FP Tree   ***************************\n")
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
        if(len(cpb[i][-1]) == 1):
            cpb[i].pop()
    for j in root.child:
        cond_pattern_base(root.child[j],i)

for i in prio:
    cond_pattern_base(start,i)
print("\n*************************  Conditional Pattern Base  *************************\n")
for i in cpb:
    print(i,' -> ',cpb[i])
print()

freq_patterns = [] #list of frequent patterns
def freq_itemsets(root):
    if root == None:
            return
    if root.child == {}:
        traverse = root
        a={}
        while traverse.name != r:
            a[traverse.name] = traverse.count
            traverse = traverse.parent
        freq.append(a)
        return
    for j in root.child:  
        freq_itemsets(root.child[j])

#creating conditional fp tree
for r in cpb:
    root = Node()
    st = root
    root.name = r
    for j in cpb[r]:
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
    print("\n*************************  Conditional FP Tree for ",r,"  *************************\n")
    traverse(st,0)
    #creating frequent itemsets
    freq = []
    freq_itemsets(st)
    print(freq,'\n')
    for i in freq:
        #print(i.keys())
        from itertools import combinations
        for j in range(1,len(i.keys())+1):
            for k in combinations(i.keys(),j):
                count=[]
                for x in k:
                    count.append(i[x])
                    #print(x,i[x])
                #print(k,min(count))
                if min(count) >= min_support:
                    l = list(k)
                    l.append(r)
                    l.append(min(count))
                    freq_patterns.append(l)
                    #print(l)
print("\n*************************  Frequent Patterns  *************************\n")
#print(freq_patterns)

#merging duplicate patterns
for i in range(0,len(freq_patterns)):
    for j in range(i+1,len(freq_patterns)):
        if(freq_patterns[i][0:-1] == freq_patterns[j][0:-1]):
            freq_patterns[i][-1] += freq_patterns[j][-1]
            freq_patterns[j] = []
freq_patterns = [i for i in freq_patterns if i != []]

#sorting patterns according to length
freq_patterns.sort(key = len)

for i in freq_patterns:#printing frequent patterns
    print(i)
