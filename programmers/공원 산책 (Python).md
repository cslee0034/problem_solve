# 공원 산책 (Python)

## Source

https://school.programmers.co.kr/learn/courses/30/lessons/172928

## Code

```python
def solution(park, routes):
    # park을 2차원 리스트로 변환
    park = list(map(list, park))
    robot = []

    # 로봇의 시작 위치 (S)를 찾기
    for x in range(len(park)):
        for y in range(len(park[0])):
            if park[x][y] == 'S':
                robot = [x, y]  # 로봇 위치를 [x, y] 형태로 저장

    # 로봇을 이동시키는 함수
    def search(robot, direction, times):
        # 시작 위치 저장
        start = robot[:]
        end = robot[:]

        d_map = {
            'E': (0, 1),
            'W': (0, -1),
            'S': (1, 0),
            'N': (-1, 0)
        }

        # 주어진 이동 횟수(times)만큼 반복
        while times > 0:
            # 로봇을 다음 위치로 이동
            nx, ny = \
                robot[0] + d_map[direction][0], robot[1] + d_map[direction][1]

            # 다음 위치가 범위를 벗어나거나 장애물(X)이면 시작 위치로 돌아감
            if nx < 0 or nx >= len(park) or ny < 0 or ny >= len(park[0]) or park[nx][ny] == "X":
                return start

            # 로봇을 다음 위치로 업데이트
            robot = [nx, ny]
            end = robot  # 현재 위치를 end로 업데이트
            times -= 1

        return end  # 마지막 위치 반환

    # 각 경로에 대해 로봇을 이동시킴
    for r in routes:
        direction, times = r.split()  # direction과 times를 분리
        times = int(times)  # 이동 횟수를 정수형으로 변환
        robot = search(robot, direction, times)  # 로봇을 이동

    return robot  # 최종 위치 반환
```

## How to solve?

동서남북으로 지정된 길이만큼 진행하며 그 중간에 장애물이 있을 경우 시작 위치로 돌아간다.

따라서 탐색을 하기 이전에 시작 위치를 저장하고, 탐색이 끝나고 중간에 장애물이 없을 경우에만 변한 위치를 되돌려준다.

BFS로 풀이한다.
