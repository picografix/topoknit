from visualize import addPath
from utils import contactNeighbours,TMatrix
from matplotlib.patches import ConnectionPatch
import matplotlib.pyplot as plt


cn = contactNeighbours(0,0)
inp1 = [["K","K","K","K"]]*1
inp2 = [["K","K","K","K"]]*2
inp3 = [["K","K","K","K"]]*3
inp4 = [["K","K","K","K"]]*4
inp5 = [["K","K","K","K"]]*5
inpn = [["K","K","K","K"]]*10
tm = TMatrix(inpn)
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
        

fig,ax1 = plt.subplots(1, 1)

for i in range(len(tm.data)):
    for j in range(len(tm.data[0])):
        temp = tm.data[i][j]
        # try next
        try:
            A = temp.getXYRevert()
            B = temp.next.getXYRevert()
            addPath(A,B,ax1, "g")
        except:
            print("No next for", temp.getXY())
        
        # try prev

        try:
            A = temp.getXYRevert()
            B = temp.prev.getXYRevert()
            addPath(A,B,ax1, "r")
        
        except:
            print("No prev for ", temp.getXY())

plt.show()

