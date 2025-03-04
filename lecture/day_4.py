'''
a = '한글'

b = a.encode('enc-kr')
print(b,type(b))

c = b.decode('utf-8')
print(c)
'''

'''
import time
def elapsed(orignal_func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = orignal_func(*args, **kwargs)
        end = time.time()
        print("함수 수행시간: %f 초" %(end - start))
        
        return result
    return wrapper
@elapsed
def myfunc(msg):
    """데코레이터 확인 함수"""
    print("'%s'을 출력합니다." % msg)
    
decorated_myfunc = elapsed(myfunc)
decorated_myfunc()
'''

'''
class MyItertor:
    def __init__(self, data):
        self.data = data
        self.position = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.position >= len(self.data):
            raise StopIteration
        result = self.data[self.position]
        self.position += 1
        return result

if __name__ == "__main__":
    i = MyItertor([1,2,3])
    for item in i:
        print(item)
'''

