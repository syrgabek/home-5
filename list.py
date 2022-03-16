list1 = [ 1, 2, 3, 4 ]
list2 = [ 8, 12, 45, 67, 89, 45 ]
list3 = [ 78, 90, 65 ]
a = [list1,list2,list3]

for list in a:
    list.extend(list)
print(f'list1{list1}\nlist2{list2}\nlist3{list3}')