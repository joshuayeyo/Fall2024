# Ch.07 파이썬 자료구조 II
## 자료구조
- 자료들을 저장하는 여러가지 구조
- 시퀀스
	- 요소로 구성
	- 요소간의 순서
	- 요소들 번호
	- `str`, `bytes`, `bytearray`, `list`, `tuple`, `range`
### 시퀀스
- 동일한 연산을 지원
	- e.g.) indexing, slicing, adding, multiplying
- 내장함수
	- len(), max(), min()\
### 튜플 
- 튜플 vs. 리스트
	- 유사한 구조, but ==변경불가==
	- 동일한 함수 지원 e.g.) indexing, slicing, ... , etc.
- 연산
	- 추가, 변경, 삭제 불가
		- 단, 다른 튜플 / 리스트와는 가능
- enumerate()
	- 반복 가능한 객체를 대상으로,
	- 각 요소에 대해 (인덱스, 값) 형태의 튜플을 반환
- why 튜플?
	- 변경 불가능 => 빠르다, 딕셔너리 키, 데이터변경 금지
### 세트
- (수학에서의 집합) 고유한 값들을 저장하는 자료구조
	- 순서 없음, 위치별 엑세스 불가능
	- `values = set()` : 공백 set을 생성한다.
	- `numbers = {1, 2, 3}`: 초기화된 set을 생성한다.
- 연산
	- all(), any(), enumerate(), len(), max(), min(), sorted(), sum()
- 요소 추가
	- `variable.add(element)`
- 요소 삭제
	- `variable.remove(element)`
	- 예외 발생시키지 않으려면 `discard()` 사용
	- 모든 요소 삭제 : `clear()`
- ==함축연산==, `[]` vs `{}`
- 부분집합 연산
- 비교
- 합집합: `C = A | B` oR `C = A.union(B)`
- 교집합: `C = A & B` oR `C = A.intersection(B)`
- 차집합: `C = A - B` oR `C = A.indifference(B)`
### 딕셔너리
- 자료구조 중의 하나
- 저장정보 : 값(value) +==키(key)==
- `딕셔너리_이름 = {키1: 값1, 키2: 값2, ... , 키n:값n }`
	- 키: 불변객체, 유일 
	- 값: 어떠한 유형도 가능 
- get()
	- 해당 키를 찾을 수 없으면, None 두 번째 인수 저장하면 두 번ㅇ쨰 인수 반환
- pop() 메서드 : 전체 딕셔너리 대상으로 키가  ()인 항목 삭제
	- del_ : 항목삭제&반환