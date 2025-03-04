class Calculator:
    def __init__(self):
        self.value = 0
        
    def add(self, val):
        self.value += val
        
    def munus(self, val):
        self.value -= val
    
class UpgradeCalculator(Calculator):
    def __init__(self):
        super().__init__()
        
cal = UpgradeCalculator()
cal.add(10)
cal.munus(7)

print(cal.value) # 10에서 7을 뺀 3을 출력력