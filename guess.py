answer_word="elephant"
print("Hint: its a wild animal")
guess=""
i=0
tries=0
while (i==0):
    
    guess=input("Take your guess  \n")
    
    if(guess==answer_word):
        
        print("You win")
        tries=tries+1
        i=i+1
        
    else:
        
        print("Try again")
        tries=tries+1

print("Number of tries=" + str(tries))
    