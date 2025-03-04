def add(n):
    total = 0
    for i in n:
        total += i
        
    return total

my_list = map(int, input('숫자를 입력하세요:').split(','))

print(add(my_list))