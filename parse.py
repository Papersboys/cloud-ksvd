import numpy as np
import math
import sys

sites=int(sys.argv[1])
fin1=open("output/Site_0_D.txt", 'r')
out=open("Y_out.txt", 'w')
X=np.array([map(float,line.split(',')) for line in fin1])

for i in range(sites):
	fin=open("output/Site_"+str(i)+"_X.txt", 'r')
	Y=np.array([map(float,line.split(',')) for line in fin])
	M=np.transpose(np.dot(X,Y))
	np.savetxt(out,M)
	fin.close()

fin1.close()
out.close()