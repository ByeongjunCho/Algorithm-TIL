import random




N = 9

def build_data(data):
    for i in range(0, N): # from 0 to 99
        data[i] = random.randint(0, N-1)

def My_index(arr, val):
    """arr에 val의 첫번째 인덱스를 반환.
     없으면 len(arr)반환
     gravity 에서만 사용할함수
     """
    for i in range(len(arr)):
        if arr[i] == val:
            return i
    return len(arr)

# def My_count(arr, val):


# data = [0] * N
# build_data(data)
#
data = [7,4,2,0,0,6,0,7,0]
# tmp = [0] * N
# max_gravity = 0
# for i in range(N-1, -1, -1):
#     for j in range(N):
#         if data[j] == i:
#             data[j] -= 1
#             tmp[j] = 1
#     try:
#         first_index = My_index(tmp, 1)
#     except:
#         first_index = N
#
#     tmp_count = N - first_index - tmp.count(1)
#     max_gravity = max(max_gravity, tmp_count)
#
# print(max_gravity)

max_gravity = 0
for i in range(len(data)):
    data[i]