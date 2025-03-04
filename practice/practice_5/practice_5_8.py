import sys

num = sys.argv[1:]
print(num,type(num))

result = 0

for i in num:
    result += int(i)

print(result)