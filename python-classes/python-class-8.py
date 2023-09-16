""" 
# SLICE
# x[:::] | start | end | Jump
x = "helloworld"
list = [0, 1,2,3,4,5,6,7,8,9]

print(list[2:5])
print(list[7:])
print(list[1::3])

# SPLIT | string to list
sentence = "This is a sample sentence"
csv_data = "car,bike,plane,truck,scooter"
date_str = "2023-09-01"
multiline_txt = ""Line 1
Line 2
Line 4
""
url = "https://www.google.com/path/method"

print(sentence.split(" "))
print(csv_data.split(","))
print(date_str.split("-"))
print(multiline_txt.split("\n"))

# JOIN | Convert list to string
words = ['this', 'is', 'a', 'sample', 'sentence']
sentence = " ".join(words)
print(sentence)

name = ['Alice', 'Bob', 'Charlie']
date = ['2023', '09', '01']
numbers = [100,102,103,104]

print(" ".join(name))
print("-".join(date))
# print(list[map(str, numbers)])

# TUPPLE | not perform mutation

l = [1,2,3,4]
t = (1,2,3,4)

lt = type(l)
tt = type(t)

lt.append(6)
# tt.append(6)

# Convert list to tupple
tupple_list = tuple(l)

print(
    id(tupple_list)
)
 """

# SET | Remove Duplicate | Mutable data tpe

s = {1, 2, 3, 4}
s.add(5)

# s.discard()
# s.remove()
# s.update()
# s.union()
# s.intersection()
# s.difference()



set_A = {1,2,3,4,5}
set_B = {4,5,6,7,8}

print(set_A.union(set_B))
print(set_A.intersection(set_B))
print(set_A.difference(set_B))
set_A.add(10)
set_B.add(10)
print(set_A)
print(set_B)
set_C = {3}
print(set_A.union(set_C))