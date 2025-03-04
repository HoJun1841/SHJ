def gugu(x): #x
    num = 1
    for i in range(9):
        if num < 10:
            print(x * num, end=" ")
            num += 1
        else:
            break


gugu(int(input("값을 입력하세요 : ")))