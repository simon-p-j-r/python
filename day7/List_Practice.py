# 小彭的乱码
list1 = [1, 2, 'pengjiaren']
list2 = [1, 3, 'wangdao']
print(list1)
print(list2)
print('*' * 50)

list1.insert(2, 2)
print(list1)
list2.append(4)
list1.extend(list2)
print(list1)
print(list2)
print('*' * 50)

list1[0] = 5
del list2[0]
print(list1)
print(list2)
list1.remove(2)
print(list2)
list2.pop()
list1.pop(0)
print(list1)
print(list2)
list2.clear()
print(list2)
print('*' * 50)

print(len(list1))
num_count = list1.count(1)
num_index = list1.index('wangdao')
print(num_count)
print(num_index)
print('*' * 50)


list1.pop(1)
list1.pop(3)
print(list1)
list1.sort()
print(list1)
list1.sort(reverse = True)
print(list1)
list1.reverse()
print(list1)





