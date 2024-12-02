# 가장 가까운 글자 (JavaScript)

## Source

https://school.programmers.co.kr/learn/courses/30/lessons/142086

## Code

```javascript
function solution(s) {
  const maps = {};
  const answer = [];

  for (let i = 0; i < s.length; i++) {
    const char = s[i];
    if (char in maps) {
      const diff = i - maps[char];
      answer.push(diff);
      maps[char] = i;
    } else {
      maps[char] = i;
      answer.push(-1);
    }
  }

  return answer;
}
```

## How to solve?

for문으로 순회하며 answer 배열에 인덱스의 차이를 넣어준다.
