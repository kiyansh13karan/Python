# write a prohram to convert USD to INR using user defined function :-


# function definiton :- 
def conv_usd(x) :
    a = 83.6 * x 
    return a 

# main function :-
USD = int(input("United State Dollar (USD) : ")) 
res = int(conv_usd(USD))  
print("Indian Rupee (INR) : " , res)