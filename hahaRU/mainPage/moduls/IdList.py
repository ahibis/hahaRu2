
class IdList:
    def __init__(self,ids=""):
        if (ids == None):
            ids = ""
        self._ids=ids

    def BinarySearch(self,array="",searchedValue=0,first=0,last=0):
        if first > last:
            return -1
        middle = int((first + last) / 2)
        middleValue = int(array[middle])
        if middleValue == searchedValue:
            return middle
        else:
            if middleValue > searchedValue:
                return self.BinarySearch(array, searchedValue, first, middle - 1)
            else:
                return self.BinarySearch(array, searchedValue, middle + 1, last)

    def BinarySearchPut(self, array="", searchedValue=0, first=0, last=0):
        if first > last:
            return first
        middle = int((first + last) / 2)
        middleValue = int(array[middle])
        if middleValue == searchedValue:
            return -1
        else:
            if middleValue > searchedValue:
                return self.BinarySearchPut(array, searchedValue, first, middle - 1)
            else:
                return self.BinarySearchPut(array, searchedValue, middle + 1, last)

    def hasId(self, Id=0):
        return self.BinarySearchPut(self._ids, Id, 0, len(self._ids) - 1) == -1

    def AddId(self,Id=0):
        f1 = self.BinarySearchPut(self._ids, Id, 0, len(self._ids) - 1)
        if f1 == -1:
            return self._ids
        ch = chr(Id)
        self._ids = self._ids[:f1] + ch + self._ids[f1:]
        return self._ids

    def toList(self):
        l = []
        for a in self._ids:
            l.append(a)
        return l

    def toString(self):
        return self._ids

    def removeId(self,Id=0):
        f = self.BinarySearch(self._ids, Id, 0, len(self._ids) - 1)
        if f == -1:
            return
        self._ids = self._ids[:f]+self._ids[f+1:]