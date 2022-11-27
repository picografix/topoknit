from utils import contactNeighbours, TMatrix
import time
from topology import TopologyGraph
from matplotlib import pyplot as plt

start=  time.time()
temp = 0
end = 0



inp =   [["K","K","K","K","K","K","K","K","K","K","K","K","K","K","K","K","K"],
         ["K","T","K","T","K","T","K","T","K","T","K","T","K","T","K","T","K"],
         ["K","K","K","K","K","K","K","K","K","K","K","K","K","K","K","K","K"]]*17

inp_n = [["K","K","K"],]
inp22 = [["K","K"],["K","K"],["K","K"]]

inp1 = [["K","K","K","K"]]
tuck = [["K","K","K","K"],["K","T","T","K"],["K","K","K","K"]]
miss = [["K","K","K"],["K","M","K"],["K","M","K"],["K","K","K"],["K","K","K"],["K","K","K"],["K","K","K"],["K","K","K"],["K","K","K"],["K","K","K"],["K","K","K"]]
Tr = [["K","K","K","K","K"],["K","K","K","K","K"],["K","M","T","T","K"],["K","K","K","M","K"],["K","K","K","K","K"],]

pattern_1 = [
    ["K","K","K","K","K","K","K"],
    ["K","T","T","K","K","K","K"],
    ["K","K","K","K","T","T","K"],
    ["K","T","T","K","K","K","K"],
    ["K","K","K","K","T","T","K"],
    ["K","K","K","K","K","K","K"],
]
pattern_float = [

    ["K","M","K","M","K"],

]
pattern = [
    ["K","K","K","K","K","K","K"],
    ["K","T","T","T","T","T","K"],
    ["K","K","T","T","T","K","K"],
    ["K","K","K","T","K","K","K"],
    ["K","K","K","K","K","K","K"],
]
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
        for j, item in enumerate(tab[i]):
            print(f"{item.st} {item.av} {item.mv}", end=";")
        print()

# showTable(tp.data)
# yp = tp.followTheYarn()# print(yp,"\n")
# showTable(tp.data)
# # print(tp.nextCN(2,3,False,0))

# start=  time.time()
# m = 225
# b = [5,10,30,50,100,75,125,225,250]
# a = [0.31099677085876465,1.0165083408355713,7.785002946853638,20.296039581298828,72.87403631210327,43.12549376487732,112.08100295066833,251.71099996566772,321.041891]

# for i in range(8):
#     b[i] = b[i]*b[i]

# plt.plot(b,a)

# plt.xlabel("Number of stitches")
# plt.ylabel("Computational time in sec")
# plt.title("Graph of compuational time taken")

# plt.savefig("my.png")
# inp_n = [["K"]*m]*m
# print(inp_n)
tp =TopologyGraph(inp)
tp.stitch()
tp.draw()
tp.show(labels=False)
# end = time.time()

# print(end-start)

# for i in range(1,m,j):
#     temp = time.time()
#     tp = TopologyGraph(inp_n*i)
#     tp.stitch()
#     tp.draw()
#     tp.show(labels=False)

#     end = time.time()
#     a.append(end-temp)


# fig, ax = plt.subplots()

# ax.plot(range(1,m,j),a)
# ax.set_title('A single plot')
# plt.savefig("Graph.png")

# print(tp.getResistance())

# print(tp.end)
# i,j,ln,cr = 0,0,True,0

# for x in range(30):
#     print(i,j,ln,cr)
#     i,j,ln,cr = tp.nextCN(i,j,ln,cr)