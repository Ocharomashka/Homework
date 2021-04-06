my_list = [2, 3.5, 'string', True, None, complex(5, 6)]

my_list.append("cosmos")
print(my_list)

my_list.insert(2,'goal')
print(my_list)

my_list.pop(2)
print(my_list)

print(my_list.index("cosmos"))

print(("love" or 100) in my_list)

my_list.extend("love")
print (my_list)

my_list.pop(7)
print(my_list)

for i in my_list:
    print(type(i))






