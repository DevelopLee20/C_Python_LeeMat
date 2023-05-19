import ctypes
from array import array

# .so 파일 path 지정
path = "./C_Python4.so"
c_module = ctypes.cdll.LoadLibrary(path)

# 2차원 리스트 생성 - 연산할 행렬식
list1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

list2 = [
    [7,8,9],
    [4,5,6],
    [1,2,3]
]

# 리스트를 포인터로 매핑하기 위해 평탄화 작업 - shape를 (1, -1)로 변경
list1_flatten = []
list2_flatten = []

for i in list1:
    for j in i:
        list1_flatten = list1_flatten + [j]

for i in list2:
    for j in i:
        list2_flatten = list2_flatten + [j]

# 사전 전처리 - array로 변경
# edit_list1 = array('i', list1)
# edit_list2 = array('i', list2)
# .from_buffer -> 파이썬 객체와 C언어에서 할당된 메모리 버퍼를 연결할 수 있음

edit_list1 = array('i', list1_flatten)
edit_list2 = array('i', list2_flatten)

edit_list1 = (ctypes.c_int * len(list1)).from_buffer(edit_list1)
edit_list2 = (ctypes.c_int * len(list2)).from_buffer(edit_list2)

# 함수 리턴 자료형 선언
c_module.lee_matrix_mul.restype = ctypes.POINTER(ctypes.c_int)

# 함수 실행
ret_array = c_module.lee_matrix_mul(edit_list1, edit_list2, len(list1), len(list1[0]))

# ret_array = array('i', ret_array)

# 리턴 값 메모리 덤프(Memory Dump) 방지용 인덱싱 - size 만큼 슬라이싱
# ret_array = ret_array[:len(list1) * len(list1[0])]

print("type: ", type(ret_array))

# 2차원으로 출력
for i in range(len(list1)):
    for j in range(len(list1[0])):
        print(ret_array[i*len(list1) + j], end=" ")
    print()
