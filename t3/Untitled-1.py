number1 = int (input())
number2 = int (input())
number3 = int (input())
if number1>number2 and number2>number3 : 
    print("--------------")
    print(number1)
    print(number2)
    print(number3)
elif  number1>number3 and number3>number2 : 
    print("--------------")
    print(number1)
    print(number3)
    print(number2)  
elif  number2>number1 and number1>number3 : 
    print("--------------")
    print(number2)
    print(number1)
    print(number3)  
elif  number2>number3 and number3>number1 : 
    print("--------------") 
    print(number2)
    print(number3)
    print(number1)  
elif  number3>number2 and number2>number1 : 
    print("--------------") 
    print(number3)
    print(number2)
    print(number1)  
elif  number3>number1 and number1>number2 : 
    print("--------------")
    print(number3)
    print(number1)
    print(number2)  
