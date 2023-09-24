import keyboard
print("Printing the Prime numbers")
x=2
while x>0:
    flag=0
    for i in range(2,int(x/2)+1):
        if x%i==0:
          flag=1
    if flag!=1:
        print(x)
    x+=1
    if keyboard.is_pressed('s'):
       print("Exiting loop")
       break

