from utils import contactNeighbours, TMatrix
import utils
cn = contactNeighbours(0,0)
inp = [["K","K","K"],
         ["K","K","K"],
         ["K","K","K"]]


inpInit = [["K","K","P","K"],["K","K","P","K"]]       

tm = TMatrix(inpInit)
tm.stitchNew()
tm.print()
curr = tm.data[0][0]
for i in range(24):
    try:
        print(curr.getST(),curr.getXY())
        curr = curr.next
    except:
        print("Stopped")
        