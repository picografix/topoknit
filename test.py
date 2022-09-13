from utils import contactNeighbours, TMatrix
import utils
cn = contactNeighbours()
# cn.print()
inp = [["K","K","K"],
         ["K","K","K"],
         ["K","K","K"]]


inpInit = [["K","K","P","K"],["K","K","K","K"]]       

tm = TMatrix(inpInit)
tm.stitchNew()
# tm.knitPurlStich(0,0,0)
# tm.knitPurlStich(1,0,0)
tm.print()
# tm.printDetail()
# tm.data[0][1].show()