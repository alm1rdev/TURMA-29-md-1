
#(celsius x 1,8) + 32

celsius=[0 ,10, 20, 30]

# resultado=list(map(lambda n : (n * 1.8) +32,celsius))

# print(resultado)

# #com DEF
# def fareh (n):
#     return (n * 1.8) +32

# print(list(map(fareh,celsius)))

#----------------------------------------------
maior_q50=[(n*1.8)+32 for n in celsius if n>10]
print(maior_q50)
