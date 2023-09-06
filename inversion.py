print("Matrix Inversion")
m,n=map(int,input("Enter the order of your Matrix").split())
print(m,n)
my_matrix=[]
print("Enter the element")
for i in range(m):
	a=[]
	for j in range(n):
		x=int(input())
		a.append(x)
	my_matrix.append(a)
print(my_matrix)
pairs=[]
num=0
for i in range(m):
	for j in range(n):
		for k in range(m):
			for l in range(n):
				if k >= i and l>= j:
					if my_matrix[i][j]> my_matrix[k][l]:
						num= num+1
						p="({},{})".format(my_matrix[i][j],my_matrix[k][l])
						pairs.append(p)
print(pairs)

print("number of inversion:",num)
					