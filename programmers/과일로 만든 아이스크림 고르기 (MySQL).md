# 과일로 만든 아이스크림 고르기 (MySQL)

## Source

https://school.programmers.co.kr/learn/courses/30/lessons/133025

## Code

```mysql
SELECT
    F.FLAVOR
FROM
    FIRST_HALF F
LEFT JOIN
    ICECREAM_INFO I ON F.FLAVOR = I.FLAVOR
WHERE
    F.TOTAL_ORDER > 3000 AND
    I.INGREDIENT_TYPE = "fruit_based"
```

## How to solve?

문제에서 주어진대로 FIRST_HALF와 ICECREAM_INFO의 조건절을 구성해준다.
