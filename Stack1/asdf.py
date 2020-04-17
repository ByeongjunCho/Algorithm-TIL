# 1267. [S/W 문제해결 응용] 10일차 - 작업순서
import sys
sys.stdin = open('1267_input.txt', 'r')

for tc in range(1, 11):
    V, E = map(int, input().split())
    G = [[] for _ in range(V+1)]
    start_case = set(range(1, V+1)) # 시작값
    input_count = [0] * (V+1) # 각 노드에 들어오는 엣지 수
    caseE = list(map(int, input().split()))

    for i in range(E):
        G[caseE[i << 1]].append(caseE[(i << 1)+1])
        start_case -= {caseE[(i << 1)+1]}
        input_count[caseE[(i << 1)+1]] += 1
    visit = [0] * (V+1)

    # start_case = []
    # for i in range(1, V+1):
    #     if not G[i]:
    #         start_case.append(i)
        # for k in G:
        #     if i in k:
        #         break
        # else:
        #     start_case.append(i)


    # input_count = []
    # # for j in range(0, V + 1):
    # #     input_count.append(len(G[j]))
    # for j in range(0, V + 1):
    #     count = 0
    #     for k in G:
    #         if j in k:
    #             count += 1
    #     input_count.append(count)

    v = start_case.pop()
    visit[v] = 1
    S = [v]
    result = [str(v)]
    # result = []
    while S or start_case:
        # if not S and not start_case:
        #     break

        if not S:
            v = start_case.pop()
            result.append(str(v))
            visit[v] = 1
            S = [v]

        for i in range(len(G[v])):
            w = G[v][i]
            if visit[w] + 1 == input_count[w] and w:

                # if v not in result:
                #     result.append(str(v))
                if str(w) not in result:
                    result.append(str(w))

                # print('{} -> {}'.format(v, w))
                visit[w] += 1
                S.append(v)
                v = w
                break
            elif visit[w]+1 != input_count[w] and input_count[w] > 1 and w:
                visit[w] += 1
                G[v][i] = 0
                # break  
        else:
            v = S.pop()

    print('#{} {}'.format(tc, ' '.join(result)))
    # print(len(result))
    # print('V=', V)
    # print(visit)




