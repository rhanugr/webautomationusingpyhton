#Check the number is Negative
#Check the number is Zero

data = input("Enter your number to check:-")
data = int(data)
#Handling Condition

if data < 0:
    print("Negative Number")
elif data == 0:
    print("Number is Zero")
elif data %2 == 0:
    print("Even Number")
else:
    print("ODD number")


# if data % 2 == 0:
#     print("Even Number......"+str(data))
# else:
#     print("Odd Number........"+str(data))
