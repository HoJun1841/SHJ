def add_over_fifty(n):
    #print(type(n))
    total = 0
    for i in n:
        if i > 50:
            total += i
    return total

A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]

print(add_over_fifty(A))