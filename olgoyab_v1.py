'''This is a program to find the formula of mathematical patterns'''
import time
print('====================================================')
print('OLGOYAB v0.1')
print('This is a program to find the formula of mathematical patterns')
index1 = int(input('number 1 >> '))
index2 = int(input('number 2 >> '))
index3 = int(input('number 3 >> '))
index4 = int(input('number 4 >> '))
if index4-index3 == index2-index1:
	mainindex = index4-index3
	secindex = index1 - mainindex
	if secindex>=0:
		print(mainindex,'*','n','+',secindex)
	else:
		print(mainindex,'*','n',secindex)
else:
	print('not supported. you can help me in coding from github :)')
print('1) close the program')
print('2) contact me')
exit = int(input('need more? >> '))
if exit == 2 :
	print('====================================================')
	print('My email: Muhammadrajabi@yahoo.com')
	print('My github: github.com/Mohrajabi05')
	print('My Persian blog: rajabi-blog.ir')
	print('My English blog: soon :)')
	print('My German blog: soon :)')
print('====================================================')
print('program will be close 10 secoundes later!')
print('thanks for using this programm  :)')
print('====================================================')
time.sleep(10)
