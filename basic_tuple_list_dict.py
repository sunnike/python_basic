tp1 = tuple([43, 21, 6, 77, 83, 65, 1, 91, 33, 52])
print("tp1 = ", tp1)
list1 = list(tp1)
print("list1 = ", list1)
list1.sort()
print("list1.sort() = ", list1, "\n")

#----------------------------------------
dic_tel={'Johny':'0933333333', 'Ivy':'0922222222', 'Mary':'09111111111'}
dic_tel['Vic']='0955555555'
print('dic_tel = ', dic_tel)
print("(key) Vic Tel :", dic_tel['Vic'])
del dic_tel['Johny']
print('dic_tel = ', dic_tel)
print('dic_tel key list= ', list(dic_tel.keys()))
print('dic_tel key sorted= ', sorted(dic_tel.keys()), "\n")




#----------------------------------------

fruits = ['orange', 'grape', 'pitaya', 'blueberry']
fruits.append("banana")
print(fruits)
fruits.pop()
for index, fruit in enumerate(fruits):
	print(index, ':', fruit)


#----------------------------------------
name = 'jackfrued'
fruits = ['apple', 'orange', 'grape']
owners = {'1001': '骆昊', '1002': '王大锤'}
if name and fruits and owners:
    print('I love fruits!')



data = [7, 20, 3, 15, 11]
result = [num * 3 for num in data if num > 10]
print(result)  # [60, 45, 33]


keys = ['1001', '1002', '1003']
values = ['骆昊', '王大锤', '白元芳']
d = dict(zip(keys, values))
print(d)