def factorial(n):
    total = 1
    for i in range (n):
        total = total * (n - i)
        print("Current i is: " + str(i))
        print("The current value of total is: " + str(total))
        ## first time total = 1
        ## increment each time total up to n
    return total
    ## return the FINAL value of total at the end

userstring = input("Number please: ")
usernum = int(userstring, 10)

print(str(usernum) + "! is " + str(factorial(usernum)))

