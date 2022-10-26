from matplotlib.patches import ConnectionPatch
import matplotlib.pyplot as plt


def addPath(xyA,xyB,ax1, c):


	coordsA = "data"
	coordsB = "data"
	con = ConnectionPatch(xyA, xyB, coordsA, coordsB,
												arrowstyle="->", shrinkA=5, shrinkB=5,
												mutation_scale=20, fc="w", color = c)

	ax1.plot([xyA[0], xyB[0]], [xyA[1], xyB[1]], "bo")
	ax1.add_artist(con)




x = [1,1,2,2,3,3]
y = [0,1,1,0,0,1]
fig, ax1 = plt.subplots(1, 1)

if __name__ == "__main__":
	for i in range(5):
		A = (x[i],y[i])
		B = (x[i+1],y[i+1])
		addPath(A,B,ax1)

