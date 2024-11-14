# 크기가 작은 부분 문자열 (Python)

## Source

https://school.programmers.co.kr/learn/courses/30/lessons/147355?language=python3

## Code

```python
def solution(t, p):
    answer = 0
    t_len = len(t)
    p_len = len(p)

    for i in range(0, t_len - p_len + 1):
        if int(t[i : i + p_len]) <= int(p):
            answer += 1
    return answer
```

## How to solve?

조건에서 주어진대로 sliding window를 구성해서 비교 연산을 한다.
