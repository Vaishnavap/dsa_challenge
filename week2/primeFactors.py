n=int(input())
i=2
while i<=n//2:
    if n%i==0:
        flag=0
        for x in range(2,i//2+1):
            if i%x==0:
                flag=1
                break
        if flag==0:
             print(i)
    i=i+1

