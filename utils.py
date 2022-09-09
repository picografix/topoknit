# imports 
import numpy as np


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

AV = {
    0:"PCN",
    1:"ACN",
    2:"UACN",
    3:"E"
}
class contactNeighbours():

    def __init__(self) -> None:

        # define ST = Stitch type, AV = Actualization Value, MV = Movement Vector (del_i,del_j)
        """
        Stich type:
        Knit = 0
        Purl = 1
        Tuck
        """
        self.st = 0
        self.av = 0
        self.del_i = 0
        self.del_j = 0
        self.mv = (self.del_i, self.del_j)
        pass
    
    def print(self):
        print(self.st,self.av, self.del_i,self.del_j, end= "\n")

class TMatrix():
    def __init__(self, inp) -> None:
        # take the size of inp
        self.n = len(inp)
        self.m = len(inp[0])
        # create a array of zeros of size 2M x N+1
        self.data = [[0]*(2*self.m)]*(self.n+1)

        for i in range(2*self.m):
            temp = contactNeighbours()
            self.data[0][i] = temp
        
        # print(self.data)
        
                

    def __associated(self,i,j):
        a = (self.data[2*i][j], self.data[2*i+1][j],self.data[2*i][j+1], self.data[2*i+1][j+1] )
        return a


    def __rowOps(self):
        pass

    def __initialize(self, arr):
        pass

    def readinpRowLeft(self, inp):
        for j in range(len(inp[0])):
            st = ST.get(inp[0][j])
            temp = self.data[0][2*j]
            temp1 = self.data[0][2*j+1]
            temp.st = st
            temp1.st = st

    def initialize(self,arr):
        return self.__initialize(arr)

    def getAssociated(self,i , j):
        self.__associated(i,j)
    def size(self):
        print(len(self.data),len(self.data[0]))
    def print(self):
        for i in range(len(self.data)):
            print("\n")
            for j in range(len(self.data[i])):
                print(self.data[i][j].st, end=" ")