print("1-add")
print ("2-subract")
print("3-Multiply")
print("4-divide")
option=int(input("Choose an operation:"))
result = 0
if(option in [1,2,3,4]):
    num1=int(input("enter the first number"))
    num2=int(input("enter the Second number"))
    
    if(option == 1):
        result = num1 + num2
    elif(option == 2):
        result = num1 - num2
    elif(option == 3):
        result = num1 * num2
    elif(option == 4):
        result = num1 // num2
       
    
else:
    print("invalid operation")
print("The Result of the operation is {}".format(result))