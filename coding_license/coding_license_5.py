def Fibonacci(x,y,n):
    if x > n:
        return
    print(x, end=" ")
    Fibonacci(y, x+y, n)
    
start_num = 0
num = int(input('정수를 입력하세요:'))

Fibonacci(start_num, 1, num)
