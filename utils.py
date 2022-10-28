# imports 
from contextlib import nullcontext
import numpy as np
import copy


# class Matrix
#  M x N inp will output 2M x (N+1) matrix

ST = {
    "K":0,
    "P":1,
    "M":2,
    "T":3,
    "E":4,
    "Tu":5,
    "NULL":6
}
ST_K = {
    0:"K",
    1:"P",
    2:"M",
    3:"T",
    4:"E",
    5:"Tu",
    6:"NULL"
}
AV = {
    0:"PCN",
    1:"ACN",
    2:"UACN",
    3:"E"
}
class contactNeighbours():

    def __init__(self,x,y) :

        # define ST = Stitch type, AV = Actualization Value, MV = Movement Vector (del_i,del_j)
        """
        Stich type:
        Knit = 0
        Purl = 1
        Tuck
        """
        self.x = x
        self.y = y
        self.st = 6
        self.av = 0
        self.del_i = 0
        self.del_j = 0
        self.mv = (self.del_i, self.del_j)
        self.next = -1
        self.back = -1
        self.prev = -1
        self.front = -1


    def getST(self):
        return ST_K.get(self.st)
      
    def getXY(self):
        return self.x, self.y
    def getXYRevert(self):
        return self.y, self.x

    def show(self):
        print(f"CN: ST = {self.getST()}, AV = {AV.get(self.av)}, MV = {self.del_i,self.del_j} \n")

class TMatrix():
    def __init__(self, inp) -> None:
        # take the size of inp
        self.n = len(inp)+1
        self.m = 2*len(inp[0])
        # create a array of zeros of size 2M x N+1
        # self.data = [[0]*(2*self.m)]*(self.n+1)
        self.data = [[0 for i in range(self.m)] for j in range(self.n)]
        self.inp = inp
        for j in range(self.n):
            for i in range(self.m):
                temp = contactNeighbours(j,i)
                self.data[j][i] = copy.copy(temp)

        
                

    def __associated(self,i,j):
        a = (self.data[2*i][j], self.data[2*i+1][j],self.data[2*i][j+1], self.data[2*i+1][j+1] )
        return a


    def __rowOps(self):
        pass

    def __initialize(self, arr):
        pass

    def readinpRowLeft(self, inp):
        i=0
        st = ST.get(inp[0][1])
        # print(self.data[1][1])
        # print(self.data[0][1])
        
        # temp = self.data[1][1]

        # temp.st = st
        for j in range(len(inp[0])):
            # print(f"Mod {i,j}")
            st = ST.get(inp[0][j])
            temp = self.data[i][2*j]
            # temp1 = self.data[i][2*j+1]
            self.data[i][2*j+1].st = st
            temp.st = st
            # temp1.st = st

    def initialize(self,arr):
        return self.__initialize(arr)

    def getAssociated(self,i , j):
        self.__associated(i,j)
    def size(self):
        print(len(self.data),len(self.data[0]))


    def loopRight(self,p1,p2,p3,p4):
        p1.next = p2
        p2.back = p1
        p2.next = p3
        p3.back = p2
        p3.next = p4
        p4.back = p3
        return p1,p2,p3,p4
    
    def loopLeft(self,p1,p2,p3,p4):
        p1.prev = p2
        p2.front = p1 # double pointer
        p2.prev = p3
        p3.front = p2
        p3.prev = p4
        p4.front = p3
        return p1,p2,p3,p4
    
    def knitPurlRight(self,i,j,st, last):

        """
          p2 -> p3
          |     |
        ->p1    p4
        
        """

        p1 = self.data[i][j]
        p1.st = st
        p1.av = 1
        p2 = self.data[i+1][j]
        p2.av = 0
        p3 = self.data[i+1][j+1]
        p3.av = 0
        p4 = self.data[i][j+1]
        p4.st = st
        p4.av = 1
        if(last.next==-1):
            last.next = p1
            p1.back = last
        # last.prev = p1
        p1.next = p2
        p2.back = p1
        p2.next = p3
        p3.back = p2
        p3.next = p4
        p4.back = p3
        return p4
    
    def knitPurlLeft(self,i,j,st, last):

        """
          p3 <- p2
          |     |
      <- p4    p1<-
        
        """

        p1 = self.data[i][j]
        p1.st = st
        p1.av = 1
        p2 = self.data[i+1][j]
        p2.av = 0
        p3 = self.data[i+1][j-1]
        p3.av = 0
        p4 = self.data[i][j-1]
        p4.st = st
        p4.av = 1
        if(last.prev==-1):
            last.prev = p1
            p1.front = last
        # last.next = p1
        p1.prev = p2
        p2.front = p1 # double pointer
        p2.prev = p3
        p3.front = p2
        p3.prev = p4
        p4.front = p3
        return p4
        
        # this wont happen like this
        #  you need to use av param to solve this

    def missLeft(self,i,j,st,last):
        ii = i
        pp1 = self.data[ii][j]
        pp2 = self.data[ii][j-1]

        while(self.data[ii][j].av!=0):
            ii = ii-1
            pp1 = self.data[ii][j]
            pp2 = self.data[ii][j-1]

        a = 0
        if(pp1.prev == pp2):
            a=0
            pp1.prev = -1
            pp2.prev = -1
        elif(pp2.next == pp1):
            a=1
            pp2.next = -1
            pp1.next=-1
        pp1 = self.data[ii-1][j]
        pp2 = self.data[ii-1][j-1]
        # print("Debug = ",ii, pp1.getXY())
        p1 = self.data[i][j]
        p1.st = st
        p1.av = -1
        p2 = self.data[i+1][j]
        p2.av = 1
        p3 = self.data[i+1][j-1]
        p3.av = 1
        p4 = self.data[i][j-1]
        p4.st = st
        p4.av = -1
        

        
        
        # check back and front
        #  remove p1 and p4 connection
        
        if(a==0):
            pp1,p2,p3,pp2 = self.loopLeft(pp1,p2,p3,pp2)

        elif(a==1):
            # print("Debug")
            pp2,p3,p2,pp1 = self.loopRight(pp2,p3,p2,pp1)

        return last 
    def missRight(self,i,j,st, last):
        p1 = self.data[i][j]
        p1.st = st
        p1.av = 0
        p2 = self.data[i+1][j]
        p2.av = 1
        p3 = self.data[i+1][j+1]
        p3.av = 1
        p4 = self.data[i][j+1]
        p4.st = st
        p4.av = 0
        ii = i-1
        pp1 = self.data[ii][j]
        pp2 = self.data[ii][j+1]
        while(self.data[ii][j].av==0):
            ii = ii-1
            pp1 = self.data[ii][j]
            pp2 = self.data[ii][j+1]

        # check back and front
        if(pp1.next == pp2):
            pp1,p2,p3,pp2 = self.loopRight(pp1,p2,p3,pp2)

        elif(pp2.prev == pp1):
            pp2,p3,p2,pp1 = self.loopLeft(pp2,p3,p2,pp1)

        return last 

    def tuck(self,i,j,last):
        """
          p2 -> p3
          |     |
        ->p1    p4->
        
        """
        # st= 3
        p1 = self.data[i][j]
        # p1.st = st
        p1.av = 0
        p1.mv[1] += 1
        p2 = self.data[i+1][j]
        p2.av = 2
        p3 = self.data[i+1][j+1]
        p3.av = 2
        p4 = self.data[i][j+1]
        # p4.st = st
        p4.av = 0
        p4.mv[1] += 1
        last.next = p2
        # p1.next = p2
        p2.next = p3
        # p3.next = p4
        last = p3
        
    def stitchNew(self):
        last = contactNeighbours(-1,-1)
        for i in range(len(self.inp)):

            if(i%2==0):
                # if(i!=0):
                #     last.next = self.data[i][j]
                
                for j in range(len(self.inp[i])):
                    st = ST.get(self.inp[i][j])
                    print(st)
                    if(st==0):
                        last = self.knitPurlRight(i,2*j,st,last)
                    elif(st==2):
                        last = self.missRight(i,2*j,st,last)
            else:
                # last.prev = self.data[i][2*j-1]
                for j in reversed(range(1,len(self.inp[i])+1)):
                    st = ST.get(self.inp[i][j-1])
                    if(st==0):

                        last = self.knitPurlLeft(i,2*j-1,st,last)
                    elif(st==2):
                        last = self.missLeft(i,2*j-1,st,last)

                    # print(last.getXY())
                    # print("hi")
                


    def stitch(self,low, mode, stichType):
        # low is lower row in which stich needs to be done
        # mode is left or right
        # self.data is top to bottom array (we are using inverse matrix than research paper)
        st = stichType
        # low represents the row number
        last= 0
        if(mode==0):
            # left
            for i in range(self.m):
                # modifying j row
                t1 = self.data[low][i]
                # t2 = self.data[low][i]
                t1.st = st
                t1.av = 1
                t1.next = last
                last = t1

                # modifying j+1 row

                t1 = self.data[low+1][i]
                t1.st = 6 #Null value
                t1.av = 0 #PCN
        elif(mode==1):
            # right
            for i in reversed(range(self.m)):
                t1 = self.data[low][i]
                # t2 = self.data[low][i]
                t1.st = st
                t1.av = 1
                t1.next = last
                last = t1

            # modifying j+1 row
                t1 = self.data[low+1][i]
                t1.st = 6 #Null value
                t1.av = 0 #PCN
        else:
            print("Mode can only be left or right")


    # def kpStich(self,cn1):

    def print_row(self,i):
        for j in range(len(self.data[i])):
            print(ST_K.get(self.data[i][j].st), end=" ")
    def print(self):
        for i in self.data:
            for j in range(len(i)):
                # print(i[j])
                print(ST_K.get(i[j].st),i[j].getXY(), end=";")
        
            print("\n")


    def printDetail(self):
        for i in self.data:
            for j in i:
                j.show()
