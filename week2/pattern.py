n =6
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    print(1,end=" ")

    for j in range(2,i+1):
        print(j,end=" ")
    if i!=0:
        print(1,end="")
    print()