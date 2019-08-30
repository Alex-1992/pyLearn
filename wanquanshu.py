
for i in range(1,9999):
    temp = 0
    for j in range(1, i+1):
        if(j != i):
            if(i%j == 0):
                temp +=j
        elif(i == temp):
            print(i)

        