def countdown(number):
    if number==0:
        print ('Completed') 
    else:
        print (number)
        countdown(number-1)
          
countdown(6)
