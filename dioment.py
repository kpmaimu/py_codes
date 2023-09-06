print("dioment.........")
n=int(input("enter the limit..."))
print("limit=",n)

#* * * *
# * * *
#  * *
#   *
#for x in range(n,1,-1)
m=n
for x in range(1,n+1):
   print(" "*m, end=" ")
   m = m-1
   print("* "*x)
m=m+2
for x in range(n-1,0,-1):
   print(" "*m, end=" ")
   m=m+1
   print("* "*x)
   
	 	