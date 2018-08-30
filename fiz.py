# files
# -------------

# imfromtion

# data, code

# Proprties or attributes of files
# name
# exteion
# 	.dll
# 	.pyc
# 	.py
# 	.c .java .html .js 
# 	.mpeg ,.img,jpg.png.mp3
# size of the files (bytes,megabyes ,kb,gb tb)
# location/path
# type of files 
# 	text
# 	csv
# 	excel
# 	database files
# 	word files
# 	ppt
# 	bin firls
# 	pdfs
# 	audio
# 	video
# 	images
# encoding
# 	utf - 8
# 	utf -16
# 	utf -32
# permission (You will use OS module)
# 	asscing 
# 	grating persomis to user
# encrtpython

# -------------------------------------------------
# oprtaion
	# read
	# write
	# append

# # open the file the follwing modes
# 	read -- 'r'
# 	write --- 'w'
# 	append -- 'a'
# 	readbinary -- 'rb'
# 	writebinary - 'wb'
# 	# + ------> advance modes
# 		read ----- 'r+'
# 		write ----- 'w+'
# 		readbinary -- 'rb+'
# 		writebinary --- 'wb+'
		

# open('filename.exteion','mode','encoding')


# f = open('sample.txt','w')
# # print(f)
# f.close()


# f = open('/home/vineet/Documents/vineet/python/todaysnews.txt','w')
# # print(f)
# f.close()

# .write('strings')


# f = open('todaysnews.txt','w')
# # print(f)
# f.write('This is the first line in the file\n\tthere \t is the new lin')
# f.write(''' # oprtaion
# 	# read
# 	# write
# 	# append

# # # open the file the follwing modes
# # 	read -- 'r'
# # 	write --- 'w'
# # 	append -- 'a'
# # 	readbinary -- 'rb'
# # 	writebinary - 'wb'
# # 	# + ------> advance modes
# # 		read ----- 'r+'
# # 		write ----- 'w+'
# # 		readbinary -- 'rb+'
# # 		writebinary --- 'wb+'
		
# ''')
# f.close()

# .read()
# f = open('todaysnews.txt','r')
# data =  f.read()
# print(data)
# f.close()

# with 
# ==============

# with open("new.txt",'w') as f:
#    f.write("my first file")
#    f.write("This file\n\n")
#    f.write("contains three lines\n")
#    f.close()
# with open("/home/vineet/Documents/vineet/python/dummy.txt",'w') as f:
# with open("new.txt",'a+') as f:
# 	f.write('with open("new.txt",w) as f:')
# 	f.close()


# with open("newopr.txt",'r') as f:
# 	# data = f.readline()
# 	# print(data)
# 	# print(f.readline())
# 	# print(f.readline())
# 	# print(f.readline())

# 	print(f.read(45))

# 	f.close()

# # file cursors postion
# seek(postion,offset(0,1))---------> change the cuurent post ion the curesor
# tell(posion,offset(0,1))----------> gives curret post of the  cursor

# f = open('newopr.txt','r+')
# print(f.tell())
# print(60*'-')
# print(f.read(50))
# print(60*'-')
# print(f.tell())
# f.seek(25,0,1)
# print(60*'-')
# print(f.tell())

# python directortys
import os
# os.mkdir('Dummyfolder')
# print(os.getcwd())
# # os.mkdir('/home/vineet/Documents/vineet/python/class_1000/Dummyfolder/dummy2')
# os.chdir('/home/vineet/Documents/vineet/python/class_1000/Dummyfolder/dummy2')
# print(os.getcwd())
# os.chdir('/home/vineet/Documents/vineet/python/class_1000')
# print(os.getcwd())

# os.rmdir('/home/vineet/Documents/vineet/python/class_1000/Dummyfolder/dummy2')

# os.remove('new.txt')
# os.rmdir()
# os.rename()
