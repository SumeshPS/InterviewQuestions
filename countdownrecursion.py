def countdown(number):
    if number==0:
        print ('Completed') //base case
    else:
        print (number)
        countdown(number-1) //recursive case
def sum_number(num):
    if num ==0:
        return 0
    else:
        return num + sum_number (num-1)
    

def fact(fct):
    if ( fct == 0 ):
        return 1
    else:
        return fct * fact ( fct-1 )


          
countdown(6);
print(sum_number(4));
print(fact(3));
