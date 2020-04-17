
# room = []
# for i in range(1, 401):
#     room.append(round((i / 2 - 0.6)))

# for i in range(1, 200, 2):
#     if room[i-1] != room[i]:
#         print(room[i])
T = 30
for test_case in range(1, T + 1):
    student_num = int(input())
    room = [0] * 10

    for _ in range(student_num):
        recent_room, target_room = map(int, input().split())
        recent_room = round((recent_room / 2 - 0.6))
        target_room = round((target_room / 2 - 0.6))
        if recent_room <= target_room:
            for i in range(recent_room, target_room+1):
                room[i] += 1
        else:
            for j in range(target_room, recent_room-1, -1):
                room[j] += 1

    print('#{} {}'.format(test_case, max(room)))

