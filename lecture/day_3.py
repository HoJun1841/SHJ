'''
C언어 : 절차적 언어(컴퓨터가 동작하는 기계적인 느낌 그대로)
- 속도가 빠르다

C++, C#, java 등 : 객체지향 언어
- 아이폰(물리적으로 사물) -

파이썬 : 대화형 인터프리터언어(객체지향을 추구)
'''

'''
#클래스
class VideMaker:
    def make(self):
        print('추억용 여행 영상 제작')

class MailSender:
    def send(self):
        print('메일 전송 완료')
        
class BlackBox:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def hi(self):
        print('하이')
class TravelBlackBox(BlackBox, VideMaker, MailSender):
    def __init__(self, name, price, sd):
        super().__init__(name, price)
        super().hi()
        self.sd = sd
        
    def set_travel_mode(self, min):
        print(f'{min}분 동안 여행 모드 On')

class AdvancedTravelBlackBox(TravelBlackBox):
    def set_travel_mode(self, min):
        print(f'{self.name} {min}분 동안 여행 모드 On')
        self.make()
        self.send()

b1 = TravelBlackBox('까망이', 20000, 128)
print(b1.name, b1.price)
b1.set_travel_mode(10)
b1.hi()
b1.make()
b1.send()

b2 = TravelBlackBox('하양이', 10000, 128)
b3 = AdvancedTravelBlackBox('까망이', 30000, 256)
b3.set_travel_mode(60)
'''

'''
b1 = BlackBox('까망이', 20000) #객체 생성, b1 : 블랙박스의 객체 변수
print(b1.name, b1.price)
b1.set_travel_mode(10)

b2 = BlackBox('하양이', 10000)
print(b2.name, b2.price)
b2.set_travel_mode(20)
'''
'''
#예외처리
num1 = 3
num2 = 0

try:
    result = num1 / num2
    print(f'연산 결과는 {result}입니다.')
except:
    print('에러가 발생했어요.')
else:
    print('정상 동작했어요.')
finally:
    print('수행 종료')

    
try:
    int('일이삼') #ValueError 발생
except ValueError:
    print('값이 이상해요')
except Exception as err:
    print('에러가 발생했어요')
finally:
    print('수행 종료')
'''
'''
#모듈
from module import goodjob , goodbye

goodjob.goodjob()
goodbye.goodbye()

import random

my_list = ['가위','바위','보']
print(random.choice(my_list))

from module import main

#main.func()
main.out_func()
'''
'''
import datetime
import time

day1 = datetime.date(2025, 2, 26)
day2 = datetime.date(2025, 1, 1)

#print(day1 - day2)

day3 = datetime.date(2025, 2, 26)
#print(day3.weekday())

#print(time.time())
a = time.localtime()
#print(time.asctime(a))
#print(time.ctime())

print(time.strftime('%Y/%m/%d  %H:%M:%S', a))


for i in range(10):
    time.sleep(0.5)
    print('출력')
'''
'''
import webbrowser

webbrowser.open_new('www.google.com')
'''

from faker import Faker

fake = Faker('ko-KR')

for _ in range(10):
    print(fake.job())
    #print(fake.name())
 
from fractions import Fraction
import sympy
