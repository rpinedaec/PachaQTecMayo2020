# lst = [1,2]
# for v in range(2):
#     lst.insert(-1,lst[v])

# print(lst)

# print(1//2)

# def func(a,b):
#     return b ** a

# #print(func(b=2,0))

# z=0
# y = 10
# x = y<z and z>y or y > z and z<y
# print (x)

# list = [x * x for x in range(5)]
# def fun ( lst):
#     del lst[lst[2]]
#     return lst

# print(fun(list))

# x = 1
# y=2
# x,y,z = x,x,y
# z,y,z = x,y,z
# print(x,y,z)

# a = 1
# b=0
# a = a ^ b
# b = a ^ b
# a = a ^ b
# print (a,b)

# def fun(x):
#     if x % 2 == 0:
#         return 1
#     else:
#         return 2

# print(fun(fun(2)))

# nums = [1,2,3]
# vals = nums
# del vals[:]
# print(nums,vals)

# x = int(input())
# y = int(input())
# x = x% y
# x = x%y
# y = y%x
# print(y)

# print("a", "b", "c", sep="sep")
# x = 1//5+1/5
# print(x)

# # tuple[1] = tuple[1]+tuple[0]

# x = float(input())
# y = float(input())
# print(y**(1/x))

# dct = {'uno':'dos', 'tres':'uno', 'dos':'tres'}
# v = dct['tres']
# for k in range(len(dct)):
#     v = dct[v]

# print(v)
def fun(x,y):
    if x == y:
        return x
    else:
        return fun(x,y-1)

print(fun(0,3))