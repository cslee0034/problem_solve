# 문자열 나누기 (Python)

## Source

https://school.programmers.co.kr/learn/courses/30/lessons/140108

## Code

```python
from collections import defaultdict

def solution(s):
    answer = start = 0
    char_count = defaultdict(int)

    for i in range(len(s)):
        char_count[s[i]] += 1

        start_count = char_count[s[start]]
        if start_count == sum(char_count.values()) - start_count:
            answer += 1
            char_count.clear()
            start = i + 1

    if char_count:
        answer += 1

    return answer
```

## How to solve?

딕셔너리를 이용해서 문제에서 제시된대로 풀이를 구현했다. 하지만 sum(char_count.values())로 매번 합계를 더할 필요는 없다.

```python
def solution(s):
    answer = 0
    sav1=0
    sav2=0
    for i in s:
        if sav1==sav2:
            answer+=1
            a=i
        if i==a:
            sav1+=1
        else:
            sav2+=1
    return answer
```

위의 코드와 같이 a와 b로 추상화 시켜 숫자만 늘려주는 형태로 문제를 해결할 수 있다.
