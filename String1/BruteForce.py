# Brute-force 패턴 매칭

p = "CATTCCCTGCGCCGC"                                                                       # pattern
t = "ATTTGTGCATGTTTGAGCTTTTACGTACGAGAAACTGAACGTACCTACGACATTCCCTGCGCCGCCACCCGCTTTTTGAA"      # text

n, m = len(t), len(p)

# 가능한 모든 위치에 대해
for i in range(n-m+1):
    j = 0
    while j < m and t[i + j] == p[j]:
        j += 1
    if j==m:
        # 패턴을 찾음

i = j = 0
while i < n and j < m:
    # if t[i] == p[j]:
    #     i, j = i+1, j+1
    # else:
    #     i = i - j +1
    #     j = 0

    if t[i] != p[j]:
        i = i - j
        j = -1
    i, j = i+1, j+1
    if j == m:
        # i-j를 저장
        j = 0



        # 찾음