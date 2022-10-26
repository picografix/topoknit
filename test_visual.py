from visualize import addPath
from utils import contactNeighbours,TMatrix
from matplotlib.patches import ConnectionPatch
import matplotlib.pyplot as plt


cn = contactNeighbours(0,0)
# cn.print()
inp = [["K","K","K"],
         ["K","K","K"],
         ["K","K","K"]]


inp1 = [["K","K","K","K"],["K","K","K","K"],["K","K","K","K"]]       
inp2 = [["K","K","P","K"],["K","K","P","K"]]
inp3 = [["K","K","P","K"],["K","K","P","K"],["K","K","P","K"],["K","K","P","K"]]
inp4 = [["K","K","P","K"],["K","K","P","K"],["K","K","P","K"],["K","K","P","K"],["K","K","P","K"]]
tm = TMatrix(inp4)
tm.stitchNew()
tm.print()

        
for i in range(len(tm.data)):
    for j in range(len(tm.data[0])):
        temp = tm.data[i][j]
        print(temp.getXY(),temp.getST(), end=" ")
        try:
            print(temp.next.getXY(), end=" ")
        except:
            print(temp.next, end=" ")

        try:
            print(temp.prev.getXY())
        except:
            print(temp.prev)
        
        # print(temp.next)

fig,ax1 = plt.subplots(1, 1)

for i in range(len(tm.data)):
    for j in range(len(tm.data[0])):
        temp = tm.data[i][j]
        # try next
        try:
            A = temp.getXYRevert()
            B = temp.next.getXYRevert()
            addPath(A,B,ax1)
        except:
            print("No next for", temp.getXY())
        
        # try prev

        try:
            A = temp.getXYRevert()
            B = temp.prev.getXYRevert()
            addPath(A,B,ax1)
        
        except:
            print("No prev for ", temp.getXY())

plt.show()

