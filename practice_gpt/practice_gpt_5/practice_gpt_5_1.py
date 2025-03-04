class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def greet(self):
        return f'{self.name}님이 {self.age}살입니다.'
        
person1 = Person("홍길동", 30)
print(person1.greet())