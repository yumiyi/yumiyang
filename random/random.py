'''
Purpose:Random choose the member in the file.
'''
import random

with open("C:\\Users\\ASUS\\Documents\\yumiyang\\random\\name2.txt", 'r',
          encoding='utf8') as f:
    CONTENT = f.read().split("\n")
print(CONTENT)
SELECT = random.sample(CONTENT, 10)
print(SELECT)
