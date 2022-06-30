# 小彭的乱码
import operator

list1 = [1, 3, 2, 4, 5, 3, 2]
# list1.sort()
# print(list1)
# print(sorted(list1))
# print(list1)
# print(sorted(list1, reverse=True))
# list1.sort(reverse=True)
# print(list1)
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
# student_tuples.sort(key=lambda student : student[1], reverse=True)
# print(student_tuples)
student_tuples.sort(key=operator.itemgetter(2))
print(student_tuples)
