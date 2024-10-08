# 달리기 경주 (Python)

## Source

https://school.programmers.co.kr/learn/courses/30/lessons/178871

## Code

```python
def solution(players, callings):
    rank_to_player = {}
    player_to_rank = {}

    for rank, player in enumerate(players):
        rank_to_player[rank] = player
        player_to_rank[player] = rank

    for calling in callings:
        current_rank = player_to_rank[calling]

        previous_rank = current_rank - 1
        previous_player = rank_to_player[previous_rank]

        rank_to_player[previous_rank] = calling
        rank_to_player[current_rank] = previous_player

        player_to_rank[calling] = previous_rank
        player_to_rank[previous_player] = current_rank

    return list(rank_to_player.values())
```

## How to solve?

이름을 부를 때 마다 매번 리스트를 검색하고 위치를 재정렬 하는 것은 많으 시간이 들어간다.

따라서 O(1)에 연산을 끝낼 수 있는 딕셔너리를 2개 만들어둔 뒤 rank -> player와 player -> rank를 저장한다.

calling을 할 때 마다 두개의 딕셔너리를 호출하여 위치를 바꾸어 준 뒤 최종적으로 rank_to_player를 반환한다.
