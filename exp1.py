n= int(input('Enter the length of list\n'))
ls = []
for a in range(0,n):
	l =  input('Enter the elemets in the list\n')	
	ls.append(l)
print(ls)
elm = input('Enter the elemet whose index number is need to find----!!\n')
def find(ls,elm):
	for a in ls:
		if a == elm:
			print(ls.index(elm))
find(ls,elm)