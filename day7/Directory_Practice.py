# 小彭的乱码
info_dir = {"name":"pengjiaren", "age":18, "Uni":'新大'}
info_dir_add = {"gender":"male"}
print(info_dir)

print(info_dir["name"])

info_dir["habby"] = "film"
info_dir["age"] = 22
print(info_dir)

info_dir.pop("Uni")
print(info_dir)

print(len(info_dir))

info_dir.update(info_dir_add)
print(info_dir)

info_dir_add.clear()
print(info_dir_add)

for num in info_dir:
    print(num)

print(info_dir.items())

info_dir_copy = info_dir.copy()
print(info_dir_copy)

list1 = ["peng", "jia", "ren"]
info_dir_fromkeys = dict.fromkeys(list1, 0)
print(info_dir_fromkeys)

print(info_dir.get('name'))

print(info_dir.popitem())