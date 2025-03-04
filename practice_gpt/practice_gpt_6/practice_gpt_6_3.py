from pandas import Series, DataFrame
import pandas as pd

def get_total_page(m, n):
    total_page = 0
    total_page = m / n
    return total_page

my_data = {'게시물의 총 개수': [None],'페이지당 보여줄 게시물 수': [10,10,10,10],'총페이지 수': [1,3,5,7]}

#num_m, num_n = int(input('게시물의 총 개수와 페이지당 보여줄 게시물 수를 입력하세요: ').split(" "))
num_m = int(input('게시물의 총 개수를 입력하세요: '))
num_n = int(input('페이지당 보여줄 게시물 수를 입력하세요: '))


get_total_page(num_m, num_n)

#my_data.update({'게시물의 총 개수': num_n, '페이지당 보여줄 게시물 수': num_m, '총페이지 수': 10})

#frame = DataFrame(my_data)
print(DataFrame(my_data))