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


# doing this with comprehensions
state = ['Gujarat', 'Maharashtra', 'Rajasthan']
capital = ['Gandhinagar', 'Mumbai', 'Jaipur']
dict_using_comp = {key: value for (key, value) in zip(state, capital)}
print(dict_using_comp)


# doing this without comprehensions ==

state = ['Gujarat', 'Maharashtra', 'Rajasthan']
capital = ['Gandhinagar', 'Mumbai', 'Jaipur']
output_dict ={}
# Using loop for constructing output dictionary
for (key, value) in zip(state, capital):
    output_dict[key] = value

print(output_dict)

# doing this without comprehensions
paragraph = ["There was a fox." , 'It was brown in color.', "It was seen near that farm sometime back"]
single_word_list =[]

for sentence in paragraph:
    for word in sentence.split():
        single_word_list.append(word)

print(single_word_list)

# doing this with comprehensions

single_word_list  = [word for sentence in paragraph for word in sentence.split()]
print(single_word_list)

# find words that begin with a vowel

vowels = ['a','e','i','o','u']
vowels_comp = [word for sentence in paragraph for word in sentence.split() if word[0].lower() in vowels]
print(vowels_comp)










product = lambda x,y: x*y
print(product(3,4))

s1 = "dweded"
print(s1.upper())

ch = lambda x:x.upper()
print(ch("david"))





