from utils import contactNeighbours, TMatrix
import utils
from topology import TopologyGraph
cn = contactNeighbours(0,0)
# cn.print()
inp = [["K","K","K"],
         ["K","K","K"],
         ["K","K","K"]]

inp1 = [["K","K","P","K"]]
inpInit = [["K","K","P","K"],["K","K","P","K"]]       
miss_inp1 = [["K","K","K","K"],["K","T","T","K"],["K","K","K","K"]]

"""
tm = TMatrix(inpInit)
tm.stitchNew()
# tm.knitPurlStich(0,0,0)
# tm.knitPurlStich(1,0,0)
tm.print()
# tm.printDetail()
# tm.data[0][1].show()
curr = tm.data[0][0]
for i in range(24):
    try:
        print(curr.getST(),curr.getXY())
        curr = curr.next
    except:
        print("Stopped")
"""

# new algorithm testing

def showTable(tab):
    for i in reversed(range(len(tab))):
        for j in (range(len(tab[i]))):
            print(tab[i][j].st, end=" ")
        print()

tp = TopologyGraph(inp1)
tp.stitch()
showTable(tp.data)
yp = tp.followTheYarn()
print(yp)
print(tp.nextCN(0,2,True,0))
# tp.draw()