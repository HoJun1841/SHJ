'''
#if문
today = '일요일'
if today =='일요일':
    print('게임 한 판')
print('공부 시작')

today = '수수요일'
if today == '일요일':
    print('게임 한 판')
elif today == '토요일':
    print('폰 5분만')
else:
    print('물 한잔')
print('공부 시작')

yellow_card = 0
foul = True
if foul:
    yellow_card += 1
    if yellow_card == 2:
        print('경고 누적 퇴장')
    else:
        print('휴 조심해야지')

#for문
# x : 임시 변수
# range : start, stop, step
for x in range(1,11,2):
    print(f'팔 벌려 뛰기 {x}번 해')
    
my_list = [1,2,3,4,5,6,7,8,9,10]

for x in my_list:
    print(x)
    
person = {'이름': '나귀욤', '나이': 7, '키': 120, "몸무게": 23 }
for k, v in person.items():
    print(k,v)
    
fruit = 'apple'
for x in fruit:
    print(x)

#while문
max = 25
weight = 0
item = 3

while weight + item <= max:
    weight += item
    print(f'짐 {weight}추가합니다')
print(f'총 무게는 {weight}입니다.')

#함수
def show_price():
    print('10000원 입니다.')
    
show_price()

def get_price():
    return 15000

print(get_price())

price = get_price()

print(price)

def get_price(is_vip = False):
    if is_vip ==True:
        return 10000 # 단골 손님
    else:
        return 15000 # 일반 손님
price1 = get_price()
print(price1)
price2 = get_price(True)
print(f'커트 가격은 {price2} 원입니다.')

def order(shot=2, size='Regular', takeout=True): # 커피 주문
    print(f'아메리카노 {size} 사이즈 {shot}샷')
    if takeout:
        print('포장 주문이 완료되었습니다')
    else:
        print('주문이 완료 되었습니다')
        
order()
order(shot=5)
order(size='Venti')
order(takeout=False)

def visit(today, *customers):
    print(today)
    for customer in customers:
        print(customer)
        
visit('오늘','나')
print('-'*10)
visit('오늘','나','너')
print('-'*10)
visit('오늘','나','너','우리')

def print_kwargs(**a): #딕셔너리 전용 가변인자
    print(a)
    return a
    
res = print_kwargs(name='foo', age = 3, height = 150)
print(type(res))

#지역변수
def secret():
    message = '이건 나만의 비밀' #secret 함수 내에서 정의
    print(message) #값 출력 가능
    message = '함수 내에서는 자유롭게 수정이 가능해요'

def please():
    message = '이렇게 하면 되지?'
    print(message)

secret()
please()

#전역변수
message = '나는 전역 변수'

print(message)

def no_secret():
    global message
    message = '오 진짜 전역 변수!!' # 전역 변수 값 변경
    print(message,id(message))
    
no_secret()
print(message,id(message))

#사용자 입력
num = int(input('몆 분이세요?'))

if num > 4:
    print('죄송합니다만 4명까지만 예약가능합니다.')
else:
    print('예약가능합니다.')
    
#파일입출력-파일쓰기
f = open('list.txt','w',encoding='utf8')
f.write('김xx\n') ##문장 입력하기
f.write('정xx\n') ##문장 입력하기
f.write('허xx\n') ##문장 입력하기
f.close()


#파일입출력-파일읽기
f = open('list.txt','r',encoding='utf8')
contents = f.read()
print(contents)

f.close()

#파일입출력-with 파일쓰기
with open('list.txt','w',encoding='utf8') as f:
    f.write('김xx\n')
    f.write('정xx\n')
    f.write('허xx\n')
    
#파일입출력-with 파일읽기
with open('list.txt','r',encoding='utf8') as f:
    contents = f.read()
    print(contents)
'''