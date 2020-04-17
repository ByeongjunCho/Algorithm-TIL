## KMP

## Karp-Rabin - 해싱의 개념 사용

- 해싱의 개념 사용

## Boyer-moore 

- 상용으로 가장 널리 사용됨
- 문자집합이 큰 경우
- 최선의 경우 O(N/M), 최악의 경우 O(MN)



### KMP

text = '.......a b c d x .....'

pattern = 'a b c d e'  

겹치는 문자열 = 'abcd'

접두어 : a, ab, abc

접미어 : d cd bcd 

