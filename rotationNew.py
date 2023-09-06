name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT
T = int(input())
for j in range(T):
    N,K = map(int,input().split())
    my_list=list(map(int,(input().split())))
      
    for i in range(K):
        for k in range(1,N):
            temp=my_list[0]
            my_list[0] = my_list[i]
            my_list[i] = temp
    print(my_list)