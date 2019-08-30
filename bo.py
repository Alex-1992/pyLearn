a = 1
b = 1
print(str(a),", ",str(b),", ",end='')
for _ in range(0,100):
        a,b = b,a+b
        print(str(b),", ",end='')
