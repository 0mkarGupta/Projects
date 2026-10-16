#input
#c guess
'''
user - rock 
    rock -rock = tie
    rock papaer = cpu
    rock scissor = user

user = paper
    papar- rock =user
    paperr - scissor= cpu
    papaer paper = tie

user = scissor
    scissor - scissr= tie
    scissor - papaer = uset
    scissor -rock = user
'''



import random
item_list = ["Rock","Paper","Scissor"]
# print("Type Exit to quit")
user = input("Enter Your Choice : Rock ,Paper ,Scissor ").lower()
cpu = random.choice(item_list).lower()
print(f"User: {user} CPU : {cpu}")

if user == cpu :
    print("Same Choice : Match Tie")
elif user.lower() =="rock":
    if cpu.lower()=="paper":
        print("Paper Covers Rock -> Computer WIN")
    else:
        print("Rock Smashes Scissor  -> You WIN")

elif user.lower() == "paper":
    if cpu.lower()=="scissor":
        print("Scissor cut paper -> Computer Win")
    else:
        
        print("Paper Covers Rock -> You WIN")
elif user.lower() =="scissor":
    if cpu.lower() == "paper":
        print("Scissor cut paper -> You Win")
    else:
        print("Rock Smashes Scissor  -> Computer WIN")





