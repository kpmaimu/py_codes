print("diaomond printing..........")
n=int(input("enter the max stars in line"))
if n>0:
	print("not a valid input")
	return 0
for i in range(1,2*n):
	if i > n:
		for l in range(n,i):
			print(" ", end="")
		for m in range(i, 2*n):
			print("* ", end="")
		print()

				
	else:	
		
		for j in range(n,i,-1):
        		print(" ", end="")
		for k in range(0,i):
			print("* ", end="")
		print()

	 