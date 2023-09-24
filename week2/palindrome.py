n=int(input())
temp=n
sum=0
while temp!=0:
    digit=temp%10
    temp=temp//10
    sum=sum*10+digit
if sum==n:
    print("The number is palindrome")
else:
    print("The number is not palindrome")



