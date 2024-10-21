# page 267
## 콘테스트 평가
### 주어진 리스트에서 최대/최소 값을 제거한다.

scores = [10.0, 9.0, 8.3, 7.1, 3.0, 9.0]
print(f'제거 전: {scores}')

scores.sort()
scores.remove(scores[-1])
scores.remove(scores[0])

print(f'제거 후: {scores}')
