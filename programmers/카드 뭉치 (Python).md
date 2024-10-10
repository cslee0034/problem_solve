# 카드 뭉치 (Python)

## Source

https://school.programmers.co.kr/learn/courses/30/lessons/159994

## Code

```python
def solution(cards1, cards2, goal):
    left_one, right_one = 0, len(cards1)
    left_two, right_two = 0, len(cards2)

    for word in goal:
        if left_one < right_one and cards1[left_one] == word:
            left_one += 1
            continue
        if left_two < right_two and cards2[left_two] == word:
            left_two += 1
            continue
        return "No"

    return "Yes"
```

## How to solve?

goal을 순회하면서 word가 cards1 혹은 cards2에 있는지 확인한다. 모든 순회가 끝나면 Yes를 반환한다.

## Reviewing the best code

```python
def solution(cards1, cards2, goal):
    for g in goal:
        if len(cards1) > 0 and g == cards1[0]:
            cards1.pop(0)
        elif len(cards2) >0 and g == cards2[0]:
            cards2.pop(0)
        else:
            return "No"
    return "Yes"
```

if-elif-else문과 pop(0)문으로 코드를 더 효율적이고 앍기 쉽게 쓸 수 있다.
