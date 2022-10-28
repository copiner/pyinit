

def flower():
    for i in range(100, 1000):
        t = str(i)
        a = int(t[0])
        b = int(t[1])
        c = int(t[2])
        '''
        a = i % 10
        b = i // 10 % 10
        c = i // 100
        '''
        if a**3 + b**3 + c**3 == i:
            print(i)

flower()
