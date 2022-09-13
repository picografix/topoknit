from utils import contactNeighbours, TMatrix

cn = contactNeighbours()

inp = [["K","K","K"],
         ["K","K","K"],
         ["K","K","K"]]


inpInit = [["K","K","K","K"]]       

tm = TMatrix(inpInit)

# tm.print_row()
print("Before")
tm.print()

tm.knitPurlStich(0,0,0)
# tm.print_row(0)
print("\nAfter")
tm.print()
# tm.size()
# cn.print()\

# data = [[0]*(2*4)]*(1)
# print(data[0])
