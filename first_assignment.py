import random

def main():
    num=random.randint(1,100)
    for i in range(3):
        try:
            gess_num=int(input(f"Attemp {i+1}:"))
            diff=num - gess_num 
            if diff == 0:
                print(f"You are correct, congratulation...\n the number is {gess_num}")
                break
            elif -2 <= diff <=2:
                print("you are close..")
            else:
                print("yor are so far from the answer.. ")
            if i<2:
                print("try again")

        except ValueError:
            pass
            # print("please enter number")
   
    print("game is over.. Good Luck in next time")
main()
