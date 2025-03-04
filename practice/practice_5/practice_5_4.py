"""
def sign_calculation(n):
    if n > 0:
        return n        
"""
my_list = [1, -2, 3, -5, 8, -3]

result = filter(lambda x : x > 0, my_list)

print(list(result))