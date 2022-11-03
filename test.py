from utils import contactNeighbours, TMatrix
import utils
from topology import TopologyGraph
cn = contactNeighbours(0,0)
# cn.print()
inp = [["K","K","K"],
         ["K","K","K"],
         ["K","K","K"]]

inp1 = [["K","K","K","K"]]
tuck = [["K","K","K","K"],["K","T","T","K"],["K","K","K","K"]]       
miss = [["K","K","K"],["K","M","K"],["K","M","K"],["K","K","K"],["K","K","K"],["K","K","K"],["K","K","K"],["K","K","K"],["K","K","K"],["K","K","K"],["K","K","K"]]

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
            print(f"{tab[i][j].st} {tab[i][j].av} {tab[i][j].mv}", end=";")
        print()

tp = TopologyGraph(tuck[0:3])
print(tp.n,tp.m)
tp.stitch()


showTable(tp.data)
# yp = tp.followTheYarn()
# print(yp,"\n")
# showTable(tp.data)
# # print(tp.nextCN(2,3,False,0))


tp.draw()

# i,j,ln,cr = 0,0,True,0

# for x in range(30):
#     print(i,j,ln,cr)
#     i,j,ln,cr = tp.nextCN(i,j,ln,cr)