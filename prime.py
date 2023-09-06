import math
print("testing...............")
prime_list=[]

for i in range(10,100):
	flag=0
	for j in range(2,int(math.sqrt(i)+1)):
		if i%j==0:
			flag=1
			break
	if flag==0:
		prime_list.append(i)	
  		
print(prime_list)	