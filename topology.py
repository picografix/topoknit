from operator import truediv
from utils import contactNeighbours
import copy
from utils import ST
from visualize import addPath
import matplotlib.pyplot as plt

class TopologyGraph():
    def __init__(self,inp) -> None:
        # take the size of inp
        self.n = len(inp)+1
        self.m = 2*len(inp[0])
        self.buffer_nextCN = []
        self.acnList = []
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
                st = self.inp[i][j]

                if(st=="K" or st=="P"):
                    # knit/purl stitch

                    
                    k1 = self.data[i][2*j]
                    k2 = self.data[i][2*j+1]

                    if(k1.av=="UACN"):
                        # CN is UACN

                        # debug here if probelems exist
                        k1.set(st,"UACN",(0,k1.mv[1]))
                        k2.set(st,"UACN",(0,k1.mv[1]))

                        # modify this if needed
                        p1 = self.data[i+1][2*j]
                        p2 = self.data[i+1][2*j+1]

                        p1.set("NULL","PCN",(0,0))
                        p2.set("NULL","PCN",(0,0))
                    elif(k1.av=="E"):
                        # CN is Empty
                        k1.set(st,"E",(0,-1))
                        k2.set(st,"E",(0,-1))
                        
                    else:
                    # PCN
                        if(k1.mv[1]!=0):

                            k1.set(st,"PCN",(0,k1.mv[1]))
                            k2.set(st,"PCN",(0,k1.mv[1]))   
                        else:
                            k1.set(st,"ACN",(0,0))
                            k2.set(st,"ACN",(0,0))


                    

                elif(st=="M"):
                    # miss stitch
                    # need to look for miss stitch
                    k1 = self.data[i][2*j]
                    k2 = self.data[i][2*j+1]
                    if(k1.av=="UACN"):
                        # CN is UACN
                        k1.set("NULL","UACN",(1,k1.mv[1]))
                        k2.set("NULL","UACN",(1,k1.mv[1]))
                    elif(k1.av=="E"):
                        # CN is Empty
                        k1.set("NULL","E",(0,-1))
                        k2.set("NULL","E",(0,-1))
                        x = i
                        temp = self.data[x][2*j]
                        temp2 = self.data[x][2*j+1]
                        while(x>=0):
                            temp = self.data[x][2*j]
                            temp2 = self.data[x][2*j+1]
                            if(temp.mv[0]>0):
                                # print("Breaking")
                                break
                            x = x-1

                        temp.mv = (temp.mv[0]+1,0)
                        temp2.mv = (temp2.mv[0]+1,0)
                        # print(temp2.mv)

                    else:
                    # PCN
                        k1.set("NULL","PCN",(1,k1.mv[1]))  
                        k2.set("NULL","PCN",(1,k1.mv[1]))            
                                   
                    # set all null
                    p1 = self.data[i+1][2*j]
                    p2 = self.data[i+1][2*j+1]
                    p1.set("NULL","E",(0,-1))
                    p2.set("NULL","E",(0,-1))
                elif(st=="Tr"):

                    # need modification
                    k1 = self.data[i][2*j]
                    k2 = self.data[i][2*j+1]

                    if(k1.av=="UACN"):
                        # CN is UACN

                        # debug here if probelems exist
                        k1.set(st,"UACN",(0,k1.mv[1]))
                        k2.set(st,"UACN",(0,k1.mv[1]))

                        # modify this if needed
                        p1 = self.data[i+1][2*j]
                        p2 = self.data[i+1][2*j+1]

                        p1.set("NULL","PCN",(0,0))
                        p2.set("NULL","PCN",(0,0))
                    elif(k1.av=="E"):
                        # CN is Empty
                        k1.set(st,"E",(0,-1))
                        k2.set(st,"E",(0,-1))
                        
                    else:
                    # PCN
                        if(k1.mv[1]!=0):

                            k1.set(st,"PCN",(0,k1.mv[1]))
                            k2.set(st,"PCN",(0,k1.mv[1]))   
                        else:
                            k1.set(st,"ACN",(0,0))
                elif(st=="T"):
                    # tuck stitch
                    k1 = self.data[i][2*j]
                    k2 = self.data[i][2*j+1]

                    if(k1.av=="UACN"):
                        # CN is UACN
                        k1.set("NULL","UACN",(1,k1.mv[1]))
                        k2.set("NULL","UACN",(1,k1.mv[1]))
                    elif(k1.av=="E"):
                        # CN is Empty
                        k1.set("NULL","E",(0,-1))
                        k2.set("NULL","E",(0,-1))
                        x = i
                        temp = self.data[x][j]
                        while(x<self.n):
                            temp = self.data[x][j]
                            if(temp.mv[1]>0):
                                break
                            x = x+1

                        temp.mv = (temp.mv[0],temp.mv[1]+1)
                    else:
                    # PCN
                        k1.set("NULL","PCN",(1,k1.mv[1]))  
                        k2.set("NULL","PCN",(1,k1.mv[1]))           
                    

                    p1 = self.data[i+1][2*j]
                    p2 = self.data[i+1][2*j+1]

                    p1.set("NULL","UACN",(0,0))
                    p2.set("NULL","UACN",(0,0))

    def finalLocationRecursive(self,i,j):
        if(self.data[i][j].st == "K" or self.data[i][j].st == "P" or i==self.n-1):
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
    def addToList(self,i,j,legNode,yarnPath):
        if(legNode):
            if(self.data[i][j].av == "ACN"):
                return True
            else:
                return False
        else:
            av = self.data[i][j].av
            if (av=="E"):
                return False
            elif(av=="UACN"):
                # UACN
                if (i%2!=0 and j%2==0):
                    lastCN = yarnPath[-1]
                    m = lastCN[0]
                    n = lastCN[1]
                else:
                    m,n, currRow, ln = self.nextCN(i,j,legNode,i)
                
                finalI, finalJ = self.finalLocation(i,j)

                if(n<finalJ):
                    self.data[i][j].av = 1
                    return True
                else:
                    return False
            else:
                return True
    
    def nextCN(self,i,j, legNode, currRow):
        # self.buffer_nextCN.append((i,j))
        i_ = i
        j_ = j

        
        
        # if(not legNode and j%2!=0 and currRow%2==0):
        #     i = i-1
        #     legNode=True
        # elif(legNode and j%2==0 and currRow%2==0):
        #     i = i+1
        #     legNode = False
        # elif()
        # elif((not legNode and currRow%2==0 and j%2==0) or (legNode and currRow%2==0 and j%2!=0)):
        #     j = j+1
        # elif((not legNode and currRow%2!=0 and j%2==0) or (legNode and currRow%2!=0 and j%2!=0)):
        #     j = j-1
        




        if(legNode):
            
            if(currRow%2==0):    
                if(j%2==0):
                    i=i+1
                    legNode = False
                else:
                    j = j+1
            else:
                if(j%2==0):
                    j=j-1
                else:
                    i = i+1
                    legNode = False
                
        else:
            if(currRow%2==0):    
                if(j%2!=0):
                    i=i-1
                    legNode = True
                else:
                    j = j+1
            else:
                if(j%2!=0):
                    j=j-1
                else:
                    i = i-1
                    legNode = True

        if(j<0 or j>=self.m):
            return i+1,j_, True, currRow+1
        else:
            return i,j, legNode, currRow
            
        
    def followTheYarn(self):
        i,j,legNode,currentStitchRow = 0,0,True,0
        l = [0,0,0]
        yarnPath = []
        while(i<self.n and j < self.m):

            
            if (self.addToList(i,j,legNode,yarnPath)):
                # print(f"loop i={i} j={j}")
                if(legNode):
                    l = [i,j,currentStitchRow]
                else:
                    i_,j_ = self.finalLocation(i,j)
                    print(f"i= {i} j= {j} i_ {i_} j_ {j_}")
                    l = [i_,j_,currentStitchRow]
                yarnPath.append(l)
            i,j,legNode,currentStitchRow = self.nextCN(i,j,legNode,currentStitchRow)
        

        return yarnPath
    def isBorder(self,i,j,legnode):
        return 1
    def draw(self):
        fig,ax1 = plt.subplots(1, 1)
        yarnList = self.followTheYarn()
        for i in range(len(yarnList)-1):
            cI,cJ,currRow = yarnList[i]
            nI,nJ,nextRow = yarnList[i+1]
            legNode = (cJ==currRow)
            edgeColor = 0
            if(currRow%2!=0):
                edgeColor = "r"
            else:
                edgeColor = "g"
            if(self.isBorder(cI,cJ,legNode)):
                addPath((cJ,cI),(nJ,nI),ax1,edgeColor)
            else:
                addPath((cJ,cI),(nJ,nI),ax1,edgeColor)
        
        plt.show()
        # plt.savefig("trala.png")
