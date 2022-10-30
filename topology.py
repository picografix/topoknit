from utils import contactNeighbours
import copy
from utils import ST

class TopologyGraph():
    def __init__(self,inp) -> None:
        # take the size of inp
        self.n = len(inp)+1
        self.m = 2*len(inp[0])
        self.buffer_nextCN = []
        # create a array of zeros of size 2M x N+1
        # self.data = [[0]*(2*self.m)]*(self.n+1)
        self.data = [[0 for i in range(self.m)] for j in range(self.n)]
        self.inp = inp
        for j in range(self.n):
            for i in range(self.m):
                temp = contactNeighbours(j,i)
                self.data[j][i] = copy.copy(temp)
    

    def stitch(self):
        for i in range(len(self.inp)):
            for j in range(len(self.inp[i])):
                st = ST.get(self.inp[i][j])

                if(st==0 or st==1):
                    # knit/purl stitch

                    
                    k1 = self.data[i][2*j]
                    k2 = self.data[i][2*j+1]

                    k1.st = st
                    k2.st = st

                    k1.av = 1
                    k2.av = 1                    

                    k1.mv = (0,0)
                    k2.mv = (0,0)

                elif(st==2):
                    # miss stitch
                    # need to look for miss stitch
                    k1 = self.data[i][2*j]
                    k2 = self.data[i][2*j+1]

                    k1.st = 6
                    k2.st = 6

                    k1.av = 1
                    k2.av = 1                    

                    k1.mv = (0,2)
                    k2.mv = (0,2)

                elif(st==3):
                    # transfer stitch
                    pass
                elif(st==5):
                    # tuck stitch
                    k1 = self.data[i][2*j]
                    k2 = self.data[i][2*j+1]

                    k1.st = st
                    k2.st = st

                    k1.av = 0
                    k2.av = 0                    

                    k1.mv = (0,1)
                    k2.mv = (0,1)
    
    def finalLocationRecursive(self,i,j):
        if(self.data[i][j].st == 1 or self.data[i][j].st == 0):
            return i,j
        else:
            return self.finalLocationRecursive(i+self.data[i][j].mv[0],j)

    def finalLocation(self,i,j):
        if(i==self.n-1):
            return i,j
        elif(self.data[i][j].mv[1]!=0):
            return self.finalLocationRecursive(i,j+self.data[i][j].mv[1])
        else:
            return self.finalLocationRecursive(i+self.data[i][j].mv[0],j)


    def isACN(self,i,j):
        if(self.data[i][j].av !=0):
            return True
        else:
            return False
    def addToList(self,i,j,legNode,yarnPath,DS):
        if(legNode):
            if(self.isACN(i,j)):
                return True
            else:
                return False
        else:
            av = self.data[i][j].av
            if (av==0):
                return False
            elif(av==2):
                # UACN
                if (i%2!=0 and j%2==0):
                    m,n = self.buffer_nextCN[-2]
                else:
                    m,n = self.nextCN(i,j,legNode,i)
                
                finalI, finalJ = self.finalLocation(i,j)

                if(m<finalI):
                    self.data[i][j].av = 1
                    return True
                else:
                    return False
            else:
                return True
    
    def nextCN(self,i,j, legNode, currRow):
        self.buffer_nextCN.append(i,j)
        i_ = i
        j_ = j
        ln = True
        if(legNode):
            ln = False
            if(j%2==0):
                i = i+1

            else:
                if(currRow%2==0):

                    j = j+1
                else:
                    j = j-1
                
        else:
            if(j%2==0):
                if(currRow%2==0):
                    j = j+1
                
                else:
                    j = j-1
            else:
                ln = True
                i = i-1
        
        if(j<0 or j>self.m):
            return i+1,j_, currRow+1, True
        else:
            return i,j, currRow, ln
            
        
    def followTheYarn(self):
        i,j,legNode,currentStitchRow = 0,0,True,0
        yarnPath = []
        while(i<self.n and j < self.m):
            if (self.addToList()):
                pass
