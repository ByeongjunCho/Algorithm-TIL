# 4408. 자기 방으로 돌아가기

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    student_num = int(input())
    room = [0] * 201

    for _ in range(student_num):
        recent_room, target_room = map(int, input().split())
        if recent_room & 1:
            recent_room += 1 
        if target_room & 1:
            target_room += 1
        
        if recent_room > target_room:
            recent_room, target_room = target_room, recent_room  
        for i in range(recent_room >> 1, (target_room >> 1) + 1):
            room[i] += 1
    

    print('#{} {}'.format(test_case, max(room)))


