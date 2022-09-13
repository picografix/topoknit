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

    def __init__(self) :

        # define ST = Stitch type, AV = Actualization Value, MV = Movement Vector (del_i,del_j)
        """
        Stich type:
        Knit = 0
        Purl = 1
        Tuck
        """
        self.st = 6
        self.av = 0
        self.del_i = 0
        self.del_j = 0
        self.mv = (self.del_i, self.del_j)
        self.next = 0


    def getST(self):
        return ST_K.get(self.st)
      
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
                temp = contactNeighbours()
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


    def knitPurl(self,i,j,st, last):

        """
          p2 -> p3
          |     |
        ->p1    p4->
        
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
        last.next = p1
        p1.next = p2
        p2.next = p3
        p3.next = p4
        last = p4


        
    def stitchNew(self):
        last = contactNeighbours()
        for i in range(len(self.inp)):
            for j in range(len(self.inp[i])):
                st = ST.get(self.inp[i][j])
                self.knitPurl(i,2*j,st,last)



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
                print(ST_K.get(i[j].st), end=";")
        
            print("\n")


    def printDetail(self):
        for i in self.data:
            for j in i:
                j.show()
