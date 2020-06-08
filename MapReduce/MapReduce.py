from functools import reduce
first_list = [2, 4, 5]
l =list(map(lambda x: x**2, first_list))
print(first_list)
print(l)


sums_list = [3,5,9,7]
sums_list2 = (4,5,6,7)
l=(list(map(lambda x,y : x+y, sums_list,sums_list2)))
print(l)

list_of_names = ['nikola', 'james', 'albert']
list_of_names2 = ['tesla','watt','einstein']
proper = lambda x, y: x[0].upper()+x[1:] +' '+ y[0].upper()+y[1:]
l=(list(map(proper, list_of_names,list_of_names2)))
print(l)

div = lambda x: x%3 == 0
l111 = [1,3,5,6,7,9]
l = list(filter(div,l111))
print(l)


q = reduce(lambda x,y:x+y,range(1,2))
print(q)

l5 = [51,15,6,7,333]
lv=reduce(lambda x,y:x if x > y else y,l5)
print(lv)