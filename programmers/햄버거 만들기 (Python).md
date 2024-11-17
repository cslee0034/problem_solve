# 햄버거 만들기 (Python)

## Source

https://school.programmers.co.kr/learn/courses/30/lessons/133502

## Code

```python
from collections import deque

def solution(ingredient):
    answer = 0
    ingredient = deque(ingredient)
    stack = []

    while (ingredient):
        stack.append(ingredient.popleft())

        if len(stack) >= 4 and stack[-4:] == [1,2,3,1]:
            for _ in range(4):
                stack.pop()
            answer += 1

    return answer
```

## How to solve?

1,2,3,1의 형태가 만들어지면 pop한다. 따라서 stack 자료구조를 이용해서 문제를 풀이한다.
