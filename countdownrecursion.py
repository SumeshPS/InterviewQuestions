def countdown(number):
    if number==0:
        print ('Completed') 
    else:
        print (number)
        countdown(number-1)
def sum_number(num):
    if num ==0:
        return 0
    else:
        return num + sum_number (num-1)

          
countdown(6)
print(sum_number(4))
