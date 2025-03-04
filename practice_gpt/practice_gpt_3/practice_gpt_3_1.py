def num_classification(num):
    result = num
    if(result % 2 == 0):
        print('짝수입니다.')
    else:
        print('홀수입니다.')

num = int(input('정수를 입력해주세요:'))

num_classification(num)