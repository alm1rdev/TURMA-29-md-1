
lista=['a',1,1.1,True,[0,1,2],(1,2),
       {0,1},{'nome':'almir'}
       ]

for item in lista:
    if isinstance(item,str):
        print(item.upper())

    elif isinstance(item,set):
        item.add(2)
        print(item)

    elif isinstance(item,int,float):
        mult=item *2
        print(mult)
