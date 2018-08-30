l1 = ['hello',34,45.67,5+9j]
l2 = ['batman','ironman',77,34.223]
# print(l1)
# print(l2)
# print(type(l))
# print(type(l[0]),type(l[1]),type(l[2]),type(l[3]))

# print(l[0])
# l[0] = 'hi'
# del l[0]
# print(l1+l2)
# print(2*l1)

# Assigrn values in list

# l2.append('ironman')
# print(l2)
# print(l2.index('ironman'))
# l2.pop()
# l2.remove(77)
# l2.pop()
# print(l2)

l = [1,2,3,[45,67,89],'hello',56.89]
# print(l)
# print(l[2])
# print(len(l))
# print(l[3][1])
# print(l[3])
# print(l[3].index(67))
# print(l[:3])
# print(l[3:])
# l(inidatail index nuber:final index number:step  size)
# print(l[0:len(l):1])
# print(l[::-1])

# List comphersion
# -------------------------------------
# list()
# l = 'DigitalLync'
# l2 = list(l)
# print(l2)

# l1 = [a for a in range(0,11)]
l1  = [divya for divya in range(0,11)]
print(l1)

# inbuilt function in list
print(sum(l1))
print(min(l1))
print(max(l1))
print(len(l1))