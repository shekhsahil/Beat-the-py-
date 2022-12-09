import os
import random
c='y'
draw=0
life=5
score=0
match=1
os.system("cls")
name=input("input your name")
option=["scissor","paper","rock"]
def win (score,life):
        print("you won !!!")
        print("score : ")
        print(score)
        print("life : ")
        print(life)

def lost(score,life):
     print("you lost !!!")
     print("score : ")
     print(score)
     print("life : ")
     print(life)         
 
while c=='y':
 list=(random.choice(option))
 print("------------------------------------------------------------------------------")
 print("MATCH -->") 
 print(match)  
 move=input(name+" choose your move s for scissors, r for rock,p for paper")
 print(name+" you choosed "+move)
 print("python choosed "+list)
 if move=='p'and list=='paper'or move=='s'and list=='scissor'or move=='r'and list=='rock':
    print("Match draw !!!")    
 elif  list =="rock":
    if move=='s':
     life=life-1
     lost(score,life)
    elif move=='p':
        score=score+1
        win(score,life)
 #####################################################################
 elif  list =="paper":
    if move=='s':
        score=score+1
        win(score,life)
     
    elif move=='r':
     life=life-1
     lost(score,life)
 ###########################################################################     
 elif  list =="scissor":
    if move=='r':
        score=score+1
        win(score,life)
     
     
    elif move=='p':
        life=life-1
        lost(score,life)
 c=input("want to play again")   
 match=match+1
 if c!='y':
   print("Thanks for playing !!!")
   exit()
 if life==0:
          break;

print("Game Over")