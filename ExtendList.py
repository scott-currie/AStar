list1 = [(0,0), (1,1), (2,2)]
list2 = [(3,3), (4,4), (5,5)]

list1.extend(list2)
list1.append(list2)

print(list1)