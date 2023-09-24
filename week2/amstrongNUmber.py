def isArmstrong(n):
    temp=n
    count=0
    sum=0
    while temp!=0:
        temp=temp//10
        count+=1
    temp=n
    while temp!=0:
        dig=temp%10
        temp=temp//10
        sum+=dig**count
    if sum==n:
       return True
    else:
        return False
n=int(input("Enter a number\n"))
print(isArmstrong(n))