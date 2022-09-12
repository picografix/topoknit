# imports 
from asyncio.windows_events import NULL
import numpy as np


# class Matrix
# 
#  M x N input will output 2M x (N+1) matrix

ST = {
    0:"Knit",
    1:"Purl",
    2:"Tuck",
    3:"Miss",
    4:"Transfer",
    5:"Empty"
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
        self.i = 0
        self.j = 0
        self.st = NULL
        self.av = 3
        self.del_i = NULL
        self.del_j = NULL
        self.mv = (self.del_i, self.del_j)
        pass

        
    def print(self):
        print(f"CN at {self.i},{self.j} \n Stitch Type = {ST.get(self.st)} \n AV = {AV.get(self.av)} \n MV = {AV.get(self.mv)}")

class TMatrix():
    def __init__(self, input) -> None:
        # take the size of input
        self.m = len(input)
        self.n = len(input[0])
        # create a array of zeros of size 2M x N+1
        self.data = [[0]*(2*self.m)]*(self.n+1)

    def __associated(self,i,j):
        a = (self.data[2*i][j], self.data[2*i+1][j],self.data[2*i][j+1], self.data[2*i+1][j+1] )
        return a


    def __rowOps(self):
        pass

    def __initialize(self, arr):
        pass

    def initialize(self,arr):
        return self.__initialize(arr)

    def getAssociated(self,i , j):
        self.__associated(i,j)