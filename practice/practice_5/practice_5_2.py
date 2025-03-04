'''
class Calculator:
    def __init__(self):
        self.my_list = []
        self.count = 0
    
    def add(self, val):
        if self.count < 100:
            self.my_list.append(val)
            self.count += 1
        else:
            print('더 이상 저장할 수 없습니다.')
            
class MaxLimitCalculator(Calculator):
    def __init__(self):
        super().__init__()
           
cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)

print(cal.my_list)
'''

class Calculator:
    def __init__(self):
        self.value = 0
    
    def add(self, val):
        if self.value + val < 100:
            self.value += val
        else:
            print('값이 100을 초과하였습니다.')

class MaxLimitCalculator(Calculator):
    def __init__(self):
        super().__init__()
            
cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)

print(f'남아있는 값은 {cal.value} 이다.')

