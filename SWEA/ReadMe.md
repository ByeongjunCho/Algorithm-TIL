## 2005.py 파스칼의 삼각형 => 재귀함수 사용

## 2007.py 대각선 그리기

## 2047.py .upper 매서드(string 대문자 변환)

## 2001.py convolution no padding 구현

## 1954.py 달팽이 숫자(한바퀴 돌면서 숫자 채우기)

```python
def snail(size):
    result = []
    tmp = list(range(1, size*size+1))
    for i in range(0, size):
        result.append(tmp[size*i:size*i+size])
    row, col = 0, -1  # row, col값. 
    # size=4인 경우 채우는 방법은 4 33 22 11 로 맨 앞에 4를 처리하기 위해 col=-1로 한다
    tmp = 1  # 이 값을 이용해 +로 채우고 -로 채우는것을 반복한다.
    count = 1
    while True:

        # 가로를 채운다
        for _ in range(size):
            col += tmp
            result[row][col] = count
            count+=1
        size -= 1    

        if size == 0:
            break
        # 세로를 채운다
        for _ in range(size):
            row += tmp
            result[row][col] = count
            count += 1
        # 거꾸로 가며 채운다
        tmp = -tmp
    return result
```

