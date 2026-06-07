#数据类型
# count  = 10
# miles = 12.5
# name = "刘红忠"
# print(count)
# print(miles)
# print(name)
# print(type(count))
# print(type(miles))
# print(type(name))
# a,b,c = 1,2,"三号"
# print(a)
# print(b)
# print(c)

#列表list
"""列表是Python中最常用的数据结构之一，它是一种有序、可变的集合，
可以包含不同类型的元素。列表使用方括号 [] 来定义，元素之间用逗号分隔。
列表支持各种操作，如添加、删除、修改和访问元素。
列表元素不存在重复值，元素可以是不同类型，列表是有序的，可以通过索引访问，且元素可改变"""
# 定义一个列表
# items = ["苹果", "香蕉", "橙子"]
# # 增加
# items.append("葡萄")          # 末尾添加
# items.insert(1, "草莓")       # 插入到索引 1
# # 删除
# items.remove("香蕉")         # 按值删除第一个匹配项
# deleted = items.pop(2)       # 按索引删除并返回元素
# # items.clear()             # 清空列表
# # 查找
# if "苹果" in items:
#     index = items.index("苹果")
#     print("苹果 在索引", index)
# print("当前列表:", items)
# # 修改
# items[0] = "青苹果"          # 按索引修改
# for i, value in enumerate(items):
#     if value == "橙子":
#         items[i] = "甜橙"
# print("最终列表:", items)


#集合set
# pname = {'one','two','there','four'}
# print(pname)
# if 'two' in pname:
#     print("答案正确！")
# else:
#     print("答案错误！")
#集合的运算
# a = set('abcdefgh')
# b = set('abcfjhk')
# print(a)
# print(a-b) #差集
# print(a|b)#并集
# print(a&b)#交集
# print(a^b)#不同时存在的元素

# #元组tuple
# #元组是Python中的一种数据结构，它是一种有序、不可变的集合，
# # 可以包含不同类型的元素。元组使用圆括号 () 来定义，元素之间用逗号分隔。
# #元组的特点：元素不可修改，元素可以是不同类型，
# # 元组是有序的，可以通过索引访问，且元素不可改变
# # 定义一个元组 
# person = ("Alice", 30, "Engineer") 
# # 访问元组元素
# print(person[0])  # 输出: Alice

# # 元组的增删查改操作示例
# # 注意：元组本身是不可变的（无法原地增删改），下面演示通过创建新元组或先转换为列表来实现增删改

# print("原始元组:", person)

# # 查（访问、成员测试、索引）
# print("姓名:", person[0])
# print("职业是否为 'Engineer'?", "Engineer" in person)

# # 增（通过连接创建新元组）
# person_added = person + ("New York",)
# print("添加后新元组:", person_added)

# # 删（创建不包含某元素的新元组，或先转为列表再删除）
# person_without_age = (person[0], person[2])
# print("删除年龄后:", person_without_age)

# # 改（先转换为列表，修改后再转换回元组）
# person_list = list(person)
# person_list[1] = 31  # 更新年龄
# person_updated = tuple(person_list)
# print("修改年龄后:", person_updated)

# # 也可以用列表的 pop 来删除元素，然后再转回元组
# plist = list(person)
# plist.pop(1)  # 删除年龄
# person_after_pop = tuple(plist)
# print("用 pop 删除年龄后:", person_after_pop)

# # 清空（赋值为空元组）
# person_cleared = ()
# print("清空后:", person_cleared)


# #字典dict
# #字典是Python中的一种数据结构，它是一种无序、可变的集合，python3。7+版本中是有序的，
# # 可以包含不同类型的元素。字典使用花括号 {} 来定义，
# # 元素以键值对的形式存在，键和值之间用冒号 : 分隔。
# my_dict = {"name": "Alice", "age": 30}
# # 访问字典元素
# print(my_dict["name"])  # 输出: Alice
# # 字典的增删查改操作示例
# print("原始字典:", my_dict)
# # 查（访问、成员测试、获取值）
# print("姓名:", my_dict["name"])
# print("年龄是否存在?", "age" in my_dict)
# # 增（添加新键值对）
# my_dict["city"] = "New York"
# print("添加后字典:", my_dict)
# # 删（删除键值对）
# del my_dict["age"]
# print("删除年龄后字典:", my_dict)
# # 改（修改键对应的值）
# my_dict["name"] = "Bob"
# print("修改姓名后字典:", my_dict)
# #显示字典的所有键   
# print("字典的所有键:", my_dict.keys())
# #显示字典的所有值
# print("字典的所有值:", my_dict.values())
# # 清空（使用 clear 方法）
# my_dict.clear()
# print("清空后字典:", my_dict)
