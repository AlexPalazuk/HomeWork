def foo(file):
    with open(file, mode='r') as stream:
        line = stream.readlines()
    return line
list1 = foo("./Task1/test1.txt")
list2 = foo("./Task1/test2.txt")

list3 = []

def compare(some_list, some_list2):
    for i in some_list:
        if i not in some_list2:
            list3.append(i)
    return list3
compare(list1, list2)
compare(list2, list1)
print(list3)