# # def avg(*names):
# # 	print(names)
# # avg('Batman','superman','Ironman')

# # output
# # --------
# # hello Batman welcom to Digital Lync
# # hello superman welcom to Digital Lync
# # hello Ironman welcom to Digital Lync

# # Type --------2
# # ----------------------------
# # convietiall follow this syntxa
# # *kwargs
# # **kwargs

# # def avg(**details):
# # 	# print(details)
# # 	# print(type(details))
# # 	for key,value in details.items():
# # 		print('this is',key,'from',value,'Welcom to digital Lync')
# # avg(Batman = 'usa',superman = 'pakistna',Ironman = 'India')


# # This is  Batman from usa welcom to Digital Lync
# # This is  superman from pakistna welcom to Digital Lync
# # This is  Ironman from india welcom to Digital Lync


# # return keyword
# # -----------------------------

# # def hello():
# # 	return 1+3
# # hello()
# # # print(hello)
# # print(hello())


# # sops and var accesing
# # ---------------------------------


# a = 1
# def f1():
# 	# a =4
# 	print(a)
# # def f2():
# # 	a = 5					
# # 	return a
# def f3():
# 	global a
# 	a = 7
# 	print(a)		#swati==== 9,4,5,6,eror
# def f4():			#firoz == 9,7,6,4,
# 	print(a)
# f1()
# f3()
# f4()

# # print(a)
# # f3()
# # a = 6
# # f3()
# # print(a)

# # a = 9				#9,9,eror
# # print(a)
# # f1()
# # a =6 
# # print(f2())
# # print(a)
# # f3()
# # f4()


# # # local var to a globa varble is done by using keyword call global



# Anaomy function or lambda function
# =========================================
# lambda --------- > keyword

# syntax

# lambda arg: expression
# var = lambda arg : expression
# function call is done by var(parametrs)'


# squ = lambda a : a**3
# print(squ(3))

# inbut functions applicable for lambda function
# -----------------------------------------------------
# map()
# filter()

# map(fun or exp , squ)-----------> it mas the elems in the squ and give a boolen o/p with the help of expression

# filter(fun or exp , squ)--------> It filter the requird elemts in a seq by refer the expression


# l = [a for a in range(0,21)]

# # print(l)
# # even = list(map(lambda a : a%2==0  , [1,4,3,2,2,3,4,555,33,2,4,6,7,88,]))
# # print(even)


# odd = (filter(lambda a: a%2!=0,l))
# # for a in odd:
# # 	print(a)
# print(odd)


# l = [1,4,3,2,2,3,4,555,33,2,4,6,7,88,4]
# # mean = sum(l)/len(l)-1
# # print(mean)

# fun(l,ele)


# l = [1,2,3,4,1,2,3,4,1,5]

# print(min(l))
# print(max(l))

# mode  = 

def squ(a,b):
	c = a**2 +2*a*b + b**2 
	return c
print(squ(2,3))
