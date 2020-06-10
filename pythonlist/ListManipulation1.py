'''
Python list manipulations

'''

list = [1,2,3]
# both will print [1, 2, 3, 1, 2, 3]
print(list*2)
print(2*list)

l = 2*list



list = [0,1,2,3,4,5,6,7,8]
print(list)
# [0, 1, 2, 3, 4, 5, 6, 7, 8]
#print('\n')
print(list[0:9])
# [0, 1, 2, 3, 4, 5, 6, 7, 8]
#print('\n')
print(list[0:9:2])
# [0, 2, 4, 6, 8]
#printing first 5 elements of a list
print(list[:5])
# [0, 1, 2, 3, 4]
#printing last 5 elements of a list
print(list[-5:])
# [4, 5, 6, 7, 8]
#printing all elements in the list
print(list[::])
#[0, 1, 2, 3, 4, 5, 6, 7, 8]
#printing all but the last 5 elements of a list
print(list[:-5])
# [0, 1, 2, 3]
#printing every 2nd element of a list
print(list[::2])
# [0, 2, 4, 6, 8]
#printing a list in reverse
print(list[::-1])
# [8, 7, 6, 5, 4, 3, 2, 1, 0]
print(list[-2::-1])
#[7, 6, 5, 4, 3, 2, 1, 0]
l =['a','b','c','d']
print(l)
print(l.pop(0))
print(l)
l.remove('b')
sd = "Ho-w are yo-u"
print(sd.split('-'))
