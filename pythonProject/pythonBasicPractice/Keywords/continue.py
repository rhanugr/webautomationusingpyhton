# continue : stop the execution of the current iteration and control will be transferred for next iteration:
a = 0
while a < 4:
    a += 1
    if a==2:
        continue
    print(a)

'''
    Output:
        1
        3
        4
    '''