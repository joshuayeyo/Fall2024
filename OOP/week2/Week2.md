- 자바 기본 프로그래밍
- C:Temp/Java2024 (윈도우 파일 경로 모르겠음;;;)
## sum() 메소드 호출과 리턴
## 자바의 기본 타입
- 특징
	- 기본 타입의 크기가 정해져 있음
	- CPU나 OS에 따라 변하지 않음.
- 문자열은 기본 타입이 아님
	- String 클래스로 문자열 표현 
	- 문자열이 섞인 + 연산 => 문자열로 변환됨
## 변수와 선언
> Tip: var 키워드를 사용하여 변수 타입 생략
- 지역 변수의 선언에만 사용
- 변수 타입 선언 생략
- 변수 선언문에 반드시 초깃값 지정!
## 리터럴(literal)
- 프로그램에서 직접 표현한 값
- 실수 리터럴
	- 소수점 형태나 지수 형태로 표현한 실수
- 문자 리터럴
- `''` 로 문자 표현
- 특수문자 리터럴은 `\`로 시작
- 논리 리터럴은 2개뿐
	- true, false
	- boolean 타입 변수에 치환하거나 조건문에 이용
	- `C나C++과 달리 Java에서 1, 0을 참, 거짓으로 사용 불가`
- null 리터럴
	- 레퍼런스에 대입 사용
- 문자열 리터럴
	- `""` (Quotation Marks)로 묶어 표현
	- 문자열 리터럴은 String 객체로 자동 처리
## 상수
- final 키워드 사용
- 선언 시 초기값 지정
- 실행 중 값 변경 불가
- 상수는 대문자로만 쓴다.
## 자동 타입 변환
작은 타입은 큰 타입으로 자동 변환
- 치환문이나 수식 내에서 타입이 일치하지 않을 때.
## 강제 타입 변환
- 자동 타입 변환이 안되는 경우 : 큰 타입이 작은 타입으로 변환할 때
- 개발자가 필요에 의해 강제로 타입 변환을 지시
	- () 안에 변환할 타입 지정
- 강제 변환은 값 손실 우려... (e.g. 소수점 이하 날아감)
# 원의 면적을 구하는 프로그램을 작성해보자.
Class: CircleArea
Input: radius
Output: 원의 면적> {value}

## 자바에서 키 입력
System.in
Scanner 클래스
```
import java.util.Scanner
```