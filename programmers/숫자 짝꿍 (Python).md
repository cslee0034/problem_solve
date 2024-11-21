# 숫자 짝꿍 (Python)

## Source

https://school.programmers.co.kr/learn/courses/30/lessons/131128

## Code

```python
def solution(X, Y):
    common = []
    X = sorted(list(map(int, X)), reverse=True)
    Y = sorted(list(map(int, Y)), reverse=True)

    x, y = 0, 0
    while x < len(X) and y < len(Y):
        if X[x] == Y[y]:
            common.append(X[x])
            x += 1
            y += 1
        elif X[x] > Y[y]:
            x += 1
        else:
            y += 1

    if not common:
        return "-1"

    if len(common) == common.count(0):
        return "0"

    return ''.join(map(str, common))
```

## How to solve?

투포인터를 이용해서 풀이했다. X와 Y를 순회 하면서 공통 값을 찾아 common에 넣어준 뒤 조건에 따라 값을 반환한다.
