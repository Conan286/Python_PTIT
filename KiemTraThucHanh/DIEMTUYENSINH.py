import math


class thiSinh:
    def __init__(self, id, name, score, danToc, khuVuc):
        self.__id = id
        self.__name = name
        self.__score = score
        self.__danToc = danToc
        self.__khuVuc = khuVuc

    def diemUuTien(self):
        t = self.__khuVuc
        if t == 1: return 1.5
        if t == 2: return 1
        return 0

    def diemDantoc(self):
        if self.__danToc == 'Kinh': return 0
        return 1.5

    def get(self):
        return self.__score + self.diemUuTien() + self.diemDantoc()

    def __str__(self):
        res = self.get()
        if res >= 20.5: trangThai = 'Do'
        else: trangThai = 'Truot'
        return f'{self.__id} {self.__name} {res} {trangThai}'

if __name__ == '__main__':
    a = []
    for i in range(int(input())):
        Ten = str(input().title())
        name = ""
        for j in Ten.split():
            name += j+' '
        name = name[:-1]
        # print(name)
        score = float(input())
        dantoc = input()
        khuvuc = int(input())
        a.append(thiSinh('TS{:02d}'.format(i + 1), name, score, dantoc, khuvuc))
    a.sort(key = lambda x : -x.get())
    for thisinh in a: print(thisinh)
# 2
# Nguyen  hong ngat
# 22
# Kinh
# 1
#   Chu thi MINh
# 14
# Dao
# 3