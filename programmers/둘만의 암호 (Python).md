# 둘만의 암호 (Python)

## Source

https://school.programmers.co.kr/learn/courses/30/lessons/155652

## Code

```python
def solution(s, skip, index):
    alpha = [i for i in range(ord("a"), ord("z") + 1)]
    position = -ord("a")
    skip = list(skip)
    skip.sort()

    position_fix = 0
    for char in skip:
        alpha.pop((ord(char) + position + position_fix))
        position_fix -= 1

    answer = ""
    for char in s:
        i = alpha.index(ord(char))
        answer += (chr(alpha[(i + index) % len(alpha)]))

    return answer
```

## How to solve?

skip에 해당하는 문자를 sort()를 통해 앞에서 부터 가져오고 하나씩 제거한다.

하나씩 제거된다는 점을 정정하기 위해 position_fix로 삭제 지점을 교정 해준다.

alpha에서 char를 찾은 뒤 모듈러 연산을 통해 알맞은 알파벳을 찾아준다.

## Reviewing the best code

```python
from string import ascii_lowercase

def solution(s, skip, index):
    result = ''

    a_to_z = set(ascii_lowercase)
    a_to_z -= set(skip)
    a_to_z = sorted(a_to_z)
    l = len(a_to_z)

    dic_alpha = {alpha:idx for idx, alpha in enumerate(a_to_z)}

    for i in s:
        result += a_to_z[(dic_alpha[i] + index) % l]

    return result
```

set()을 이용해서 간편하게 skip을 지울 수 있고 dictionary를 통해 문자의 인덱스에 접근 시간을 줄일 수 있다.
