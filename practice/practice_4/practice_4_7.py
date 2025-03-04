f = open('test.txt', 'w', encoding='utf8')
f.write('Life is too short\n')
f.write('you need java\n')
f.close()

f = open('test.txt','r')
body = f.read()
f.close()

body = body.replace('java','python')

f = open('test.txt', 'w', encoding='utf8')
f.write(body)
f.close()
