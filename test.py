#list comprehension
list1=[1,2,3,4]
list2=[x+1 for x in list1]
print(list2)
name="Padre"
name_list=[l for l in name]
print(name_list)
doubles=[x*2 for x in range(1,10) if x %2==0]
names=["berh","bohr","hun","xin"]
names=[name.upper() for name in names if name.__len__()<4]
print(names)
print(doubles)
#with open("file1.txt") as file1:
 #   data=file1.write()
#dictionary comprehension
dict1={
    1:"a",
    2:"b",
    3:"c",
    4:"d",
    5:"e"
}
print(dict1.items())
dict2={x[0]:x[1] for x in dict1.items() if x[0]!=1}
print(dict2)