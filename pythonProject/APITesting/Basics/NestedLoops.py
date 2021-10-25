
data = input("Enter your Number to Check :-")

data = int(data)
#
# if(data < 0):
#     print("Negative Number")
# else:
#     if(data % 2 ==0):
#         print("Even Number")
#     else:
#         print("Odd Number")

if(data >= 0):
    if(data % 2==0):
        print("Even Number")
    else:
        print("Odd Number")

else:
    print("Negative Number")