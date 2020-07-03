# a = (1,2,3)
# print(a)
# b = [1,23,43,5]
# print(b)
#元祖 长度不可变
# a = (1,2,3,4,5)
# print(type(a))
# b = (1,(2),{'name':'zyx'},[1,2,3],True,6)
# print(b[-2]) #倒数第几个值
# print(b)


#列表 长度可变
# a = [1,(2,4),{'name':'zyx'},[1,2,3],True,'hhh']
# print(a[0])
# print(a)
# a.append({'age':'22'})  #增加元素
# print(a)
# a.clear()   #清除所有元素
# print(a)
# a.pop(3)    #取出一个元素并删除
# print(a.pop(3))
# print(a.pop(3))
# print(a)
# b = a.count(1)  #计数
# print(b)
# print(a.index('hhh'))



#字典
a = {'name':'zyx','password':"123456"}
# print(a.get('name'))
# print(a['password'])
a["name"] = "ZHANGyx"
print(a["name"])

a["age"] = "22"
print(a)

a.pop("name")
print(a)

print(a)