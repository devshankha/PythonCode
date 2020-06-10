l = lambda x:x**2
print(l(2))

product = lambda x,y:x*y
print(product(7,8))

captain = "Mahendra Singh Dhoni"

s = lambda x:x.split('  ')
print(s(captain))

l2 = [2,4,5]
#print(map(lambda x:x**2,list))

cd = list(map(lambda x:x**2,l2))
print(cd)


sums_list = [3,5,9,7]
sums_list2 = (4,5,6,7)
print(list(map(lambda x,y : x+y, sums_list,sums_list2)))

list_of_names = ['nikola', 'james', 'albert']
list_of_names2 = ['tesla','watt','einstein']
proper = lambda x, y: x[0].upper()+x[1:] +' '+ y[0].upper()+y[1:]
print(list(map(proper, list_of_names,list_of_names2)))

divby3 = lambda x:  x % 3 == 0
my_list = [3,4,5,6,7,8,9]
div = filter(divby3, my_list)
print(list(div))

#Reduce
from functools import reduce
q  = reduce(lambda x, y: x+y, range(1,4))
print(q)

list_of_nums = [22,45,32,20,87,94,30]
print(reduce(lambda x,y: x if x>y else y,list_of_nums))
