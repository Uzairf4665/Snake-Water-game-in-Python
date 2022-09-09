import random
def game(p1,p2):
    if p1==p2:
        return None
    elif p1=='s':
        if p2 =='w':
            return False
        elif p2=='g':
            return True
    elif p1=='w':
        if p2 =='s':
            return True
        if p2=='g' :
            return False
    elif p1 == 'g':
        if p2=='s':
            return False
        elif p2=='w':
            return True
print("p1 turns snakes(s),water(w),gun(g)?")
randno = random.randint(1,3)
if randno == 1:
    p1='s' 
elif randno ==2:
    p1 ='w' 
elif  randno ==3:
    p1 ='g'  


p2 =input("your turn snake(s),water(w) or gun(G)?")
a = game(p1, p2)
print(f"Computer chose {p1}")
print(f"You chose {p2}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")

