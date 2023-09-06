print("welcome to matrix world.........")
x, y=list(map(int,input("enter the size of matrix").split()))
print("order of matrix",x,y)
my_matrix=[]
print("Enter the Elements")
for i in range(x):
	a=[]
	for j in range(y):
		a.append(int(input()))
		print("hai")
	my_matrix.append(a)
print(my_matrix)
