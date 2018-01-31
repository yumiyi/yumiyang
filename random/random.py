'''
Purpose:Random choose the member in the file.
'''
import random
member = open('C:\\Users\\ASUS\\Documents\\yumiyang\\random\\name.txt','r')
file = member.read().split("\n")
print (file)
selectN = random.sample(file,10)
print (selectN)