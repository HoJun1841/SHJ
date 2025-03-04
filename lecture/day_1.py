'''
# 각각의 사칙연산에 대한 출력
print(5+2)
print(5-2)
print(5*2)
print(5/2)

# 나머지,몫,거듭제곱에 대한 출력
print(5%2)
print(5//2)
print(5**2)

# 비교 연산자에 대한 결과 출력
print(5>2)
print(5>=2)
print(5<2)
print(5<=2)
print(5==2)
print(5!=2)

#논리 연산자에 대한 결과 출력
print(3<5 and 7<5)
print(3<5 or 7<5)
print(not 3<5)

#멤버 연산자에 대한 결과 출력
print('c' in 'cat')
print('c' not in 'cat')

#파이썬 인덱싱/슬라이싱
lang = 'PYTHON'
print(lang[:])
print(lang[0])
print(lang[-1])
print(lang[0:])
print(lang[:6])
print(lang[3:5])

snack = '꿀꽈베기'
two = '2개'

juseyo = snack + two

print(snack+two)
print(juseyo)

print(len(juseyo))

print('-' * 20)
print('NadoCoding')
print('-' * 20)

#문자열 메소드
letter = 'how are YOU?'

print(letter.lower()) #소문자 변경 출력
print(letter.upper()) #대문자 변경 출력
print(letter.capitalize()) #앞글자만 대문자 변경 출력
print(letter.title()) #각 글자 앞글자만 대문자 변경 출력
print(letter.swapcase()) #대문자 소문자가 반대로 변경 출력

swap_letter = letter.swapcase()
print(swap_letter)

print(letter.split()) #각 글자별로 묶어서 출력

print(letter.count('how')) #특정 문자가 있는걸 세기


a = '   ...나도고등학교...   '
print(a.startswith('도도')) #시작글자가 맞는지 확인
print(a.endswith('고등학교')) #끝나는 글자가 맞는지 확인
print(a.strip('.')) #특정문자를 제거처리
print(a.lstrip('.')) #특정문자를 왼쪽만 제거처리
print(a.rstrip('.')) #특정문자를 오른쪽만 제거처리

lw = a.lstrip(' ')
print(a.lstrip(' ')) #특정문자를 왼쪽만 제거처리
print(len(lw))

rw = a.rstrip(' ')
print(a.rstrip(' ')) #특정문자를 오른쪽만 제거처리
print(len(rw))

python = '파이썬'
java = '자바'
c = 'c언어'

print(python + java)
print(python,java,c)
print('개발언어에는 {2},{1},{0}가 있어요.'.format(python,java,c))
print(f'개발언어에는 {python},{java},{c}가 있어요.')

print('하지만 \'나만 당할수없지\'라는 생각에 \"엄청쉽지\" 라고했다.')

print('C:\\SHJ\\test.py') #raw string 미사용시 적용법
print(r'C:\SHJ\test.py') #raw string 사용시 적용법

snack = "꿀꽈배기는\n너무\n맛있어요."
print(snack)

#리스트
#my_list = ['오예스','몽쉘','초코파이']
my_list = ['오예스','몽쉘','초코파이','초코파이'] #중복 허용
your_list  = [1,2,3.14,True,False,'아무거나'] #자료형에 대한 구분이 없음

print(my_list[0])
print(my_list[-1])
print(my_list[:3])
print(my_list[2:])
print(my_list[1:3])

print(your_list[0])
print(your_list[-1])
print(your_list[:7])
print(your_list[2:])
print(your_list[2:5])

my_list = ["오예스","몽쉘","초코파이",'초코파이','카카오오']
print(len(my_list))

my_list[1] = '몽쉘카카오' #몽쉘을 몽쉘카카오로 변경 후 출력
print(my_list)

my_list.append('가나초콜렛') #뒤에 가나초콜렛을 추가 후 출력
print(my_list)
my_list.remove('오예스') #오예스 항목을 제거 후 출력
print(my_list)

my_list = ["오예스","몽쉘","초코파이",'카카오']
your_list = ["빅파이","오뜨"]

print(my_list+your_list)

my_list.extend(your_list)
print(my_list)

my_list = ["오예스","몽쉘","초코파이",'카카오']
#my_list.insert(1,'여기 맞나') #윈하는 위치에 값 추가
#my_list.pop() #원하는 위치(또는 마지막)의 값 삭제
#my_list.clear() #모든 값 삭제
#my_list.sort() #값 순서대로 정렬
#my_list.reverse() #순서 뒤집기
#copy_list = my_list.copy() # 리스트 복사
#print(copy_list)
#print(my_list.count('오예스')) #어떤 값이 몇 개 있는지
#print(my_list.index('카카오')) #어떤 값이 어디에 있는지지

print(my_list)

#튜플
my_tuple = ("오예스","몽쉘","초코파이")

pie1,pie2,pie3 = my_tuple
print(pie1,pie2,pie3)

numbers = (1,2,3,4,5,6,7,8,9,10)

one,two,*others = numbers

print(one)
print(two)
print(others)

A = {"돈까스","보쌈","제육덮밥"}
B = {"짬뽕", "초밥", "제육덮밥"}

print(A.intersection(B))
print(A.union(B))
print(A.difference(B))

#딕셔너리
person = {'이름': '나귀욤','나이': 7, '키': 120,'몸무게': 23}

print(person['이름'])
print(person['나이'])
print(person['키'])
print(person['몸무게'])
print(person.get('별명'))
person['최종학력'] = '유치원'
print(person)
person['키'] = 130
print(person)
#person.update({'키':150,'최종학력':'대학교'}) #key value를 추가
#print(person)
#person.pop('몸무게') #특정 key value를 제거
#print(person)
#person.clear() #key value 전부 제거
#print(person)

print(person.keys())
print(person.values())
print(person.items())

#print(person.fromkeys())
#print(person.popitem())
#print(person)
#print(person.setdefault())

#튜플 리스트 변환
my_tuple = ('오예스','몽쉘')
print(type(my_tuple))
my_list = list(my_tuple)
print(my_list,type(my_list))
my_list.append('초코파이')
my_tuple = tuple(my_list)
print(my_tuple)


my_list = ["오예스","몽쉘","초코파이","초코파이","초코파이"]
my_dict = dict.fromkeys(my_list)
print(my_dict)
my_list =list(my_dict)
print(my_list)
'''