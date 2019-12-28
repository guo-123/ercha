# !/usr/bin/python
# -*-coding:utf8-*-

# 1.上三角形
# for i in range(5):
#     print("* "*(i+1))


# 2.下三角形
# for i in  range(4,-1,-1):
#     print("* "*(i+1))

# 3.等腰三角形
# for i in range(5):
#     print("* "*(i+1))
# for i in  range(3,-1,-1):
#     print("* "*(i+1))

# 4.菱形
m=6
for i in range (1,6):
    m=m-1
    print(" "*m,"* "*i)
m=1
for i in range (4,-1,-1):
    m=m+1
    print(" "*m,"* "*i)

# 5.正方形
# for i in range(4):
#     print("* "*4)

# a**2+b**2=c**2  and   a+b+c=1000 的组合
# for a in range(1001):
#     for b in range(1001):
#         for c in range(1001):
#             if a+b+c == 1000 and a**2+b**2 == c**2:
#                 print(a,b,c)

# 6. 质数和
# c=0
# for a in range(2,101):
#     for b  in range (2,a):
#         if a%b == 0:
#             break
#     else:
#             c=c+a
# print(c)

# 7.因数和
# c=0
# for a in range(1,101):
#     for b in range(1,a+1):
#         if  a%b==0:
#             c=c+b
# print(c)



