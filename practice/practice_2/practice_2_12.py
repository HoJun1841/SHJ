a = b =[1,2,3]
print(id(a),id(b))
a[1] = 4
print(b)

#list에서 a라는 변수에 접근했을 경우 하나의 리스트의 값에 접근을 한것이기 때문에 b에서도 접근할 경우 변경된 값으로 출력된다