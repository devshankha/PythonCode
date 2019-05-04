#list = [12,45,"David",45.6]
#print(list)
tup = (34.5,"Raju",12)
print(tup)
dic = {1:"David",2:"Raju"}
print(dic)

list1 = []
list1.append("A")
list1.append("B")
list1.append("C")
print(list1)
# tuple is unmodefiable, so first convert it to a list
# and then add
tup1 = (1,2,3)
print(tup1)
list2 = list(tup1)
list2.append(4)
list2.append(5)
list2.append(6)
tup1 = tuple(list2)
print(tup1)

dic ={}
dic[0] = "Rajiv"
dic[1] = "Kaju"
dic["Tim"] = "Timothy"
print(dic)
