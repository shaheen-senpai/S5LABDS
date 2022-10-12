
class Data:
    def __init__(self,file):
        self.file=open(file,'r')
        self.table=[ x[:-1].split() for x in self.file.readlines()]
        self.rowcount=len(self.table)

    def __str__(self):
        string=""
        for i in self.table:
            string+=" ".join(i)+'\n'
        return string

    def view(self,matrix):
        for i in matrix:print(i)

    def nominaldiff(self,r1,r2,npos):
        p=len(npos)
        q=0
        for i in npos:
            if r1[i]==r2[i]:q+=1
            
        return (p-q)/p

    def numericaldiff(self,r1,r2,npos):#euclidean distance
        dist=0
        for i in npos:
            dist+=(int(r1[i])-int(r2[i]))**2
        return round(dist**0.5,2)

    def prox(self,npos,type):
        matrix=[]
        for i in range(self.rowcount):matrix.append([0]*self.rowcount)

        for i in range(self.rowcount):
            for j in range(i+1,self.rowcount):
                if type=="nominal":
                    matrix[i][j]=matrix[j][i]=\
                        self.nominaldiff(self.table[i],self.table[j],npos)
                elif type=="numerical":
                    matrix[i][j]=matrix[j][i]=\
                        self.numericaldiff(self.table[i],self.table[j],npos)
        self.view(matrix)
        return matrix



obj=Data('exp2.txt')
print(obj)
print("Nominal Dissimilarity Matrix")
obj.prox([0,1],'nominal')
print("Numerical Dissimilarity Matrix")
obj.prox([2,3],'numerical')