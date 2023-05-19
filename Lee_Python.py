import ctypes
from array import array

class LeeMat:
    def __init__(self) -> None:
        self.module = self.get_so()
    
    def get_so(self) -> ctypes.CDLL:
        path = "./Lee_Cpp.so"
        module = ctypes.cdll.LoadLibrary(path)

        return module

    def create_array(self, list1:list) -> object:
        return Lee_array(list1)

    
class Lee_array:
    def __init__(self, list1:list) -> None:
        self.row = len(list1)
        self.col = len(list1[0])
        self.array = self.make_array(list1)

    def make_array(self, list1:list) -> array:
        flatten = []

        for i in list1:
            for j in i:
                flatten.append(j)

        flatten = array('i', flatten)
        flatten = (ctypes.c_int * len(flatten)).from_buffer(flatten)

        return flatten
    
    def print_array(self, array1:object) -> None:
        for i in self.array:
            pass

if __name__ == "__main__":
    cmod = LeeMat()
    a = cmod.create_array([[1,2,3],[3,4,5]])
    print(a)