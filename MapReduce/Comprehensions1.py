input_list = [1,2,3,3,4,7,11,14]
output_list = []
for x in input_list:
    if x%2 == 0:
        output_list.append(x)
print(output_list)


input_list1 = [1,2,3,3,4,7,11,14]
output_list1 = [x for x in input_list if x % 2 == 0]
print(output_list1)

input_list2 = [1,2,3,4,4,5,6,7]
output_list2 = [x**2 for x in input_list2]
print(output_list2)

input_list = [1, 2, 3, 4, 5, 6, 7]

output_dict = {1:"David",2:"Hussain"}
dtct2 = {x:x**2 for x in output_dict}
print(dtct2)
print(output_dict)

product = lambda x,y: x*y
print(product(3,4))

s1 = "dweded"
print(s1.upper())

ch = lambda x:x.upper()
print(ch("david"))





