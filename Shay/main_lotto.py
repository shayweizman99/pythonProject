from Shay.Lotto import Lotto
lt = Lotto()
count=0

print("the guessed nums are:", end="")
lt.show_num()

for i in range (6):
    guess=int(input("enter geussed numbers between 1-45: "))
    if guess<1 or guess>45:
        print("invalid guess")
        count=0
        break
    else:
        if lt.check_num(guess):
            count+=1

print(lt.win(count))
