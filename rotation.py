n = int(input("enter the length of array"))
my_list=[]
for i in range(n):
  x=int(input())
  my_list.append(x)
print(my_list)
k= int(input("enter the number of iterations"))
for i in range(k):
  for i in range(1,n):
     temp=my_list[0]
     my_list[0] = my_list[i]
     my_list[i] = temp
      
  
print("rotated list........",my_list)