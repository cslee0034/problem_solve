# 무인도 여행 (Python)

## Source

https://school.programmers.co.kr/learn/courses/30/lessons/154540

## Code

```python
from collections import deque


def solution(maps):
    answer = []

    row = len(maps)
    col = len(maps[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    maps = list(map(list, maps))
    visit = [[0] * col for _ in range(row)]

    def bfs(x, y):
        if visit[x][y]:
            return

        visit[x][y] = 1

        q = deque()
        q.append((x, y))

        val = 0
        while q:
            cx, cy = q.popleft()
            val += int(maps[cx][cy])

            for i in range(4):
                nx, ny = cx + dx[i], cy + dy[i]
                if 0 <= nx < row and \
                    0 <= ny < col and \
                        not visit[nx][ny] and \
                maps[nx][ny] != 'X':
                    q.append((nx, ny))
                    visit[nx][ny] = 1

        return val

    for r in range(row):
        for c in range(col):
            if maps[r][c] != 'X':
                life = bfs(r, c)
                if life:
                    answer.append(life)

    if answer:
        answer.sort()
        return answer
    else:
        return [-1]
```

## How to solve?

bfs를 통해 map을 순회하면서 자원을 얻는다.

이때 별도로 visit 배열을 선언하고 만약 방문했다면 표시를 해주어 또 다시 방문하지 않도록 해준다.
