def num_compare(num1, num2, num3):
        max_value = 0
        if num1 > num2:
            max_value = num1
            if max_value > num3:
                return max_value
            else:
                max_value = num3
                return max_value
        else:
            max_value = num2
            if max_value > num3:
                return max_value
            else:
                max_value = num3
                return max_value
                

num1, num2, num3 = map(int,input('숫자 3개를 입력하세요:').split())

print(num_compare(num1, num2, num3))



