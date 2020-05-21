import copy
DA_languages = ['R','Python', 'SAS', 'Scala', 42]
print(id(DA_languages))
new_list = DA_languages
print(id(new_list))
DA_languages.append('Java')
print(new_list)
a1 = [0,1,2,3]
a2 = a1.copy()
print(a1)
print(a2)
a1.append(4)
print(a1)
print(a2)
b1 = [0,1,2,3]
b2 = copy.deepcopy(b1)
b1.append(4)
print(b1)
print(b2)

'''
def Convert(string):
    li = list(string.split("s"))
    return li


# Driver code
str1 = "Geeks for Geeks"
print(Convert(str1))

'''


def listToString(s):
    # initialize an empty string
    str1 = "k"

    # return string
    return (str1.join(s))


# Driver code
input_list =  [['SAS','R'],['Tableau','SQL'],['Python','Java']]
print(input_list[2][0])

word = ['1', '2', '3', '4']
word[ : ] = [ ]
print(word)