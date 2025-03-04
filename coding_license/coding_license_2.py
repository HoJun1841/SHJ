a = {'A': 90,'B': 80} 

try:
    a['C']
except:
    a.update({'C': 70})
    print(a)