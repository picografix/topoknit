from utils import contactNeighbours, TMatrix

cn = contactNeighbours()

inp = [["K","K","K"],
         ["K","K","K"],
         ["K","K","K"]]
inpInit = [["K","K","K","K"]]       

tm = TMatrix(inpInit)

tm.readinpRowLeft(inpInit)
tm.print()
# tm.size()
# cn.print()\

# data = [[0]*(2*4)]*(1)
# print(data[0])