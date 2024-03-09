import math
import random
lower=int(input("adad avalo vared kon!: "))
upper=int(input("adad dovom ra vared kon!: "))
x=random.randint(lower,upper)
print(round(math.log(upper-lower+1,2)))
count=0
for count in range(count<=math.log(upper-lower+1,2)):
    while count < math.log(upper-lower+1,2):
        count = count+1
    
        guess=int(input("ye adad hads bezan: "))
        
    if x==guess:
        print("yo did it in ",count,"try")
        break   
    elif x>guess:
        print("too small!")
    elif x<guess:
        print("too big!")

if count >= math.log(upper-lower+1,2):
    print("The number is",x)
    print("Try again! ")







