# 개인정보 수집 유효기간 (Python)

## Source

https://school.programmers.co.kr/learn/courses/30/lessons/150370?language=python3

## Code

```python
from collections import defaultdict

def format_date(date):
    year, month, day = map(int, date.split("."))
    return year * 28 * 12 + month * 28 + day

def solution(today, terms, privacies):
    answer = []
    terms_dict = defaultdict(int)

    for term in terms:
        key, month = term.split()
        terms_dict[key] = int(month) * 28

    today = format_date(today)

    for i in range(len(privacies)):
        date, key = privacies[i].split()
        date = format_date(date)

        if key in terms_dict and terms_dict[key] + date <= today:
            answer.append(i + 1)

    return answer
```

## How to solve?

연, 월, 일을 int 형태로 바꾸어서 계산을 용이하게 만들어준다.

딕셔너리에 약관 유효기간을 저장해놓고 today와의 차이를 비교해서 만약 약관 유효기간이 지났다면 answer에 더해준다.
