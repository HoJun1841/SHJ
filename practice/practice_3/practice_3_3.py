
floor = 0
num = 0

while True:   
    if(floor < 5):   
        if(num < floor):
            print('*',end="")
            num += 1
        else:
            print('*')
            num = 0
            floor += 1
    else:
        break

'''
i = 0    
while True:
    i += 1
    if i < 5:    
        break
    print('*'*i)
'''