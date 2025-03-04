def total_sum(num):
    total = 0
    i = 1
    for i in range(i,num+1):
        total += i
        
    return total
    

num = int(input('숫자를 입력하세요:'))

print(total_sum(num))