def common_multiple(n):
    my_list = []
    total = 0
    for i in range(n):
        if i != 0:
            if i % 3 == 0 or i % 5 == 0:
                my_list.append(i)
    
    print(f'1에서 {n}까지의 범위에서 존재하는 3과 5의 공배수는')
    print(f'{my_list}이다.')
    total = sum(my_list)
    print(f'값을 전부 더한 총합은 {total}이다.')
    
num = int(input('원하는 값을 입력해주세요: '))
common_multiple(num)