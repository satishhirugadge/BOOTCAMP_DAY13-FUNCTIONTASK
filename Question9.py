# 9.         Write a function called showNumbers that takes a parameter called limit. 
# It should print all the numbers between 0 and limit with a label to identify the even and odd numbers. 
# Example: If the limit is 3 , it should print:
# 0 EVEN
# 1 ODD
# 2 EVEN
# 3 ODD
limit=int(input("Enter any number between 1 to 20!!! : "))
def showNumbers(limit):
    for i in range(0,limit+1):  # as the indexing start from 0
                                 # when we take a input then it is always a string but here we are not taking input.
        
        if i%2==0:
            print(i," EVEN")
           
        elif i%2 !=0:
            print(i," ODD")

showNumbers(limit)










