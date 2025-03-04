import re

pattern = re.compile('[a-z]+')
#result = pattern.match('3 python')
#result = pattern.search('3 python')
result = pattern.findall('life is too short')
print(result)
print(result.group())
print(result.start())
print(result.end())
print(result.span())
