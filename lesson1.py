# coding=utf-8
# встроенные функции

# abs(-2)
# pow(3, 2)
# print()
# input()
# len()
# list()
# tuple()
# int()
# str()
# type()
# dir() - tells how many methods

# map(), filter(), reduce()

# map() - 1st element must be a function

# def add(x):
#     return x + 7
# lists = [3, 5, 8, 12]
# add_to = list(map(add, lists))
# print(add_to)

# def add(x):
#     return x + 7
# lists = [3, 5, 8, 12]
# add_to = list(map(abs, lists))
# print(add_to)


# factorial with negative numbers
# def fact(a):
#     if a < 0:
#         a = abs(a)
#     x = 1
#     for i in range(1, a + 1):
#         x *= i
#     return x
#
#
# lists = [3, -5, 8, -2]
# list_new = list(map(fact, lists))
# print(list_new)

# filter - filters
# def test(num):
#     if num <= 3:
#         return num
#
#
# numbers = [1, 19, 13, 3, ]
# result = filter(test, numbers)
# print(list(result))


# polindrome = ["Anna", "civic", "китнаморенеромантик", "Almaz", "Uluk"]
#
#
# def is_pol(strin):
#     new_str = strin[::-1]
#     if strin.lower() == new_str.lower():
#         return strin
#
#
# new_polindrome = list(filter(is_pol, polindrome))
# print(new_polindrome)


# from functools import reduce
#
#
# def proiz(a, b):
#     return a * b
#
#
# numbers = [4, 2, 2, 3]
# num = reduce(proiz, numbers)
# print(num)

# from functools import reduce
#
#
# def square(x):
#     return x ** 2
#
#
# lists = list(range(1, 101))
# add_to = list(map(square, lists))
# print(add_to)
#
#
# def can_divide(y):
#     if y % 3 == 0 and y % 5 == 0:
#         return y
#
#
# lists = list(range(1, 101))
# divided = list(filter(can_divide, lists))
# print(divided)
#
#
# def sum(a, b):
#     return a + b
#
#
# added = reduce(sum, divided)
# added_2 = reduce(sum, add_to)
# added_both = added, added_2
# added_3 = reduce(sum, added_both)
# print(added)
# print(added_2)
# print(added_3)


# Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12),
# и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень).

# def season(num_month):
#     if 9 <= num_month <= 11:
#         print("Fall")
#     elif 3 <= num_month <= 5:
#         print("spring")
#     elif 6 <= num_month <= 8:
#         print("summer")
#     elif 1 <= num_month <= 2:
#         print("winter")
#     elif num_month == 12:
#         print("winter")
#     else:
#         print("There is no such season")
#
#
# inp = int(input("Enter season num: "))
# season(inp)

# Напишите код банкомата, который принимает цифру, выдает деньги с
# номиналом 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 3, 1.





