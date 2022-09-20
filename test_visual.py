from visualize import addPath
from utils import contactNeighbours,TMatrix
from matplotlib.patches import ConnectionPatch
import matplotlib.pyplot as plt


cn = contactNeighbours(0,0)
# cn.print()
inp = [["K","K","K"],
         ["K","K","K"],
         ["K","K","K"]]


inpInit = [["K","K","P","K"],["K","K","P","K"]]       

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
        print("Stopped",i)
        

curr = tm.data[0][0]
fig, ax1 = plt.subplots(1, 1)
for i in range(17):
    A = curr.getXY()
    B = curr.next.getXY()
    addPath(A,B,ax1)
    curr = curr.next

plt.show()