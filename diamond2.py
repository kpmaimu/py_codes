n=int(input("enter the max star length"))
m=n
s=m
o=m+1
for x in range(1,2*(m+1)):
	if x<m+1:
		for t in range(s,0,-1):
	  		print(" ", end="")
		s=s-1
		for i in range(0,x):
	  		print("* ", end="")
		print()
	else:
		for x in range(s,m):
	  		print(" ", end="")
		s=s-2	
		for y in range(i-1,0,-1):
	  		print("* ", end="")
		print()
		
