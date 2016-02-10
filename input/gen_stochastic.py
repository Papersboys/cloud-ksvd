import numpy as np

if __name__=="__main__":
	f=open('edgeList.txt', 'r')
	out=open('stochastic.txt','w')
	degree_list=[]
	for line in f:
		words=line.rstrip().split(" ")
		node=words[1].split(",")
		degree=len(node)
		degree_list.append(degree)

	for i in range(0,len(degree_list)):
		for j in range(0,len(degree_list)):
			out.write(str(round(1.0/max(degree_list[i],degree_list[j]),2)))
			if(j!=len(degree_list)-1):
				out.write(",")
		out.write(" ")

	f.close()
	out.close()