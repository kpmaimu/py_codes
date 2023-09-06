print("hellooooooo")


T = int(input())
for _ in range(T):
    n, k= map(int,input().split())
    l=list(map(int,input().split()))
    d=k%n
    print("n",n,"k",k, "l",l,"d",d)
    new_l = l[n-d:]+l[:n-d]
    print(new_l)

