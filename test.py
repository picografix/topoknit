from utils import contactNeighbours, TMatrix
import utils
cn = contactNeighbours()
cn.print()
inp = [["K","K","K"],
         ["K","K","K"],
         ["K","K","K"]]


inpInit = [["K","K","K","K"]]       

tm = TMatrix(inpInit)
tm.knitPurlStich(0,0,0)

for i in tm.data:
    for j in i:
        j.print()