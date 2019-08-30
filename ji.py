#我国古代数学家张丘建在《算经》一书中提出的数学问题：鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。
#百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
for num_cock in range(0,100):
    for num_hen in range(0,100):
        if(num_cock + num_hen +(100-num_cock*5-num_hen*3)*3 ==100):
             print('公鸡{0}只，母鸡{1}只，雏鸡{2}只'.format(num_cock,num_hen,(100-num_cock-num_hen)))
        