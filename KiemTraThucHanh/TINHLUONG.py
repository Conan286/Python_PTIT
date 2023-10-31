import math
import re
class Employee:
    def __init__(self, id, name, salary, date):
        self.__id = id
        self.__name = name
        self.__salary = salary
        self.__date = date

    def get_heso(self):
        group, exp = self.__id[0], int(self.__id[1:3])
        if group == 'A':
            if exp < 4: return 10
            if exp < 9: return 12
            if exp < 16: return 14
            return 20
        if group == 'B':
            if exp < 4: return 10
            if  exp< 9: return 11
            if exp < 16: return 13
            return 16
        if group == 'C':
            if exp < 4: return 9
            if exp < 9: return 10
            if exp < 16: return 12
            return 14
        if group == 'D':
            if exp < 4: return 8
            if exp < 9: return 9
            if exp< 16: return 11
            return 13

    def get_id(self):
        return self.__id[3:]

    def get(self):
        return self.__salary * self.__date * self.get_heso() * 10 ** 3

    def __str__(self):
        return f'{self.__id} {self.__name}'

if __name__ == '__main__':
    mp = {}
    a = []
    for _ in range(int(input())):
        res = input().split()
        mp[res[0]] = ' '.join(res[1:])
    n = int(input())
    for i in range(n): a.append(Employee(input(), input(), int(input()), int(input())))
    for x in a:
        res = x.get_id()
        print(x, end = ' ')
        print(mp[res], x.get())
# 2
# HC Hanh chinh
# KH Ke hoach Dau tu
# 2
# C06HC
# Tran Binh Minh
# 65
# 25
# D03KH
# Le Hoa Binh
# 59
# 24





























