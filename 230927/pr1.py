class OperList:
    def __init__(self, *args):
        self.__operlist = list(args)

    def __str__(self):
        return f'<{str(self.__operlist)[1:-1]}>'

    def __repr__(self):
        return f'<{str(self.__operlist)[1:-1]}>'

    def __len__(self):
        return self.__operlist.__len__()

    def __add__(self, other):
        if len(self.__operlist) != len(other.__operlist):
            raise
        for i in range(len(self.__operlist)):
            self.__operlist[i] += other.__operlist[i]
        return self.__operlist

    def __sub__(self, other):
        if len(self.__operlist) != len(other.__operlist):
            raise
        for i in range(len(self.__operlist)):
            self.__operlist[i] -= other.__operlist[i]
        return self.__operlist

    def __mul__(self, other):
        if len(self.__operlist) != len(other.__operlist):
            raise
        for i in range(len(self.__operlist)):
            self.__operlist[i] *= other.__operlist[i]
        return self.__operlist

    def append(self, data):
        self.__operlist.append(data)

    def remove(self, data):
        self.__operlist.remove(data)


l = OperList(1, 2, 3, 4)
print(l)
l.append(5)
print(l + l)